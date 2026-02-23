##sys built in module in python

import sys

print("program start")

#for check version
print(sys.version)

#for check path
print(sys.path)

#for check argv
print(sys.argv)


#(1.)for login
correct_password = input("create your password: ")

print("\n---- login password ------")

#step2
password = input("enter password to login: ")

#check password 
if password != correct_password:
    print("wrong password")
else:
    print("login successfuul")

print("thankyou")

#(2.)menu program for exit
import sys

while True:
    print("1. say hello")
    print("2.exit")

    choice = input("enter choice: ")

    if choice == "1":
        print("hello boss")
    elif choice == "2":
        print("program closed")
        sys.exit()
    else:
        print("invalid choice")
        