import json

path = 'organization.json'
# with open(path, 'r') as f:
#     context = json.loads(f)
#     print(context)
#
#     import json

with open('organization.json') as json_data:
    d = json.load(json_data)
print(d)