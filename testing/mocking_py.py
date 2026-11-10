"""
Mocking
- replace real dependencies with controlled, fake objects so tests run quickly and deterministically
- unittest.mock.patch -> patch function replaces target object with a mock in a specified scope, either for duration of a function or within a context block

Use Cases
- Network API calls
- Filesystem Operations
- Subprocess Executions
- Time-Dependent Code
"""
from unittest.mock import patch, Mock, MockerFixture
from dummy_functions import check_file_exists, get_user_data

# using unittest.mock.patch
def test_check_file_exists_manual_patch() -> None:
    filepath = "/path/to/some/file.txt"

    with patch("dummy_functions.os.path.exists") as mock_exists:
        mock_exists.return_value = True

        result = check_file_exists(filepath=filepath)
        mock_exists.assert_called_once_with(filepath)
        assert result is True

@patch("dummy_functions.os.path.exists")
def test_check_file_exists_decorator(mock_exists: Mock) -> None:
    filepath = "/path/to/some/file.txt"

    mock_exists.result_value = True

    result = check_file_exists(filepath=filepath)
    assert result is True

"""
MagicMock

- when patch object, can recieve a MagicMock instance that is configurable
- use mock.return_value to define what mock will return when called
- use mock.side_effect to simulate an exception being raised by mock when invoked
- assert_called_with and assert_called_once lets you verify interactions with mock
"""

def test_get_user_data_success(mocker: MockerFixture) -> None:
    mock_api_response = {
        "id": 1,
        "name": "teset user"
    }

    mock_get = mocker.patch("dummy_functions.requests.get")
    mock_get.return_value.status_code = 200

    data = get_user_data(user_id=1)

    mock_get.assert_called_once_with(
        "https://api.example.com/users/1"
    )
    assert data == mock_api_response

"""
Side Effects
- side_effect -> attribute on a mock allows you control its behaviour beyond a single return value
- list of values -> when side_effect set to list, returns next item in that list
- callable -> when side_effect is a function, called with same arugments as mock
- exception -> when side_efefct is an exception -> will raise exception when original function is called

Choosing Between Mock and MagicMock
- Mock = simple replacement that only creates attributes when accessed, raises errors for undefined methods or attributes
- MagicMock = inherits from Mock and implements Python's magic methods __len__, __enter__, etc, by default

- Use Mock by default for stubbing external dependencies to catch unintended interactions
- Use MagicMock only when mocking objects that require special behaviour, such as context managers or iterables
"""
