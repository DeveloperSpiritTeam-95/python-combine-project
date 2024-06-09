
def sum(num1,num2):
    return (num1+num2)

print(sum(10,20))

def sum(num1,num2,num3):
    return(num1+num2+num3)

print(sum(1,2,3))

def substract(sourceValue, removeValue):
    return (sourceValue-removeValue)

print(substract(10,5)) # return value 5

def substract(sourceValue,addExtraValue,removeValue):
    return (sourceValue+addExtraValue-removeValue)


print(substract(10,5,4)) # return value 11

def sayHello(name):
    print("Hello "+name)

sayHello("prabhakar")

def sayHello(name):
    print("Hello",name)

sayHello("Sudhakar")


def average(list):
    sum = 0
    for ele in list:
        sum += ele
    
    print(sum)
    print(sum/len(list))
    
average([97,98,95])


numbers = [1,2,3,4,2,3,4,5,2,6,2,4]
print(numbers,"length",len(numbers))

def printLength(list):
    print(len(list))

printLength(numbers)

# completely my logic
def length(list):
    len = 0
    for ele in list:
        len += 1
    print("given list length: ",len)

length(numbers)
        

heroes = ["Thor","IronMan","C America","Thanos","Hulk","Prabhakar"]
cities = ["Hyderabad","Pune","Mubai","Amaravati","Bengalore","Delhi"]

def printInLine(list):
    for item in list:
        print(item,end=" ")

printInLine(cities)
print()
printInLine(heroes)
print()

def factorialNum(number):
    fact = 1
    for i in range(1, number+1):
        fact *= i
    print(fact)

factorialNum(5)


def convertUSDToINR(usd):
    inr = usd * 83.45
    print(usd,"USD =",inr,"INR")

convertUSDToINR(20)

def convertINRToUSD(inr):
    usd = inr * 0.012
    print(inr,"INR = ",usd,"USD")

convertINRToUSD(1)
convertINRToUSD(83.45)

print("Recursion: ")
def recursion(n):
    if (n == 0):
        return
    print(n)
    recursion(n-1)

recursion(5)

print("factorial using Recursion: ")
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        print(n) # simple explanation
        return n * fact(n-1)

print(fact(5))

def sumOfFirst(number):
    if(number == 0):
        return 0
    else:
        print(number)
        return number + sumOfFirst(number-1)

print(sumOfFirst(10))

print("print list using recursion: ")
def printList(list, idx=0):
    if(idx == len(list)):
        return
    else:
        print(list[idx])
        printList(list,idx+1)

fruits = ["mango","banana","berry","jambu","apple"]
printList(fruits)
    