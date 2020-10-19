class BankAccount:
  bank = ""
  
  def __init__(self, first_name, last_name):
    self.first_name= first_name
    self.last_name= last_name
    self.balance = 0
   
    
    
  def account_name(self):
    name = "{} account for  {} {}".format(self.bank, self.first_name, 
       self.last_name, self.deposit)
       
    return name
     
  def deposit(self, amount):   
   self.balance += amount 
   print("You have deposited {} into your account ".format(amount))
  
 
  def withdraw(self, amount):  
    if self.balance>=amount: 
           self.balance-=amount
           print("\n You Withdrew:", amount) 
    else:
           print("\n Insufficient balance  ") 
  
  def  get_balance(self):
   return "The balance for {} is {}".format(self.account_name(), 
   self.balance)
  
  
Acc1 = BankAccount("Nesta", "Karanja")
Acc2 = BankAccount("Slyvia", "Adeli")

print("----------------------------------")
print(Acc1.account_name())
Acc1.deposit(500)
print(Acc1.get_balance())
Acc1.deposit(700)
print(Acc1.get_balance())
Acc1.withdraw(600)
Acc1.withdraw(100)

print("----------------------------------")
print(Acc2.account_name())
Acc2.deposit(20000)
print(Acc2.get_balance())
Acc2.deposit(600)
print(Acc2.get_balance())
Acc2.withdraw(15000)
Acc2.withdraw(500)


    