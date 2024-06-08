# store movie names in list from user input

movies = []

# first way
"""
mov1 = input("Enter first movie: ")
mov2 = input("Enter second movie: ")
mov3 = input("Enter third movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)
"""

# second way
"""
mov = input("Enter first movie: ")
movies.append(mov)
mov = input("Enter second movie: ")
movies.append(mov)
mov = input("Enter third movie: ")
movies.append(mov)

print(movies)
"""
# third way
"""
movies.append(input("Enter first movie: "))
movies.append(input("Enter second movie: "))
movies.append(input("Enter third movie: "))

print(movies)
"""

# palindrome list or not
list = [1,2,3,4,5,4,3,2,1]
copyList = list.copy()

copyList.reverse()
if(list == copyList):
    print("palindrome list")
else:
    print("Not a palindrome list")
    


