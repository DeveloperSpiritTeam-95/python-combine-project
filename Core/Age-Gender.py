age = int(input("Enter your age: "))
gender = input("Enter your Gender M/F: ")

if(age>=18 and gender == "M"):
    print("your age: ",age," gender: ",gender)
elif(age>18 and gender == "F"):
    print("your age: ",age," gender: ",gender)
elif(age<18 and gender == "M"):
    print("your age: ",age," gender: ",gender)
else:
    print("your age: ",age," gender: ",gender)