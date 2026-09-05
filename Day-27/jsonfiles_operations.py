import json
with open("data.json",'r') as f:
    data=json.load(f)
data["Name"]="Srinivas Kandagtla"
data["skills"].extend(["Falsk","Django"])


with open("data.json",'w') as f:
    json.dump(data,f,indent=4)

student={
    "Name": "Srinivas Kandagtla",
    "batch": 63,
    "skills": [
        "Python",
        "Java",
        "DSA",
        "Falsk",
        "Django"
    ]
}
print(student)
print(type(student))
json_data=json.dumps(student)
print(json_data)
print(type(json_data))

student=json.loads(json_data)
print(student)
print(type(student))
