"""
- Any directiory that contains a file named __init__.py is recognized by Python interpreter as a package

- can import entire module using full path, e.g. import devops_utils.file_ops, or access contents like devops_utils.file_ops.check_file_extensions()
- can also use from keyword, from devops_utils import file_ops

"""

# in my_package/__init__.py
# improt json
# from .file_a import helper_function
#
# inside my_package/file_b.py -> in same directory
# from . import json, helper_function
#
# in different directory
# from my_package import json, helper_function

"""
Subpackages
- can have file_utils and network_utils under devops_utils as subpackages
- each subdirectory must contain __init__.py to be recognized by Python as a package

- absolute path follows projects directory structure with explicit path to module
- relative import = path based on location of file performing the import
"""

"""
Running as a module
- need to do python3 -m package.module, sets sys.path to cwd
- if file is both a library (meant to be imported) and a script, then it may raise RuntimeWarning
- should separate library modules (contain only reusable functions and classes) should not contain __name__ == "__main__", from runner scripts

- running scripts inside packages directly using python3 file.py will acuse ModuleNotFoundErrors for absolute imports, need to run it as python -m
"""

"""
Editable installs with pyproject.toml

- makes packages importable from anywhere without manual path hacks or special commands
- the standard professional way
- pip install -e . -> editable or development install with pip, instead of copying files it creates a special link from virtual environment back to original source code
"""
