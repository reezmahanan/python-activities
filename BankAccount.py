class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn.")
        else:
            print("Insufficient funds.")

    def display(self):
        print(f"Account owner: {self.owner}, Balance: {self.balance}")

account = BankAccount("Raj", 2000)
account.display()
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
account.display()
