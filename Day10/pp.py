import datetime

dob_input = input("enter DOB(DD-MM-YY): ")

dob = datetime.datetime.strptime(dob_input, "%d-%m-%Y").date()

today = datetime.date.today()

age = today.year - dob.year 


#agar birthday abhi is saal nhi aaya 
if(today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("your age is:", age)

if age<18 :
    print("you are not eligubale to gve vote i am sorry")
else:
    print("you are able to give vote")

import datetime

print("===AGE CALCULATOR===")

#user input
dob_input = input("enter your DOB(DD-MM-YY): ")
dob = datetime.datetime.strptime(dob_input, "%d-%m-%y").date()

today = datetime.date.today()

age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1
# total days lived 
total_days = (today - dob).days

print("\nYour age is"  ,age,"years")
print("total days lived: ", total_days)

#voting eligibility 
if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote ")

print("============THE END============")