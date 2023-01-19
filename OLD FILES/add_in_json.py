import json

with open('ktk.json') as f:
    templates = json.load(f)

print(len(templates[0]))