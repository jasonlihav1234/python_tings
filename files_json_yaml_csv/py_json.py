"""
- JSON objects:
{} -> dict
[] -> list
string -> str
numbers -> int or float
true/false -> True/False
null -> None
keys -> double quoted string, no trailing commas
"""

import json

## deserialising json
api_response_str = '{"status": "active"}'
try:
    data = json.loads(api_response_str)
    print(f"Status: {data.get("status", None)}")
except json.JSONDecodeError as e:
    print(f"Failed to parse JSON: {e}")


## parsing json files
# use json.load() to read json, always open files with encoding="utf-8"
# wrap file operations in with
from pathlib import Path

config_path = Path("service_config.json")
with config_path.open("r", encoding="utf-8") as file:
    config_data = json.load(file)

for config in config_data:
    service_name = config.get("service", None)

    if service_name:
        print(f"Service: {service_name}")

## serialising python objects into JSON String
# use json.dumps()
# indent makes output human-readable
# sort_keys=True orders key alphabetically
python_data = {
    "deployment": "frontend-v2",
    "replicas": 3,
    "ports": [80, 443],
    "health_check": True,
    "logs_enabled": None
}

print(f"Pretty JSON:\n{json.dumps(python_data, indent=2, sort_keys=True)}")


### serialising python objects to JSON files
output = {
    "status": "complete",
    "Test": 123
}

output_path = Path("run_summary.json")
with output_path.open("w", encoding="utf-8") as file:
    json.dump(output, file, indent=2)
