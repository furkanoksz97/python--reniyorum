# %% classes

employee1_name = "Ali"
employee1_age = 33
employee1_address = "İstanbul"

class Employee:
    #attribute = age, address, name
    #behaviour = run
    pass

employee1=Employee()

# %% attribute

class Footballer:
    
    football_club = "Galatasaray"
    age = 30

f1= Footballer()
print(f1.age)
print(f1.football_club)

#%% methods

class Square(object):
    
    edge=5 #meter
    area=0
    def area1(self):
        
        self.area=self.edge*self.edge
        print("Area: ",self.area)
    
    
s1 = Square()
print(s1.edge)
print(s1.area1())

s1.edge =7
s1.area1()

# %% methods vs functions

class Emp(object):
    
    age = 25
    salary = 1000 
    
    def ageSalaryRatio(self):
        
        a = self.age / self.salary
        print("method: ",a)
#function
def ageSalaryRatio (age, salary):
    a = age/salary
    print("function: ",a)
    
e1 = Emp()
e1.ageSalaryRatio()

ageSalaryRatio(30, 3000)


# %% initializer or contructor

class Animal(object):
    
     def __init__(self, a, b): #  (name, age) == ("dog", 3) == (a, b)
         self.name = a
         self.age = b
     
     def getAge(self):
         return self.age
     
     def getName(self):
         print(self.name)
         
        
a1 = Animal("dog", 3)
a2 = Animal("cat", 1)
a3 = Animal("bird", 5)


















