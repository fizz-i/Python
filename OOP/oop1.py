class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} has been added into your account.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("You have insufficient funds")
        else:
            self.balance -= amount
            print(f"You just withdrawed {amount}")
    
    def display_balance(self):
        print(f"You have a balance of {self.balance} rupees.")

rohit = BankAccount("Rohit", 9000)

rohit.withdraw(10000)
rohit.display_balance()