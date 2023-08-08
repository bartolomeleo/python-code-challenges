import json

x = '{ "name": "John", "age": 30, "city": [{"hello": "world"}, "dfsds", true]}'

y=json.loads(x)

print(y)