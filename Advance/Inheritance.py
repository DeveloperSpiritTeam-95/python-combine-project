    # Define a superclass
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Define a subclass inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."
# Create objects
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy barks.
