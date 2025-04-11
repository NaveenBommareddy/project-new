class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount! Amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            print("Invalid withdrawal amount! Amount must be greater than zero.")

    def view_balance(self):
        print(f"Account balance: ${self.balance:.2f}")

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, account_holder)
            print(f"Account created for {account_holder} with account number {account_number}.")
        else:
            print("Account number already exists.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

def menu():
    bank_system = BankSystem()

    while True:
        print("\n---- Bank Account Management System ----")
        print("1. Create a new account")
        print("2. Deposit money into an account")
        print("3. Withdraw money from an account")
        print("4. View account balance")
        print("5. Exit")

        try:
            choice = int(input("Choose an option (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            bank_system.create_account(account_number, account_holder)

        elif choice == 2:
            account_number = input("Enter account number: ")
            account = bank_system.get_account(account_number)
            if account:
                try:
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                except ValueError:
                    print("Invalid input! Please enter a valid number for the deposit.")
            else:
                print("Account not found!")

        elif choice == 3:
            account_number = input("Enter account number: ")
            account = bank_system.get_account(account_number)
            if account:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Invalid input! Please enter a valid number for the withdrawal.")
            else:
                print("Account not found!")

        elif choice == 4:
            account_number = input("Enter account number: ")
            account = bank_system.get_account(account_number)
            if account:
                account.view_balance()
            else:
                print("Account not found!")

        elif choice == 5:
            print("Thank you for using the Bank Account Management System. Goodbye!")
            break

        else:
            print("Invalid option! Please choose a number between 1 and 5.")

# Running the menu
menu()