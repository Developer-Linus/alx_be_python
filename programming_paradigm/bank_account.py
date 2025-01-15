# Define class
class BankAccount:

    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.initial_balance = 0

    def deposit(self, amount):
        self.account_balance += amount
    def withdraw(self, amount):
        if amount > self.account_balance:
            self.account_balance -= amount
        else:
            print("The account balance is insufficient to withdraw {amount}.")
    def display_balance(self):
        print("Current Balance: {self.account_balance}")

    
# Instantiating a class
account = BankAccount(200)
    