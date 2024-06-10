print(1+3)             # addition mean in math
print("prabha"+"kar")  # conctination mean in strings
print([1,2,3]+[4,5,6]) # merge mean in list

#  here the mean of fuction completely changes base on accordance
#  set of rules in python that is completely depends on type of input value
#  above + oprator fuctions are implicit in python. python already implemeted and published.
print("====================")
print("Complex Numbers Example Variable overloading")
class Complex:
    
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
        
    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    def sub(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)
    
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)
    

print("Addition Function: ")
num1 = Complex(6,8)
num1.showNumber()

num2 = Complex(4,5)
num2.showNumber()
print("----------")
num3 = num1.add(num2)
num3.showNumber()

print("substraction function: ")
num1 = Complex(6,8)
num1.showNumber()

num2 = Complex(4,5)
num2.showNumber()
print("----------")
num3 = num1.sub(num2)
num3.showNumber()

print("THis is possible with dunder functions")
# like __add__, __sub__, ect
# num4 = num1+num2
# num4.showNumber()

print("Addition using Dunder Function: ")
num1 = Complex(6,8)
num1.showNumber()

num2 = Complex(4,5)
num2.showNumber()
print("----------")
num3 = num1 + num2
num3.showNumber()

print("substraction using Dunder function: ")
num1 = Complex(6,8)
num1.showNumber()

num2 = Complex(4,5)
num2.showNumber()
print("----------")
num3 = num1 - num2
num3.showNumber()


