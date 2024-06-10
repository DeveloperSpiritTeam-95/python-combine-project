# class ClassA:
#     varA = "welcome to class A"
    

# class ClassB:
#     varB = "welcome to class B"
    

# class ClassC(ClassA,ClassB):  # multiple inheritance
#     varC = "welcome to class C"
    

# c = ClassC()
# print(c.varA)
# print(c.varB)
# print(c.varC)

class Car:
    def __init__(self,fuelType,size):
        self.fuelType = fuelType
        self.size = size
    
# you want to access the method without self key mention 
# with @staticmethod which is called decorator in python
    @staticmethod       
    def start():
        print("Car started...")
       
    @staticmethod 
    def stop():
        print("Car stopped...")
        

class BMW(Car):
    def __init__(self,name, fuelType, size):
        super().__init__(fuelType, size)        # to assign the parent attribute get super
        self.name = name                        # key in child class then assig from input
        super().start()
    
    @staticmethod
    def holdWishes():
        print("BMW Wishes on you. Thank you visit Again.")
    

bmw = BMW("BMW144","Petrol","Big")
print(bmw.name,bmw.fuelType,bmw.size)
bmw.stop()
bmw.holdWishes()

    
