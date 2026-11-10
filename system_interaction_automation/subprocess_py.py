"""
- Subprocess module providers interface to spawn child processes, control input/output streams, and inspect their exit status
-> modern recommended method is subprocess.run(), combines execution, output capture, and error handling
-> args = list of strings where the first element in command and rest are params
-> capture_output=True, captures both stdout and stderr into returned CompeletedProcess, use to get human-readable strings
-> text=True, decodes bytes into strings
-> check=True, raises CalledProcessError for non-zero exit codes
-> shell=False, avoids invoking shell, prevents injection vulnerabilities
-> shell=True, only if you fully control the command string
-> CompletedProcess, has attributes args, returncode, stdout, stderr

Common pitfalls
-> forgetting capture_output=True, means result.stdout and result.stderr will be None, and cannot inspect them
-> omitting text=True leaves you with raw bytes
-> using check=False without checking result.returncode can let failures go unnoticed
-> always prefer shell=False, invoking a shell with shell=True and untrusted input enables injection attacks

Tips
-> Wrap subprocess.run in a try block
-> First catch FileNotFoundError to detect missing executables
-> then subproces.TimeoutExpired
-> then CalledProcessError for non-zero exits
-> an except Exception block for any other unexpected issues
"""

import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-c", "print('Hello from subprocess.')"],
    capture_output=True,
    text=True
)

print(f"Args: {result.args}")
print(f"Return code: {result.returncode}")
print(f"Stdout: {result.stdout.strip()}")
print(f"Stderr: {result.stderr.strip()}")
print(f"Return code: {result.returncode}")


"""
- Using subprocess.run(..., check=True) shifts return-code checks into exceptions you can catch
- specific exception types (CalledProcessError, FileNotFoundError, TimeoutExpired) let you distinguish failure modes and respond
- subprocess.CalledProcessError attributes
-> e.returncode = non-zero exit status of the command
-> e.cmd = exact command invoked
-> e.stdout / e.output = caputred standard output if capture_output = True
-> e.stderr = captured standard error, if capture_output = True
    
"""

cmd = ["ls", "missing_dir"]
subprocess.run(cmd, check=True)

try:
    subprocess.run(cmd, check=True)
except subprocess.CalledProcessError as err:
    print(f"Command executed {err.cmd}")
    print(f"Return code: {err.returncode}")
    print(f"STDOUT capture: {err.stdout}")
    print(f"STDERR capture: {err.stderr}")


### Handling FileNotFoundError, subprocess.run() raises FileNotFoundError before running
cmd = ["fakecmd", "--version"]

try:
    subprocess.run(cmd, check=True, capture_output=True, text=True)
except FileNotFoundError as err:
    print("FileNotFoundError caught!")
    print(err)


### Handling timeout expired
# killsprocess if it runs too long
# TimeoutExpired exception raised containing cmd, timeout, and partial stdout/stderr
cmd = ["sleep", "5"]

try:
    subprocess.run(cmd, timeout=2, capture_output=True, text=True)
except subprocess.TimeoutExpired as err:
    print("TimeoutExpired caught!")
    print(err.cmd)
    print(err.timeout)
