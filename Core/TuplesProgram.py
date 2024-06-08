# immutable sequences of values in Tuples

tuple = (2,4,6,8,9,3,5,5,2,6,2,8,2,7,2,'t')
print(tuple[len(tuple)-1])
print(tuple[0])
print(tuple[1])
print(tuple)

# tuple methods
print(tuple.count(2)) # get count on given value how many times in tuple

print(tuple.index(6)) # get index on given value

print(type(tuple))

tup = (1)
print(tup)
print(type(tup))

tup = (5.0)
print(tup)
print(type(tup))

tup = ('B')
print(tup)
print(type(tup))

tup = ("prabha")
print(tup)
print(type(tup))

tup = (1,)
print(tup)
print(type(tup))


# count A grade students in tuple

tuple = ('A','C','D','A','A','D','B','B','D','A','B','A')

print(tuple.count('A'),"students are get",tuple[tuple.index('A')],"Grade")


# store the above values in list and sort ascending order
list = ['A','C','D','A','A','D','B','B','D','A','B','A']
    
list.sort()
print(list)
