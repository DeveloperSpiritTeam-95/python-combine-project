class Person:
    name = "anonymous"
    age = 0
    salary = 0.0
    
    def __init__(self):
       pass
   
   
    def changeName(self,name,age,salary):
        self.__class__.name = name
        self.__class__.age = age
        self.__class__.salary = salary
        
    @staticmethod       # or mension self key
    def changeName1(name,age,salary):
        Person.name = name
        Person.age = age
        Person.salary = salary
    
    @classmethod        # optional but cls argument must
    def changeName2(cls,name,age,salary):
        cls.name = name
        cls.age = age
        cls.salary = salary
    

p = Person()
print(p.name,p.age,p.salary)

p.changeName("prabhakar",25,20000.0)
print(p.name,p.age,p.salary)

p.changeName1("sudhakar",29,30000)
print(p.name,p.age,p.salary)

p.changeName2("Tharun",24,40000)
print(p.name,p.age,p.salary)


class Student:
    
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = self.percentage()
        # self.percentage = str((self.chem+self.phy+self.math)/3)+"%"
    
    @property
    def percentage(self):
        return str((self.chem+self.phy+self.math)/3)+"%"
    
    
s = Student(98,99,97)
print(s.percentage)
s.chem = 86
print(s.percentage)

