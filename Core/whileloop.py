# x =1
# while x<=5:
#     print("Hello")
#     x = x+1  # or x += 1

# i =1
# while i<=10:
#     print('prabha',i)
#     i += 1

# x = 100
# while x >= 1:
#     print(x)
#     x -= 1

# i = 1
# num = 3
# while i<=10:
#     print(num,'X',i,'=',(num*i))
#     i +=1

nums = [1,4,9,16,25,36,49,64,81,100]
i= 0
# while i<=len(nums)-1:
#     print(nums[i])
#     i +=1

# or

# while i< len(nums):
#     print(nums[i])
#     i +=1

#  pattern

# i=1
# while i<=10:
#     print(i*i)
#     i +=1

numbers = (1,4,9,16,25,36,49,64,81,100)
i = 0
# while i< len(numbers):
#     if numbers[i] == 36:
#         print('found',numbers[i]," At index",i)
#         break
#     else:
#         print('finding..')
#     i +=1

while i < len(numbers):
    if (numbers[i] == 36):
        print("skipped")
        i +=1
        continue
    else:
        print(numbers[i])
    i +=1

