import json
import os

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be greater than zero")
            return
        self.balance += amount
        print(f"Deposited ₹{amount}. Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be greater than zero")
            return
        if amount > self.balance:
            print("Insufficient balance")
            return
        self.balance -= amount
        print(f"Withdrew ₹{amount}. Balance: ₹{self.balance}")

    def save(self):
        data = {
            "owner": self.owner,
            "balance": self.balance
        }

        accounts = []

        # Load existing data
        if os.path.exists("account.json"):
            with open("account.json", "r") as file:
                try:
                    accounts = json.load(file)

                    # Convert old dict to list
                    if isinstance(accounts, dict):
                        accounts = [accounts]

                except json.JSONDecodeError:
                    accounts = []

        accounts.append(data)

        with open("account.json", "w") as file:
            json.dump(accounts, file, indent=4)


account1 = BankAccount("Ehtesham Anwar", 5000)
account1.withdraw(500)
account1.save()

account2 = BankAccount("Saad", 3000)
account2.deposit(150)
account2.save()
