import json
import requests
import sys

dataset = sys.argv[1]
cell = sys.argv[2]
view_type = sys.argv[3]  # JSON or TEXT

url = f'https://www.nomisweb.co.uk/api/v01/dataset/{dataset}/{cell}.def.sdmx.json'
r = requests.get(url)
d = json.loads(r.text)

result = []

for code in d['structure']['codelists']['codelist'][0]['code']:
    number = code['value']
    description = code['description']['value']
    result.append([number, description])

if view_type == 'JSON':
    print(json.dumps(result, indent=2))
else:
    for number, description in result:
        print(number, description)
