#Real world uses of getter-setter method
# 1. Age can not be float or negative
# 2. Bank balance check before any transaction

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  

    @property
    def balance(self):
        return f"${self._balance:,.2f}"

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Error: Balance cannot be negative.")
        else:
            self._balance = amount

account = BankAccount("test user", 1000)
account.balance = 500   

print(account.balance) 
account.balance = -100  
print(account.balance)  