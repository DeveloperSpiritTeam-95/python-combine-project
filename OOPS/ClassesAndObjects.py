class Student:
    name = ""
    age = 0
    gender = ""
    def __init__(self):
        print("new Student Data Created In Database..")

# s1 = Student()
# print(s1)
# s1.name = "prabhakar"
# s1.age =25
# s1.gender = "M"
# print(s1.name,s1.age,s1.gender)


class Teacher:
    name = ""
    subject = ""
    age = ""
    
    def __init__(self,fullname,subject,age):
        print("This is New Teachers Data...")
        self.name = fullname
        self.subject = subject
        self.age = age
    
    def welcome(self):
        print("welcome Teachers")


# t1 = Teacher("sudhakar","History",29)
# t1.welcome()
# print(t1.name,t1.subject,t1.age)

# t2 = Teacher("prabha","Chemistry",25)
# print(t2.name,t2.subject,t2.age)

class Students:
    school = "Student School"
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        sum = 0
        for i in marks:
            sum += i
        self.average = sum/len(marks)
    
    
    @staticmethod
    def hello():
        print("Hello Students")
    
    

s1 = Students("prabhakar",[99,98,97])
print(s1.name,s1.marks,s1.average)

Students.hello()
s1.hello()

class Account:
    acc_no = 0
    balance = 0.0
    
    def __init__(self,acc_no,balance):
        if(acc_no != -1):
            self.acc_no = acc_no
            self.balance = balance
            print("Account Created.",self.acc_no,"Balance",self.get_balance())
        
    def credit(self,acc_no, balance):
        if(self.acc_no == acc_no):
            self.balance += balance
            print("Credited balance",balance,"current Balance:",self.get_balance()) 
    
    def debit(self, acc_no,balance):
        if(self.acc_no == acc_no and self.balance >= balance):
            self.balance -= balance
            print("Debited balance",balance,"current Balance:",self.get_balance())
        
    def get_balance(self):
        return self.balance
    
            
a1 = Account(123,4000)
a1.credit(123,2000)

print(a1.balance)

a1.debit(123,5000)
print(a1.balance)

# object deleted
# del a1
# print(a1)

class Student2:
    _name = "Global"
    __namePrivate= "Local"
    
    def __init__(self):
        self._name = self._name
        self.__namePrivate = self.__namePrivate
        print(self._name,self.__namePrivate)
    
    def get__namePrivate(self):
        return self.__namePrivate
    
s1 = Student2()
print(s1._name)
print(s1.get__namePrivate())

