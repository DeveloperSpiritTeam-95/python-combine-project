grade = int(input("Enter your Grade:"))

if(grade>=90):
    print("first class")
elif(grade>=70 and grade<90):
    print("second class")
elif(grade>=40 and grade<70):
    print("third class" )
else:
    print("fail")