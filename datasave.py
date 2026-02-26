#use of json dump = it is use when we need convert python dict. into JSON file
#use of json load = it is use when we need to return back dat fromJSON into python dict
import json
data = {"name":"mohini","age":18}

json_string = json.dumps(data)

print(json_string)
print(type(json_string))


import json

name = input("Enter name: ")
age = int(input("Enter age: "))

student = {
    "name":name,
    "age":age
}

#save data
with open("student.json", "w") as f:
    json.dump(student, f)

print("data saved successfully")

#load data
with open("student.json", "r") as f:
    data = json.load(f)

print("loaded Data:" , data)