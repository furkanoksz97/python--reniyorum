# calculator project
#class -> init -> method/attribute -> function vs method

class Calc(object):
    "calculator"
    #init metodu
    def __init__(self, a, b):
        "initialize values"
        # attribute
        self.value1 = a
        self.value2 = b
        
    
    def add(self):
        "addition a+b = result -> return result"
        return self.value1 + self.value2
        
    
    def multiply(self):
        "multiplication a*b = result -> return result"
        return self.value1 * self.value2
    
    def division(self):
        "division a/b = result -> return result"
        return self.value1 / self.value2
    
    def subtract(self):
        "subtract a-b = result -> return result"
        return self.value1 - self.value2
while True:
     print("Choose add(1), multiply(2), division(3), subtract(4)")
     selection = input("select 1  2  3  4 (or 'quit' to exit): ")

     if selection == "quit":
         break  # exit

     v1 = int(input("first value: "))
     v2 = int(input("second value: "))

     c1 = Calc(v1, v2)
     if selection == "1":
        add_result = c1.add()
        print("Add: {} ".format(add_result))
        
     elif selection == "2":
        multiply_result = c1.multiply()
        print("Multiply: {}".format(multiply_result))
        
     elif selection == "3":
        division_result = c1.division()
        print("Division: {}".format(division_result))
        
     elif selection == "4":
        subtract_result = c1.subtract()
        print("Subtract: {}".format(subtract_result))
     



















