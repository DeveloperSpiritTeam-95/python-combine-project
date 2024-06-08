import math
# input statement is used to accept valuesm(using keyboard) from user
""""
name = input("Enter your name: ")
age = int(input("Enter your age: "))
grade = input("Enter your grade: ")
salary = float(input("Enter your salary: "))

print("welcome ",name,", age: ",age,", grade: ",grade," and salary is: ",salary)
"""
# input side of a square and print it's area
#  -----
# |     |
#  -----
# square have equal sides so follow the below pro
"""
side = float(input("Enter side of square: "))

print(side * side)
# if you wanna accurate value without decimals
print(int(side*side))

# another way
print(side ** 2)
"""
# input 2 float values and find out average value
"""
from statistics import mean

num1 = float(input("Enter first Number: "))
num2 = float(input("Enter second number: "))

array = [num1,num2]
result = mean(array)

print("Average: ",(num1+num2)/2)
print("average using statistics: ",result)
"""
# input 2 int values print true if num1 greater than num2 or equals to num2 if not print false
"""
num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))

# simple way
print(num1>=num2)

# be clarity on conditional
if(num1>=num2):
    print(num1>=num2)
    print("if")
else:
    print(num1>=num2)
    print("else")
"""

