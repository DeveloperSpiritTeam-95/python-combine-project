# classRooms = 0
# subjects = {"java","c++","python","java","c","java",
#             "c++","python","ruby","javascript"}
# print(subjects)
# classRooms = len(subjects)
# print("we need ",classRooms,"class rooms.")

subjects = {}
print(type(subjects))
print(subjects)

"""
# two ways insert

# value = int(input("Enter phy : "))
subjects.update({"phy":int(input("Enter phy : "))})

# value = int(input("Enter chem : "))
subjects.update({"chem":int(input("Enter chem : "))})

# value = int(input("Enter math : "))
subjects.update({"math":int(input("Enter math : "))})

print(subjects)
"""

# subjects = {9,9.0} not working python consider 9.0 also 9
subjects = {9,"9.0"}   # but it will work because of string
print(subjects)


values = {
    ("float",9.0),
    ("int",9)
}

print(values)

