"""
- Uses built-in assert statement to declare conditions

Pytest:
- file must start or end with test
- test functions must start with test

Configuration:
1. pyproject.toml
2. pytest.ini
3. tox.ini with [pytest] section
4. setup.cfg

Configuration Options:
- addopts -> default cli flags that Pytest applies on every run
- markers -> pre-registers custom markers with descriptions
- testpaths -> restricts test discovery to listed directories
- python_files -> specifies filename patterns that Pytest treats as test files
- python_classes -> indicates class name patterns Pytest will consider when looking for test cases
- python_function -> Sets function name patterns Pytest uses to identify individual test functions
"""
from typing import TypedDict
import pytest
import time

x: int = 5
assert x == 5, "x should be 5, but it is not"

def test_sring_equality() -> None:
    expected_status = "SUCCESS"
    actual_status = "success".upper()

    assert expected_status == actual_status

class TextAttributes(TypedDict):
    word_count: int
    unique_words: set[str]
    average_word_length: float
    longest_word: str

def calculate_text_attributes(input_text: str) -> TextAttributes:
    split_text = input_text.split()

    return {
        "word_count": 0,
        "unique_words": set(split_text),
        "average_word_length": 0.0,
        "longest_word": "",
    }

def test_word_count() -> None:
    text = "Deploying microservice to Kubernetes cluster."

    assert (calculate_text_attributes(text)["word_count"]) == 5

def test_unique_words() -> None:
    text = "Deploying microservice to Kubernetes cluster."

    text_results = calculate_text_attributes(text)
    len_unique_words = len(text_results["unique_words"])

    assert len_unique_words == 5

### Pytest Rich Failure Output
# use -ra -s
# use pytest.approx for floating point comparision
def test_string_mismatch() -> None:
    expected = "Hello World"
    actual = "hello world"

    assert expected == actual

def test_float_with_approx() -> None:
    calculated_val = 0.1 + 0.2
    expected_val = 0.3

    # will error since floating point comparision
    assert calculated_val == pytest.approx(expected_val)


### Testing exceptions
# use pytest.raises
def test_raises_exception() -> None:
    with pytest.raises(ZeroDivisionError):
        _division = 1 / 0

### Marking test as expected failure
# use @pytest.mark.xfail

"""
- Skipping tests unconditionally
@pytest.mark.skip

- Skipping tests conditionally
@pytest.mark.skipif

- Expected Failures
@pytest.mark.xfail

Markers
- m <expression> CLI option selects tests matching a marker expression
- support logical operators, and, or, and negation with not
- e.g. pytest -m slow, pytest -m "not slow", pytest -m "api and integration"
"""

@pytest.mark.slow
def test_very_long_computations() -> None:
    time.sleep(5)
    assert True

"""
- Fixtures -> supply test data, manage test environment, and provide flexible resources
@pytest.fixture -> fixture that can return or yield resources
- fixture that returns a value runs it setup code, returns the value, and skips teardown logic
- fixture that yields a value becomes a generator, code before yield is setup, yielded value goes to the test, code after is teardown

Using Fixtures in Test Functions
- tests recieve fixture results as parameters, Pytest locates and executes matching fixtures automatically

Fixture Scope and lifecycle
- function scoped = runs for each test function
- session scoped = runs only once for the entire test session

Fixture Teardown
- to ensure cleanup logic executes after tests, define fixtures with yield rather than return
- code after yield always run, even if fail or raises an error

Sharing Fixtures
- define fixtures in conftest.py, makes them available without explicit imports
- place conftest.py in a test directory
"""
ConfigDict = dict[str, int | str]

@pytest.fixture
def sample_config_dict() -> ConfigDict:
    return {
        "api_url": "https://test.api.example.com",
        "timeout": 30,
        "retries": 3
    }

def test_api_url_is_present(sample_config_dict):
    print(" [TEST]: test_api_url_is_present is running... ")
    assert "api_url" in sample_config_dict
    assert sample_config_dict["api_url"] == "https://test.api.example.com"


"""
Parameterized Tests
- allow a single test function to run multiple times with different data, adheres to DRY
- use @pytest.mark.parametrize(argnames, argvalues), takes arg names and a list of values tuples to generate multiple test invocations
"""

def is_valid_hostname_char(a):
    return -1

@pytest.mark.paramterize(
    "input char, expected result",
    [
        ("a", True),
        ("5", True),
        ("-", True),
        ("A", False)
    ]
)
def test_is_valid_hostname_char(input_char: str, expected_result: bool):
    assert is_valid_hostname_char(input_char) is expected_result

"""
- pytest.param() -> wraps a set of parameter values and allows you to attach metadata to that invocation
- id = custom label shown in test report
- marks = one or more markers applied only to that case

- useful if you want to mark individual cases as expected failures or skip them selectively
- by default Pytest creates IDs from parameter values, which is no descriptive -> use pytest.param(..., id="custom_id") to assign clear human-readable name
"""

@pytest.mark.paramterize(
    "input char, expected result",
    [
        pytest.param("a", True, id="lowercase_letter_a"),
        pytest.param("z", True, id="lowercase_letter_z"),
        pytest.param("0", True, id="digit_0"),
        pytest.param("P", False, marks={
                         pytest.mark.xfail(reason="No implementation available for P")
                     })
    ]
)
def test_is_valid_hostname_custom_param(input_char: str, expected_result: bool):
    assert is_valid_hostname_char(input_char) is expected_result


