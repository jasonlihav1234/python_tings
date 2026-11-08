# Can chain multiple generator functions to from a multi-stage pipeline
# No intermediate lists are made, memory stays low even for very large streams
# Each generator holds its own minimal state and passes items downstream on demand
# Use sys.getsizeof() to inspect in-memory size of objects themselves


# 1. Ingest log files
# 2. Filter log files based on either level or message substring
# 3. Extract and return only the message attribute of the logs
import sys
import json

def read_logs(filepath):
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)

def filter_logs(logs, level=None, message_substring=None):
    """Filters any iterable containing dictionaries by either level or message_substring or both

    Args:
        logs (iterable(dict)): Iterable containing the logs to be filtered.
        level (str): The log level to keep. Defaults to None.
        message_substring (str): The pattern to look for irn messages. Defaults to none.

    Returns:
        generator (dict(str)): The json dictionary for the filtered log.
    """

    for log in logs:
        if level is not None and log.get("level", "").lower() != level.lower():
            continue
        if message_substring is not None and message_substring.lower() not in log.get("message", "").lower():
            continue

        yield log

def extract_field(logs, field="message"):
    for log in logs:
        yield log.get(field, "").strip()

logs_gen = read_logs("large_logs.txt")
filter_gen = filter_logs(logs_gen, "INFO", "user")
extract_gen = extract_field(filter_gen, "message")

next(extract_gen)
