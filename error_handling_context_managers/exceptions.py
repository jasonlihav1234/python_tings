"""
OSError -> signals problems with operating system, file, permissions, sockets, path
-> Subclasses = FileNotFoundError, PermissionError, IsADirectoryError, ConnectionRefusedError, TimeoutError

KeyError -> Raised when dict[key] is absent
-> use dict.get(key, default), membership tests, or tailored except KeyError

IndexError -> when list/tuple indices fall outside valid range

ValueError -> Argument type is acceptable but content is invalid, e.g. int("abc")

TypeError -> Operation applied to an object of the wrong type altogether, e.g. len(5) or "a" + 3

AttributeError -> When attribute or method doens't exist on object referenced

ImportError -> when import statement ccannot locate a module/package
-> ModuleNotFoundError is specific subclass, catching ImportError also covers it

raise -> triggers an exception
-> raise TypeError()
"""


### Custom Exception
class AutomationError(Exception):
    pass

class FileProcessingError(Exception):
    pass


def process_file(filepath):
    raise FileProcessingError(f"Failed to process file at path: {filepath}")

try:
    process_file("test.txt")
except FileProcessingError as e:
    print(f"File error: {e}")


### Adding context to custom exceptions
class ConfigValueError(ValueError):
    """Raised when a config value is invalid"""
    def __init__(self, key_name, invalid_value, message="Invalid configuration value."):
        self.key_name = key_name
        self.invalid_value = invalid_value
        full_message = f"{message} for key '{key_name}': received '{invalid_value}'"
        super().__init__(full_message)

try:
    raise ConfigValueError("timeout", -5, message="Timeout cannot be negative")
except ConfigValueError as e:
    print(f"{e}")
    print(f"\t-> key: {e.key_name}")
