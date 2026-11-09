"""
Useful for troubleshooting and debugging, auditing and security, monitoring and alerting, and understanding system behaivour

- Logging vs print()
-> all prints look the same, logging uses levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
-> logs automatically add valuable context, timestamp, source file, function name, process ID
-> print goes to stdout, logging can easily direct output to files, rotate logs, send over network, and handle multiple destinations without code changes

logging.getLogger(logger_name) -> retrieves a specific logger by name
logger_name -> can use dots to define hierarchy (app.network.api), is a tree structure with a root
    
"""

# Basic logger
import logging
import logging.handlers
import sys
import os
import time

for lvl in (
    logging.DEBUG,
    logging.INFO,
    logging.WARNING,
    logging.ERROR,
    logging.CRITICAL
):
    print(f"{logging.getLevelName(lvl)} = {lvl}")

## Two Stage filtering
filter_logger = logging.getLogger("demo.filter")
filter_logger.setLevel(logging.INFO) # drops anything less than INFO

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.ERROR)
filter_logger.addHandler(stream_handler) # drops everything less than ERROR

filter_logger.info("INFO")
filter_logger.error("Error")

# Configuring logs and handlers
data_logger = logging.getLogger("demo.data")
data_logger.setLevel(logging.DEBUG)

data_sh = logging.StreamHandler(sys.stdout)
data_sh.setLevel(logging.ERROR)

# writes to a file
# delay = True means only creates file if stuff is written
data_fh = logging.FileHandler("process.log", "w", delay=True)
data_fh.setLevel(logging.INFO)

data_logger.addHandler(data_sh)
data_logger.addHandler(data_fh)

data_logger.debug("DEBUG: will be dropped")
data_logger.info("INFO: file only")
data_logger.warning("WARNING: file only")

## Rotating file handler
# Size-Based Rotation -> rotates when file reaches maxBytes, backupCount determines how many old files to keep
rotating_logs_filename = "rotatingfile.log"

# cleaning up existing log files
for file_name in os.listdir("."):
    if file_name.startswith(rotating_logs_filename):
        os.remove(file_name)

rotating_logger = logging.getLogger("file.rotating")
rotating_logger.setLevel(logging.DEBUG)

rotating_fh = logging.handlers.RotatingFileHandler(
    rotating_logs_filename,
    maxBytes=500,
    backupCount=2,
    encoding="utf-8"
)

rotating_fh.setFormatter(logging.Formatter("%(levelname)-8s %(message)s"))
rotating_logger.addHandler(rotating_fh)

for i in range(30):
    rotating_logger.info(f"Entry {i}: {'Z'*50}")
    time.sleep(0.05)


### Rotating log files by time
# rotates based on elapsed time (when, interval)
# when: S, M, H, D, midnight, W0-W6
# S = every n seconds
# M = every n minutes
# H = every n hours
# D = every n days
# 'midnight' = rorate once per day at midnight
# 'W0-W6' = rotate weekly on a specific weekday, W0 = Sunday
timed_rotating_logs_filename = "timerotatingfile.log"

timed_rotating_logger = logging.getLogger("file.timed")
timed_rotating_logger.setLevel(logging.DEBUG)

timed_rotating_fh = logging.handlers.TimedRotatingFileHandler(
    timed_rotating_logs_filename,
    when="S",
    interval=3,
    backupCount=2,
    encoding="utf-8"
)
timed_rotating_fh.setFormatter(
    logging.Formatter("%(levelname)-8s %(message)s")
)

timed_rotating_logger.addHandler(timed_rotating_fh)

for i in range(30):
    timed_rotating_logger.info(f"Entry {i}: {'Z' * 50}")
    time.sleep(0.2)


### Structured logging
# can log in JSON format
 
from pythonjsonlogger import json

json_logger = logging.getLogger("demo.json")
json_logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
json_formatter = json.JsonFormatter(
    "{asctime}{levelname}{message}",
    style="{",
    json_indent=4,
    rename_fields = {"asctime": "timestamp"}
)

handler.setFormatter(json_formatter)
json_logger.addHandler(handler)
json_logger.info("Strucutred logging initialized")

### Logging with extra content
extra_content = {
    "user_id": "devops1",
    "request_id": "request-1234abc",
    "source_ip": "10.0.0.05"
}

json_logger.warning(
    "Request took longer than 5s to complete",
    extra=extra_content
)

### Logging exceptions as JSON

try:
    result = 1 / 0
except ZeroDivisionError:
    json_logger.exception(
        "Unexpected calculation error",
        extra={"operation": "division"}
    )

### Using Log Confiuration with INI files
import logging.config

config_path = "declarative-config.ini"
logging.config.fileConfig(
    fname=config_path,
)

app_logger = logging.getLogger("app")
app_logger.debug("INI-style fileConfig is working!")


### Declarative logging confi using dictionary
dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)-8s -%(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {
        "config.dict": {
            "level": "DEBUG",
            "handlers": ["console"]
        }
    }
}

logging.config.dictConfig(dict_config)
config_logger = logging.getLogger("config.dict")
config_logger.debug("Test")
config_logger.info("Test2")
