print("🤝day02 welcome here")
print("🤷welcome to the number_gusseing🤷")

# genrate a random number between 1 and 100

import random 

secret = random.randint(1,100)

#ask user for a guess

user = int(input("enter your number: "))

#comapre guess with secret
if user == secret:
    print("🎉congratulations! you guessed it right🎉")  
elif user < secret:
    print("too low! try again!")
else:
    print("too high ! try again")   