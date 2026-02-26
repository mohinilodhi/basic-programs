import math

print(math.sqrt(25))
print(math.factorial(5))
print(math.pow(2, 7))
print(math.sin(math.pi / 2))
print(math.floor(4.2))
print(math.ceil(3.4556))
print(math.pow(5, 9))
print(math.pow(8, 7))
print(5 ** 2)

numbers = [2, 4, 6, 8]
squares= [num ** 2 for num in numbers]
print(squares)


numbers = [1, 3, 5, 7, 9]
squares = [num ** 2 for num in numbers]
print(squares)


import random
print(random.random())
print(random.randint(29, 45))
print(random.uniform(1, 10))

numbers = [2, 4, 5, 6]
print(random.choice(numbers))

import secrets
print(secrets.randbelow(10))

import random
secrets__numbers = random.randint(1, 10)

guess = int(input("guess numbers (1-10): "))

if guess ==  secrets__numbers:
    print("you win")
else:
    print("you lose")