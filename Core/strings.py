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


