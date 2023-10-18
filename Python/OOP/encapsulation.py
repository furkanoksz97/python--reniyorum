class BankAccount:
    
    def __init__(self, name, money, address):
        self.name = name #global
        self.__money = money #  __ private
        self.address = address
        
 # get and set global
    def getMoney(self):
        return self.__money   

    def setMoney(self, amount):
        self.__money = amount
#private        
    def __increase(self):
        self.__money = self.__money + 500
        
        
        
p1 = BankAccount("Furkan", 5000, "Ankara")
p2 = BankAccount("Ali", 2000, "İstanbul")

print("get method: ",p1.getMoney())
p1.setMoney(500)
print("after set method: ", p1.getMoney())

# p1.__increase()
# print("after raise: ",p1.getMoney())













