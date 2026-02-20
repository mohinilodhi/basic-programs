#random module
import random
print(random.random())
print(random.randint(1, 10))
print(random.uniform(45, 78))

numbers = [2,3,4,5,]
print(random.choice(numbers))

#secrets module
import secrets
print(secrets.randbelow(10))

#mini game using this module
import random
secret__numbers = random.randint(1, 10)

guess = int(input("guess number(1-10): "))

if guess == secret__numbers :
    print("you win")
else:
    print("you lose")