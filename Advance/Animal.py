class Animal:
 # Constructor method
    def __init__(self, name):
        self.name = name  # Attribute

    # Method
    def speak(self):
        return f"{self.name} makes a sound."

# Create objects (instances of the class)
dog = Animal("Dog")
cat = Animal("Cat")

# Call methods on objects
print(dog.speak())  # Output: Dog makes a sound.
print(cat.speak())  # Output: Cat makes a sound.