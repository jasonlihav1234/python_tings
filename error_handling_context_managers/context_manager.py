"""
Classes that implement __enter__(self) and __exit__(self, exc_type, exc_val, exc_tb) methods can be used inside with expression
- __enter__ -> used for setup, returned value will be bound to 'as' target
- __exit__ -> run when indented block under with finished, independently of whether exception was raised or not. If it returns True, suppresses exceptions
- exception information passed to __exit__ through positional parameters

Common Context Manager Examples
1. Files -> with open(...) as f
2. Locks -> with threading.Lock()
3. Tempfiles/Dirs -> with tempfile.TemporaryDirectory() as d
"""

### Custom Resource Management -> Writing Context Managers
class MyContextManager:
    def __init__(self, timeout):
        self.timeout = timeout

    def __enter__(self):
        print("Setup complete")
        return "a simple value"

    # exception_type, exception_value, traceback
    def __exit__(self, *args):
        print(f"Teardown")

        for arg in args:
            print(arg)

        return False

with MyContextManager(timeout=30) as cm:
    print(cm)
    print("inside the block")
    raise ValueError("Simulated problem")


### @contextlib.contextmanager Decorator - turns a generator into context manager
# decorated function needs exactly one yield
# code before yield runs as __enter__
# code after runs as __exit__
import os
from contextlib import contextmanager

@contextmanager
def change_directory(destination):
    origin_dir = os.getcwd()

    try:
        print(f"Changing into {destination}")
        os.makedirs(destination, exist_ok=True)
        os.chdir(destination)
        yield os.getcwd()
    except FileExistsError as e:
        print(e)
        os.chdir(destination)
        yield os.getcwd()
    finally:
        print(f"Reverting to original dir: {origin_dir}")
        os.chdir(origin_dir)

print(f"Start: {os.getcwed()}")

with change_directory("temp_dir") as new_dir:
    print(f"Inside: {new_dir}")

print(f"End: {os.getcwd()}")

