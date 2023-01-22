import json

#convert json to python
x='{"name":"pooja","age":26,"city":"indore"}'
y=json.loads(x)
print(y['age'])

#convert python to json
x={"name":"pooja","age":26,"city":"indore"}
z=json.dumps(x)
print(z)


