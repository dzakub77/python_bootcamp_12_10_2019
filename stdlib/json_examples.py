
import json

text = """{
"ala": "kot",
"x": "y"
}"""

python_obj = [1, 2, 3, 4, 'a', 'b']


obiekt = json.loads(text)
print(obiekt)
print(type(obiekt))


json_obj = json.dumps(python_obj)
print(json_obj)
print(type(json_obj))

with open("dane.json") as fp:
    dane = json.load(fp)
    print(dane)

with open("dane2.json", 'w') as f:
    json.dump(python_obj, f)