# nested program
age = 34
gender = "Female"
if(age > 18):
    if(gender == "Male"):
        print("Driver is Male")
    else:
        print("Driver is Female")
else:
    print("your not ready for driving")
    

# Even program
num = 16

if(num % 2 ==0):
    print("Even")
else:
    print("Odd")
    
# get greatest number from 3 user input numbers
"""
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd Number: "))

if(num1 >= num2 and num1 >= num3):
    print("first one BIG: ",num1)
elif(num2 >= num3):
    print("second one BIG: ",num2)
else:
    print("Third one BIG: ",num3)
    
"""
# multiple of 7

num = 21

if(num % 7 == 0):
    print(num," multiplied by 7")
else:
    print(num," not mutiplied by 7")


