### PyYAML community package is needed
# mapping = key: value
# sequences using leading hyphen plus space
# scalars include string, number, bools, and null
# multi-line scalars can be |
import yaml
import pprint

snippet = """
service: &svc
    name: user-api
    port: 8080
    enabled: true
    tags:
        - key: service
          value: api
staging:
    <<: *svc
    replicas: 2
production:
    <<: *svc
    replicas: 4
"""

parsed = yaml.safe_load(snippet)
pprint.pprint(parsed, indent=4)

multiline_demo = """
literal: |
    line 1
    line 2
    line 3
folded: >
    This is a long string
    that could go out of screen,
    so we will break this up into
    multiple lines to improve readability
"""

pprint.pprint(yaml.safe_load(multiline_demo), indent=4)


### YAML serialisation and deserialisation
# prefer yam.safe_load to prevent abitrary code execution, avoid yaml.load on untrusted data
# wrap with try / except yaml.YAMLError
from pathlib import Path

compose = Path("compose.yaml")

try:
    with compose.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

        for svc, options in config["services"].items():
            print(svc, options)

        print(config)
except yaml.YAMLError as e:
    print("YAML error:")
    print(e)

### yaml.dump -> use this to output it to a file
python_cfg = {
    "sevice": {"name": "listener-service"}
}

output_path = Path("listener_config.yaml")

with output_path.open("w", encoding="utf-8") as file:
    yaml.dump(python_cfg, file, sort_keys=False, default_flow_style=False)

