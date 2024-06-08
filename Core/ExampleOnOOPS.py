# Define a class
class ExampleOnOOPS:
 
    # Constructor method
 def __init__(self, name):
        self.name = name  # Attribute

 def __init__(self,age):
      self.name = age

    # Method
 def speak(self):
        return f"{self.name} makes a sound."

# Create objects (instances of the class)
dog = ExampleOnOOPS("Dog")
cat = ExampleOnOOPS("Cat")
age = ExampleOnOOPS(34)

# Call methods on objects
print(dog.speak())  # Output: Dog makes a sound.
print(cat.speak())  # Output: Cat makes a sound.
print(age.speak())
