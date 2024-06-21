# Join elements of an iterable
words = ["Hello", "World"]
print(" ".join(words))


# Left justify the string with padding
s = "hello"
print(s.ljust(20, '*'))


# Convert string to lowercase
s = "HELLO"
print(s.lower())


# Remove leading characters
s = "   hello"
print(s.lstrip())


# Create a translation table
trans = str.maketrans("aeiou", "12345")
s = "hello"
print(s.translate(trans))



# Partition the string at the first occurrence of separator
s = "hello world"
print(s.partition(" "))


# Replace occurrences of a substring
s = "hello, world!"
print(s.replace("world", "Python"))


# Find the highest index of a substring
s = "hello, world! hello, everyone!"
print(s.rfind("hello"))


# Find the highest index of a substring, raise ValueError if not found
s = "hello, world!"
print(s.rindex("world"))


# Right justify the string with padding
s = "hello"
print(s.rjust(20, '*'))


# Partition the string at the last occurrence of separator
s = "hello world"
print(s.rpartition(" "))


# Split the string from the right
s = "hello world hello"
print(s.rsplit(" ", 1))


# Remove trailing characters
s = "hello   "
print(s.rstrip())


# Split the string
s = "hello world"
print(s.split())

# Split the string at line breaks
s = "hello\nworld"
print(s.splitlines())


# Check if string starts with a prefix
s = "hello, world!"
print(s.startswith("hello"))


# Remove leading and trailing characters
s = "   hello   "
print(s.strip())


# Swap the case of all characters
s = "Hello, World!"
print(s.swapcase())

# Translate the string using the translation table
trans = str.maketrans("aeiou", "12345")
s = "hello"
print(s.translate(trans))


# Pad the string with zeros on the left
s = "42"
print(s.zfill(5))
