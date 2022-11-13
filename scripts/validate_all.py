import os
import sys
import json

import jsonschema
from box import Box

BASE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")
CONFIGS_DIR = os.path.join(BASE_DIR, "configs")

with open(os.path.join(BASE_DIR, "schema", "fiction_config.schema.json")) as file:
    schema = json.load(file)

# Additionally to purely validating the YAML schema, we could also check things like the validity of URLs
# Depending on the number of configs, this should probably be done selectively for the configs that have been changed

for file in os.listdir(CONFIGS_DIR):
    if file.endswith(".yaml") or file.endswith(".yml"):
        print('Validating "%s"' % file)
        try:
            config = Box.from_yaml(filename=os.path.join(CONFIGS_DIR, file), camel_killer_box=True)
            jsonschema.validate(config, schema)
        except Exception as error:
            print(error)
            sys.exit(1)

print("All configs validated successfully!")
