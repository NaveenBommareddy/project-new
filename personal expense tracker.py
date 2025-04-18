import os

expenses = []

def menu():
    print("\n  Personal Expense Tracker  ")
    print("1. Add new expense")
    print("2. View all expenses")
    print("3. Get expense summary")
    print("4. Save expenses to file")
    print("5. Load expenses from file")
    print("6. Delete an expense")
    print("7. Exit")

def add_expense():
    description = input("Enter description: ")
    category = input("Enter category: ")
    try:
        amount = float(input("Enter amount: "))
        expenses.append({"description": description, "category": category, "amount": amount})
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_expenses():
    if expenses:
        print("\n  All Expenses  ")
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense['description']} | {expense['category']} | ${expense['amount']:.2f}")
    else:
        print("No expenses recorded.")

def expense_summary():
    if expenses:
        total = sum(exp['amount'] for exp in expenses)
        avg = total / len(expenses)
        print(f"\n  Expense Summary  ")
        print(f"Total expenses: ${total:.2f}")
        print(f"Average expense: ${avg:.2f}")
    else:
        print("No expenses to summarize.")

def save_to_file():
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense['description']},{expense['category']},{expense['amount']}\n")
    print("Expenses saved to file!")

def load_from_file():
    if os.path.exists("expenses.txt"):
        with open("expenses.txt", "r") as file:
            for line in file:
                description, category, amount = line.strip().split(",")
                expenses.append({"description": description, "category": category, "amount": float(amount)})
        print("Expenses loaded from file!")
    else:
        print("No saved expenses found.")

def delete_expense():
    view_expenses()
    try:
        index = int(input("\nEnter the expense number to delete: ")) - 1
        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            print(f"Deleted expense: {removed['description']} | ${removed['amount']:.2f}")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            expense_summary()
        elif choice == '4':
            save_to_file()
        elif choice == '5':
            load_from_file()
        elif choice == '6':
            delete_expense()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()