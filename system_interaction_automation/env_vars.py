"""
- os.getenv retrieves value of environment variable by key, returning None or provided key, always strings
- prevents KeyError exceptions

- os.environ behaves like dictionary mapping environment variable names to their string values
- access missing key gives KeyError, should guard against this
"""

import os

for key in ["HOME", "SHELL"]:
    value = os.getenv(key)
    print(f"{key} = {value if value else "Not set"}")

# adding env variable
os.environ["APP_API_KEY"] = "abc123cd"

env_keys = list(os.environ.keys())
print(f"We have {len(env_keys)} environment variables")


### Setting Environment Variables within Python
# assigning os.environ["KEY"] makes variable available to any subprocesses spawned by the script
# deleteing entry from os.environ removes it from subsequenet oeprations, changes do not persist after script exists
import sys
import subprocess

print(f"Initial MY_CUSTOM_VAR: {os.getenv("MY_CUSTOM_VAR")}")

os.environ["MY_CUSTOM_VAR"] = "SetByOurScript"
print(f"Updated MY_CUSTOM_VAR: {os.getenv("MY_CUSTOM_VAR")}")

result = subprocess.run([
    sys.executable,
    "-c",
    """import os
print(f"Child sees MY_CUSTOM_VAR: {os.getenv("MY_CUSTOM_VAR")}")"""
])

result.stdout

del os.environ["MY_CUSTOM_VAR"]


### dotenv to Manage Local Environment Files
# loaded at runtime into os.environ
from dotenv import load_dotenv

load_dotenv() # needs to pass override=True here if you want os.environ to change it
secret_dotenv_value = os.getenv("MY_DOTENV_VAR")

print(f"Retrieved MY_DOTENV_VAR with value {secret_dotenv_value}")
