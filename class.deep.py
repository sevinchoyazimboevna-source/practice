'''
CLASS DEEP DIVE:
1 Encapsulation
2 Inheritance
3 Polymorphism
'''

print("=========Encapsulation==========")
#Encapsulation > public  __private   _protected

class Account():
    #state
    description = "The class makes bank account"

    #constructure
    def __init__(self, owner, amount):
     self.__owner = owner
     self.__amount = amount

    #method
    def get_balance(self):
       print(f"the owner {self.__owner} has {self.__amount} usd")
       
    def deposit(self, amount):
       print("* deposit executed *")
       self.__amount =+ amount

    def withdraw(self, amount):
       print("*  withdraw executed *")
       self.__amount -= amount

    @property
    def holder(self):
       return self.__owner
    
    @holder.setter
    def holder(self, new_owner):
       print("holder.setter:", new_owner)
       self.__owner = new_owner
    
    def change_ownership(self, new_owner):
       print("change_ownership:", new_owner)
       self.__owner = new_owner


my_account = Account("Angel", 7700000000)
my_account.get_balance()

print("------")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()

print("======")
my_account.amount = 1000000
my_account.get_balance()

print("============")

try:
   result = my_account.__amount 
   print("result:", result)
   pass
except Exception as err:
   print("No target state found", err)

account_owner = my_account.holder  #state
print("account_owner", my_account.holder)

# my_account.change_ownership("Javanna")
# getter vs setter
print("account_owner", my_account.holder)
my_account.holder = "Angel"
print("account_ownerss", my_account.holder)