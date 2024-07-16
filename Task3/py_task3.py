import json


def analyze_object(obj):

    if 'id' in obj.keys() and 'value' in obj.keys():
        if obj['id'] in values.keys():
            obj['value'] = values[obj['id']]

    for entry in obj.values():
        if isinstance(entry, dict):
            analyze_object(entry)
        elif isinstance(entry, list):
            analyze_array(entry)


def analyze_array(arr):
    for entry in arr:
        if isinstance(entry, dict):
            analyze_object(entry)
        elif isinstance(entry, list):
            analyze_array(entry)


values = {}

with open('values.json', 'r') as f:
    values_raw = json.load(f)

for obj in values_raw['values']:
    values[obj['id']] = obj['value']


with open('tests.json', 'r') as f:
    report = json.load(f)


analyze_object(report)


with open('report.json', 'w') as f:
    json.dump(report, f, indent=4)
