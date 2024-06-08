food = input("Enter food: ")

eat = "eat "+food if food == "cake" else "no cake"
print(eat)

# another way

food = input("Enter food: ")

eat = "eat "+food+" happyly." if food == "cake" or food == "apple" or food == "rice" else "not mension food"

print(eat)

# other one

age = int(input("Enter your age: "))

vote = "your eligible for vote because your age: "+str(age) if age >=18 else "You are not eligible for vote"

print(vote)

# other way direct printing

data = input("Enter fav colour: ")

print("your fav colour is: ",data) if data == "red" or data == "orange" or data == "green" or data == "blue" or data == "white" or data == "black" else print("not mensioned colour")

