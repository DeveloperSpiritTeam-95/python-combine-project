
number = 10
numberStr = "20"
string = "prabhakar"
character = 'K'
decimal = 30.9
decimalStr = "40.6"

print("number: ",type(number),number)
print("intNum: ",type(numberStr),numberStr)
print("string: ",type(string),string)
print("character: ",type(character),character)
print("decimal: ",type(decimal),decimal)
print("floatDecimal: ",type(decimalStr),decimalStr)

# typecast here
result = number+int(numberStr)
print(result)

# result = number+ int(string)  throws error
result = str(number)+(string)
print(result)

# you can typecast all data type to str but not to some other data type like below code
# 10 + int("prabha")
# 30.6 + float("K")

result = decimal+ float(decimalStr)
print(result)

result = string.upper()
print(result)
result = string.lower()
print(result)

result = number.bit_count()
print(result)





