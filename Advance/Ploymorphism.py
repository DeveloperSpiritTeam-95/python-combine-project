# Polymorphism example
class Animal:
    def speak(self):
        return "Animal speaks."

class Dog(Animal):
    def speak(self):
        return "Dog barks."

class Cat(Animal):
    def speak(self):
        return "Cat meows."

def animal_sound(animal):
    return animal.speak()

animal = Animal()
dog = Dog()
cat = Cat()
print(animal_sound(animal))
print(animal_sound(dog))  # Output: Dog barks.
print(animal_sound(cat))  # Output: Cat meows.
