import random
import string
import sys

print("Welcome to the Password Generator!")
user = input("Do you want to generate a password? Yes/No")
if user.lower() == "yes":
    print("Proceeding to generate password")
else:
    print("Exit")
    sys.exit()

length = int(input("Enter the length of the password: "))
letters = string.ascii_letters
numbers = string.digits
symbols = "!@#$%^&*()"

all_charecters = letters + numbers + symbols
password = ""
for i in range(length):
    password += random.choice(all_charecters)
print(password)