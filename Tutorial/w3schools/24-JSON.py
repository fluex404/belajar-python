import json

x =  '{ "name":"John", "age":30, "city":"New York", "arr": [1, 2,3, 4]}'

print(x)
#convert to directionary
print(json.loads(x))
print(json.loads(x)['name'])
print(json.loads(x)['arr'])
for x in json.loads(x)['arr']:
    print(x)

# convert dict to JSON
x = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
print(x)
print(json.dumps(x))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(x)
print(json.dumps(x))
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, separators=(". ", " = ")))