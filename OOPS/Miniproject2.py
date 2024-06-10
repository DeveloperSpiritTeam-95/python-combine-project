# Project Name: Random Password Generator

import random
import string

print(random.choice([1,2,3,'u','o',5]))

print(random.randint(100,200))
print(random.randrange(200,300))

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)


length = 8
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(charValues)
    

print("Your Random Password: ",password)


#  list comprehensive function [for i n range(length)]

password = "".join([random.choice(charValues) for i in range(length)])

print("Your Random Password: ",password)