"""
list = [2,4,6,8,10,13,14,17,18,20]

print("all elements:")
for element in list:
    print(element)
    
print('odd elements:')
for element in list:
    if(element % 2 != 0):
        print(element)

print("even elements:")
for element in list:
    if(element % 2 == 0):
        print(element)
"""

for element in range(5):
    # element +=1
    print(element)

print("===========")
for element in range(5):
    print(element+1)

print("===========")
for element in range(2,10):
    print(element)

print("===========")
for element in range(2,11,2):
    print(element)

print("=====Even======")
for element in range(2,21,2):
    print(element)

print("=====Even 1======")
for element in range(1,20,2):
    print(element+1)

print("=====Odd======")
for element in range(1,20,2):
    print(element)

print("=====Odd 1======")
for element in range(2,20,2):
    print(element+1)

#  1 to 100
print("===== 1 to 100 ====")
for element in range(1,101):
    print(element)

#  100 to 1
print("==== 100 to 1 ====")
for element in range (100,0,-1):
    print(element)

print("multiplication table")
n = 5
for element in range(1,11):
    print(n,'X',element,'=',(n*element))


print("list example: ")
nums = [1,4,9,16,25,36,49,56,81,100]

for ele in nums:
    print(ele)

print("tuple example: ")
nums = (1,4,9,16,25,36,49,56,81,100)
find = 36
for ele in nums:
    if(find == ele):
        print(ele)
        break
    else:
        print(ele)

print("sum of rang using for loop: ")

sum = 0

for ele in range(0,10):
    sum += ele
    print(sum)

print("sum: ",sum)

sum = 0
n = 7
for i in range(1,n+1):
    sum += i

print("sum: ",sum)

print("using while loop: ")

n =8
sum =0
i=1
while i<=n:
    sum +=  i
    i += 1
print("sum",sum)