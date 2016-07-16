import json
import yaml
import csv
from pprint import pprint

FILENAME_JSON='input.json'
FILENAME_YAML='input.yaml'
FILENAME_CSV='input.csv'

with open(FILENAME_JSON, 'r') as json_file:
    json_data = json.load(json_file)
pprint(json_data)

with open(FILENAME_YAML, 'r') as yaml_file:
    yaml_data = yaml.load(yaml_file)
pprint(yaml_file)

with open (FILENAME_CSV, 'r') as csv_file:
    reader = csv.reader(csv_file)
    name = next(reader)
    lines = [l for l in reader]

print(names)
print(lines)

