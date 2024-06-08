myName = "prabhakar"
myBroName = 'sudhakar'
str3 = """example way"""

print(myName)
print(myBroName)
print(str3)

# concatination strings
print(myName+myBroName+str3)
# original string together
print(myName,myBroName,str3)

#1.\n goes in next line 
#2.\t give tab space
#3. len() function in string
str1 = "This is string. we are creating in python."
print(str1)
str1 = "This is string.\nwe are creating in python."
print(str1)
str1 = "This is string.\twe are creating in python."
print(str1)

print("my name length: ",len(myName))

# indexing
string = "string indexing"
print(string[2])
print(string[0])
print(string[len(string)-1])

# slicing
str1 = "python learning"
print(str1[0:5])
print(str1[0:6])
print(str1[4:len(str1)-2])

# another version
# missing first parameter python will take 0
# missing last parameter python will take len() value
print(str1[:6]) 
print(str1[3:])

# Negative indexing "python learning"
print(str1[-1])
print(str1[-3])
print(str1[-4:-1])