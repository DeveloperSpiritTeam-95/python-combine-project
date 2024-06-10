# Example 1
class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return (22/7) * self.radius **2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius        
        
c = Circle(21)

print(c.area())
print(c.perimeter())


# Example 2
class Employee:
    name = "give Employee Name"
    age = "Enter your age"
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
        
    
    def showDetails(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Role:",self.role)
        print("Department:",self.dept)
        print("Salary:",self.salary)
        
    

emp = Employee("Junior Developer","Java",float(30000))
emp.showDetails() 

# Example 3
class Engineer(Employee):
    def __init__(self,name,age):
        super().__init__("Software Engineer","Java Dev",float(30000))
        self.name = name
        self.age = age
    

print("Engineer Data:=====>")
eng = Engineer("prabhakar",int(25))
eng.showDetails()


# Example 4

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
        
    
    def __gt__(self,order2):
        return self.price > order2.price
    
order1 = Order("chips",30)
order2 = Order("tea",20)

print(order1 > order2)

        
