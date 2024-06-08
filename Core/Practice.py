# store values from user input in 3 subjects in dictionary
# start with empty one and add one by on  subject name as key marks as value
"""
marks = {}

value = int(input("Enter math: "))
marks.update({"math":value})

value = int(input("Enter phy: "))
marks.update({"phy":value})

value = int(input("Enter chem: "))
marks.update({"chem":value})

value = int(input("Enter biology: "))
marks.update({"biology":value})

print(marks)

"""
# store 9, 9.0 in set you can use pre built methods
# one way
values = {'9',9.0}
print(values)

# another way
values = {
    "int":9,
    "float":9.0
}
print(values)
print(values.values())
