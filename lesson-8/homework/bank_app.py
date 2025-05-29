import os
import json

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }

    @staticmethod
    def from_dict(data):
        return Account(data["account_number"], data["name"], data["balance"])


class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            raise ValueError("Initial deposit must be non-negative.")
        account = Account(self.next_account_number, name, initial_deposit)
        self.accounts[self.next_account_number] = account
        print(f"Account created successfully! Your account number is: {self.next_account_number}")
        self.next_account_number += 1
        self.save_to_file()

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}")
            print(f"Name: {account.name}")
            print(f"Balance: ${account.balance:.2f}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            print(f"${amount:.2f} deposited successfully. New balance: ${account.balance:.2f}")
            self.save_to_file()
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            try:
                account.withdraw(amount)
                print(f"${amount:.2f} withdrawn successfully. New balance: ${account.balance:.2f}")
                self.save_to_file()
            except ValueError as e:
                print(e)
        else:
            print("Account not found.")

    def save_to_file(self):
        data = {
            "next_account_number": self.next_account_number,
            "accounts": [acc.to_dict() for acc in self.accounts.values()]
        }
        with open("accounts.txt", "w") as file:
            json.dump(data, file)

    def load_from_file(self):
        if not os.path.exists("accounts.txt"):
            return
        with open("accounts.txt", "r") as file:
            data = json.load(file)
            self.next_account_number = data.get("next_account_number", 1001)
            accounts_list = data.get("accounts", [])
            for acc_data in accounts_list:
                acc = Account.from_dict(acc_data)
                self.accounts[acc.account_number] = acc


def main():
    bank = Bank()

    while True:
        print("\n=== Bank Menu ===")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        try:
            if choice == "1":
                name = input("Enter your name: ")
                deposit = float(input("Enter initial deposit: "))
                bank.create_account(name, deposit)

            elif choice == "2":
                acc_num = int(input("Enter your account number: "))
                bank.view_account(acc_num)

            elif choice == "3":
                acc_num = int(input("Enter your account number: "))
                amount = float(input("Enter amount to deposit: "))
                bank.deposit(acc_num, amount)

            elif choice == "4":
                acc_num = int(input("Enter your account number: "))
                amount = float(input("Enter amount to withdraw: "))
                bank.withdraw(acc_num, amount)

            elif choice == "5":
                print("Thank you for using the bank application. Goodbye!")
                break

            else:
                print("Invalid option. Please choose between 1 and 5.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
