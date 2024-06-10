class Car:
    color = ""
    @staticmethod
    def start():
        print("car started.")
     
    @staticmethod   
    def stop():
        print("car stopped")
        
    @staticmethod
    def horn():
        print("horn sound")

class TayotaCar(Car):       # single level inheritance
    brand = "Tayota"
    def __init__(self,brand):
        
        self.brand = brand
    
    @staticmethod
    def model():
        print("This is Tayota Model")

t1 = TayotaCar("fortuner")
t1.color = "black"
print(t1.brand,t1.color)
t1.brand = "Parius"
t1.color = "white"
print(t1.brand,t1.color)

t1.start()
t1.stop()
t1.horn()

print(t1.color)

class Fortuner(TayotaCar):   # multilevel inheritance
    color = "Black"
    def __init__(self, type):
        self.type = type

f = Fortuner("fortuner")
print("Car type",f.type,"Brand of Car",f.brand,"Colour of Car",f.color)
f.start()
f.horn()
f.stop()
    
class Diesel(Fortuner):
    def __init__(self, type):
        super().__init__(type)
    
    
d = Diesel("Diesel")
print(d.type)
d.start()

