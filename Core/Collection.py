collection = {1,2,3,4,5,3,2,4,3,"prabha","hello","prabha","hello",9}
print(collection)

print("length: ",len(collection))
print(type(collection))

# empty dictionary syntax
collection = {}
print(collection)
print(type(collection))

# empty set syntax

collection = set()
print(collection)

# type of given syntax
print(type(collection))

# add elements
collection.add(2)
collection.add("prabha")
collection.add(22.0)
collection.add('C')
print(collection)

# remove specified element
collection.remove(2)
print(collection)

# update which is last one added
collection.update("rrr")
print(collection)

collection.update('98997')
print(collection)

# remove random element
collection.pop()
print(collection)

# clear the set like empty
collection.clear()
print(collection)

# set is a collection of unorder items
# each element in the set must be unique and immutable.
# set is mutable as well immutable
# because we can add and remove the elements which is part of mutable
# we can not update the value of the set elements which is part of immutable.
# we can add tuple and dictionay but not list
# set not allow duplicates
 
#  try below code
# collection.add(0,28)
# print(collection)
collection.add(1)
collection.add(5)
print(collection)
collection.add((1,2,3,3,3))
print(collection)
# we can not add list and dictionary in set
# collection.add([1,2,3,4,5])

# printing length
print(len(collection))

set1 = {1,2,3,4,5}
set2 = {9,8,7,6,5,4}

print("unions")
print(set1.union(set2))
print(set2.union(set1))

print("intersections")
print(set1.intersection(set2))
print(set2.intersection(set1))
