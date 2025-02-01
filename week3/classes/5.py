class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
        
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}, {amount} is added to your account")
        print(f"Your current balance is {self.balance}\n")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money on balance\n")
            return False
        self.balance -= amount
        print(f"{self.owner}, {amount} is withdrawn from your account")
        print(f"Your current balance is {self.balance}\n")
        return True
        
acc = Account("Denis")
acc.withdraw(1000)
acc.deposit(100000)
acc.withdraw(5000)