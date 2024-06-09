# import os

# os.remove("Quiz\demo2.txt")

# with open("Quiz\practice.txt","w") as file:
#     file.write("This is prabhakar\n He is want to learn python\n")
#     file.write("File I/O also part of that.\n I like Java Programing language.")
#     file.close()
    

# with open("Quiz/practice.txt","r") as file:
#     data = file.read()
#     data = data.replace("Java","python")
#     print(data)


# with open("Quiz/practice.txt","w") as file:
#     file.write(data)
    

word = "learn"
# with open("Quiz/practice.txt","r") as file:
#     data = file.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")

# def check_Word(word):
#     with open("Quiz/practice.txt","r") as file:
#         data = file.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("Not Found")
            
# check_Word(word)

# def check_for_line(word):
#     data =True
#     line_no=1
#     with open("Quiz/practice.txt","r") as file:
#         while data:
#             data = file.readline()
#             if(word in data):
#                 print("found at",line_no)
#                 return
#             line_no +=1
#     return -1

# check_for_line(word)
count = 0
with open("Quiz\practice.txt","r") as file:
    data = file.read()
    print(data)
    
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            print(int(val))
            count += 1
        
print(count)
            