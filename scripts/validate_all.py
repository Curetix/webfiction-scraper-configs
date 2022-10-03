import os
import sys
import json

import jsonschema
from box import Box

BASE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")
CONFIGS_DIR = os.path.join(BASE_DIR, "configs")

with open(os.path.join(BASE_DIR, "schema", "fiction_config.schema.json")) as file:
    schema = json.load(file)

for file in os.listdir(CONFIGS_DIR):
    if file.endswith(".yaml"):
        print('Validating "%s"' % file)
        try:
            config = Box.from_yaml(filename=os.path.join(CONFIGS_DIR, file), camel_killer_box=True)
            jsonschema.validate(config, schema)
        except Exception as error:
            print(error)
            sys.exit(1)

print("All configs validated successfully!")
