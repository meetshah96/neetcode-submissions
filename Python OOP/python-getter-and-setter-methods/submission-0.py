class BankAccount:
    def __init__(self, balance: int):
        pass  # Add private balance
        self.balance = balance    
    # TODO: Add getter method for balance
    def get_balance(self):
        return self.balance

    # TODO: Add setter method for balance
    def set_balance(self, new_bal):
        if new_bal < 0:
            print("Cannot set negative balance!")
            return
        self.balance = new_bal 



# Don't modify the code below this line
account = BankAccount(1000)
print(account.get_balance())
account.set_balance(-100)
print(account.get_balance())
account.set_balance(100)
print(account.get_balance())
account.set_balance(0)
print(account.get_balance())
