class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.acoount_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance
  
  def deposit(self, amount):
    self.balance = amount + self.balance
    print("the new balance is :", self.balance) 

  def withdraw(self, amount):
    self.balance = self.balance - amount
    print("the new balance is :", self.balance) 
  
  def display_balance(self):
    print("the balance is :", self.balance)

rohan = BankAccount('Rohan', 'Walimbe', 55000, 'savings', 1234, 0)
print(vars(rohan))
rohan.deposit(96)
rohan.withdraw(25)
rohan.display_balance()