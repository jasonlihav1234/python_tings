# Callable that takes another function, adds behaviour before and/or after it runs, and returns a new callable
import time
import random

def simple_task():
    print("running task")

def timing_decorator(original_function):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = original_function(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"{original_function.__name__} took {duration:.3f}s")

        return result

    return wrapper

simple_task = timing_decorator(simple_task)
simple_task()

# @ syntax -> place above func, triggers my_func = decorator_name(my_func) at definiton time
@timing_decorator
def another_task():
    print("running another task...")

another_task()

# Decorator Factory Pattern -> factory function receives configuration arguments and returns actual decorator
def retry(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    print(f"Attempt {attempt}/{max_attempts}")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}")
                    if attempt == max_attempts:
                        raise

        return wrapper
    return decorator

@retry(2)
def sometimes_fails():
    if random.random() < 0.7:
        raise RuntimeError("flaky failure")
    return "Success!"

print(f"Result: {sometimes_fails()}")

# Handling return values in decorators
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"LOG: Calling {func.__name__}")
        value = func(*args, **kwargs)
        print(f"LOG: Finished {func.__name__}")
        return value # needs to be done here
    return wrapper

@log_calls
def multiply(a, b):
    return a * b

print(multiply(2, 3))


## Handling Exceptions in decorators
# Should re-raise exceptions so callers can handle or see errors
def log_and_reraise(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            print(f"[ERROR] {func.__name__} raised {err.__class__.__name__}")
            raise # re raising the exception
    return wrapper


## Using functools.wraps
# Decorator replaces original functiom with wrapper, you lose __name__, __doc__, __module__, and type hints
# confuses debuggers, documentationg generators, anyone relying on help(), inspect, or error traces
# need ot use functools module supplying @wraps(original_func)

from functools import wraps

def correct_decorator(func):
    @wraps(func) # best practice you should always use it
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@correct_decorator
def multiply(a, b):
    return a * b

print(f" __name__: {multiply.__name__}")
print(f" __doc__: {multiply.__doc__}")


## Stacking decorators
# attach more than one decorator to a single function by writing multiple @decorator lines above the def
# each decorator contributes a slice of behaviour keeping core function clear, order matters
def decorator_A(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("A before")
        result = func(*args, **kwargs)
        print("A after")
        return result

    return wrapper

def decorator_B(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("B before")
        result = func(*args, **kwargs)
        print("B after")
        return result

    return wrapper

@decorator_A
@decorator_B
def foo():
    print(" >>> inside function foo")

foo()
