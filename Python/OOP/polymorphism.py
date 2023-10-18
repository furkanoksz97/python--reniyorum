class Employee:
    
    def raisee(self):
        raisee_rate = 0.1
        result = 100 + 100 * raisee_rate
        print("Employee: ", result)
    
class ComputerEng(Employee):
    
    def raisee(self):
        raisee_rate = 0.2
        result = 100 + 100 * raisee_rate
        print("ComputerEng: ", result)
        
class EeEng(Employee):
    
    def raisee(self):
        raisee_rate = 0.3
        result = 100 + 100 * raisee_rate
        print("EeEng: ", result)
        
e1 = Employee()

ce = ComputerEng()

eee = EeEng()

employee_list = [ce, eee]


for employee in employee_list:
    employee.raisee()
    






