"""
Standard project layout with tests
- Separate app and test code via directories
- Have an empty __init__.py inside the tests directory to ensure it can be treated as a package if needed
- When importing modules for tests, use absolute imports
- python -m pytest -> guarantees that cwd is added to sys.path before pytest begins execution
    
"""
