import os 

#for checking path
print("curent working Directory: ")
print(os.getcwd())




#for checking files and folder
print("\nFiles and folders: ")
print(os.listdir())



#for creating new folder
folder_name = input("enter new folder name: ")

os.mkdir(folder_name)
print("folder created successfully🔥")




#dummy practice file banana
with open("practice.txt","w") as f:
    f.write("this is a practice file")

print("practice file created👈")





#for rename the file name
old_name = input("enter old file name: ")
new_name = input("enter old file name: ")

os.rename(old_name, new_name)
print("renamed successfully🔥")




#for delete file
file_name = input("enter file name to delete: ")
os.remove(file_name)
print("file deleted❌")


#for exit from program

import sys

choice = input("enter you choice: ")

if choice == "2":
    print("exiting .....")
    sys.exit()

    
import json
data = {"name":"mohini","class":12}

json_string = json.dumps(data)
print(json_string)

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



































