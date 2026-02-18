print("here we  built the password and also check password")

password  = input("Enter password:  ")

if len(password) >= 8:
    print("length OK")

has_upper = False

for ch in password:
    if ch.isupper():
        has_upper = True

for ch in password:
    if ch.isdigit():
        has_digit = True

for ch in password:
    if not ch.isalnum():
        has_special = True

if len(password) >+ 8 and has_upper and has_digit and has_special:
    print("strong password")
else:
    print("weak password")     