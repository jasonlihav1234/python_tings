"""
- Listing directory contents
-> use os.listpath(dir); gets all list of entry names (files and subdirectories) in a directory
-> use Path(path).iterdir() to iterate over Path objects, can query further with .is_file() or .is_dir()
-> os.listdir returns a plain list of strings

- Making directories
-> os.mkdir(path), creates a single dir, fails if parent doesn't exist
-> os.makedirs(path, exist_ok=False), creates all intermediate directories, set exist_ok=True to ignore existing leaf
-> Path(path).mkdir(parents=True, exist_ok=True) -> pathlib equiv for recursive, idempotent creation

- Removing Files and Directories
-> os.remove(path) or Path(path).unlink(), deletes single file and raises if missing
-> os.rmdir(path) or Path(path).rmdir(), removes empty directory only
-> shutil.rmtree(path), recursively deletes a directory tree and all contents

- Copying Files and Directories
-> shutil.copy(src, dst), copies a file but does not preserve metadata like timestamps and permissions
-> shutil.copy2(src, dst), copies files and attempts to preserve metadata
-> shutil.copytree(src_dir, dst_dir, dirs_exist_ok=False), recursively copies an entire directory tree

- Moving Files and Directories
-> shutil.move(src, dst), move or rename files and directories in one step
-> if dst is an existing directory, src is moved into it, if dst names a file, src is renamed there
-> may involve copy and delete

- Temporary Files and Directories
-> tempfile module provides secure, unique temporary files and directories with optional automatic cleanup
-> generates unique names, avoids collisions, integrates with context managers, works with windows, mac, linux
-> tempfile.TemporaryFile(), creates an unnamed temporary file opened in binary or text mode, deleted automatically when closed
-> tempfile.NamedTemporaryFile(), creates temporary file with a visible name in fs, delete=True removes file when closed, delete=False leaves it for manual cleanup
-> tempfile.TemporaryDirectory(), creates new temporary directory returned as path string, used with a with block directory and everything inside are deleted on exit
"""

import tempfile
import os

temp_dir = tempfile.gettempdir()
print(f"Default temporary directory: {temp_dir}")

with tempfile.TemporaryFile(mode="w+t", encoding="utf-8") as temp_file:
    temp_file.write("This is some temporary data.")
    temp_file.seek(0)
