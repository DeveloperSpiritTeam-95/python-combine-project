# set in the collection of the unordered list
# each element in the set must be unique and immutable

collection = {1,2,3,4,5,6,6,"hello","world","hello",8}
print(collection)
print(len(collection))

# empty set

set = set()
print(set)
set.add(1)
set.add(4)
set.add(2)
set.add(7)

print(set)
set.add("prabha")
set.add((3,4,5,6))

"""
print(set)
set.add({"city":"hyd","location":"nanakram guda","postal":500032}) /# dict not allowed

print(set)
set.add([4,6,8,9,0,5]) # list not allow
"""
print(set)

set.add(9)

set.remove(4)
print(set)

set.pop()
print(set)

set.clear()
print(set)

set1 = {1,3,2,7,10,11}
set2 = {5,7,3,9,2}
print(set1.union(set2))

print(set1.intersection(set2))