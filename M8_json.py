import json

a = {"key1": "value1",
     "key2": None}

#json.dump(a, open("js_test.json", "w"))
astr = json.dumps(a)

t = json.loads(astr)
print(type(t))

print(a)
print(type(a))
print(type(astr))

# c = json.load(open("js_test.json"))
# print(type(c))




