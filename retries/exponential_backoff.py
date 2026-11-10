"""
- Fixed delays overwhelm a recovering server if many clients retry simultaneously
- Exponential backoff increaess the wait time after each failure
- Adding jitter prevents synchronized retry spikes

"""

import requests
import time
import random

def get_with_backoff(url, max_retries=3):
    delay = 1

    for attempt in range(1, max_retries + 1):
        print(f"Attempt {attempt} / {max_retries}...")

        try:
            res = requests.get(url, timeout=10)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as err:
            if err.response.status_code < 500:
                print("Failed with client error code")
                break
            else:
                jitter = random.uniform(-0.1 * delay, 0.1 * delay)
                wait = min(delay * 2, 30) + jitter

                print(err.response.status_code)
                time.sleep(wait)
                delay = min(delay * 2, 30)

    raise RuntimeError(f"All retires to query {url} failed!")
 
