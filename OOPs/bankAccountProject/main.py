import json
import os

FILE_NAME = "accounts.json"

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def to_dict(self):
        return {
            "owner": self.owner,
            "balance": self.balance
        }


# ---------------- FILE HANDLING ---------------- #

def load_accounts():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_accounts(accounts):
    with open(FILE_NAME, "w") as file:
        json.dump(accounts, file, indent=4)


# ---------------- MAIN LOGIC ---------------- #

def create_account():
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))

    if balance < 0:
        print("❌ Balance cannot be negative")
        return

    accounts = load_accounts()

    for acc in accounts:
        if acc["owner"] == name:
            print("❌ Account already exists")
            return

    new_acc = BankAccount(name, balance)
    accounts.append(new_acc.to_dict())
    save_accounts(accounts)

    print("✅ Account created successfully!")


def deposit_money():
    name = input("Enter account holder name: ")
    amount = float(input("Enter amount to deposit: "))

    if amount <= 0:
        print("❌ Amount must be greater than zero")
        return

    accounts = load_accounts()

    for acc in accounts:
        if acc["owner"] == name:
            acc["balance"] += amount
            save_accounts(accounts)
            print("✅ Amount deposited successfully!")
            return

    print("❌ Account not found")


def withdraw_money():
    name = input("Enter account holder name: ")
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("❌ Amount must be greater than zero")
        return

    accounts = load_accounts()

    for acc in accounts:
        if acc["owner"] == name:
            if amount > acc["balance"]:
                print("❌ Insufficient balance")
                return
            acc["balance"] -= amount
            save_accounts(accounts)
            print("✅ Amount withdrawn successfully!")
            return

    print("❌ Account not found")


def show_all_accounts():
    accounts = load_accounts()

    if not accounts:
        print("⚠️ No accounts found")
        return

    print("\n------ All Bank Accounts ------")
    for acc in accounts:
        print(f"👤 Name: {acc['owner']}")
        print(f"💰 Balance: ₹{acc['balance']:.2f}")
        print("-----------------------------")


# ---------------- MAIN MENU ---------------- #

def main():
    while True:
        print("\n====== BANK MANAGEMENT SYSTEM ======")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View All Accounts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            show_all_accounts()
        elif choice == "5":
            print("👋 Thank you for using the Bank A")



main()