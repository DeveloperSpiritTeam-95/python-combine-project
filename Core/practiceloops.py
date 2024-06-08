n=5
sum = 0
print("sum of first n numbers: using for loop")
for element in range(1,n+1):
    sum = sum + element
    print(sum)
    
print("sum",sum)

factorial = 1
print("factorial of first n numbers: using for loop")
for element in range(1,n+1):
    factorial = factorial * element
    print(factorial)
    
print("factorial",factorial)

sum =0
i = 1
print("sum of first n numbers: using while loop")
while i<=5:
    sum += i
    i +=1
print("sum",sum) 

print("factorial of first n numbers: using while loop")
factorial = 1
i = 1
while i<=5:
    factorial *= i
    i += 1
print(factorial)