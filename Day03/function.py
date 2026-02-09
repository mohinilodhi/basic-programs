###day 03 of this series. 
##function resuable. 
print("welcome to the third (3)day👌")
print("This is the working of function ")


##in this method we make a student profile with full data used...
##witb dictionary..
dic = {
    "student name" : "mohini lodhi  ",
    "student id "  : "0105AL2345",
    "student branch" : "AIML",
    "student subject": "mathematices 1"
}

print(dic('student name'))
print(dic('student id'))
print(dic('student branch'))
print(dic('student subject'))


## write about the info..
## writing about the information..
info = {'name':'karan','age':'19','eligiable':True}
print(info)

print( info.get('name'))
print( info.get('age'))
print( info.get('eligiable'))
print( info.get('keys'))

## with the help of dictonaries.
dic = {
    344: "harry",
    56:"shubham",
    678:"zakir",
    345:"neha"
}
print(dic[344])

# Defining a function.
def greet(name):
    print(f"Hello, {name}!")

# Calling the function.
greet("mohini")
greet("Python Learner")
    
