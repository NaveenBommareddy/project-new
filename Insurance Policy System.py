class InsurancePolicy:
    def __init__(self):
        self.policies = {}

    def add_policy(self, policy_number, customer_name, coverage_amount):
        if policy_number in self.policies:
            print(f"Policy number '{policy_number}' already exists.")
        else:
            self.policies[policy_number] = {
                "customer_name": customer_name,
                "coverage_amount": coverage_amount
            }
            print(f"Insurance policy added for {customer_name} with policy number {policy_number}.")

    def view_policies(self):
        if not self.policies:
            print("No insurance policies found.")
        else:
            print("\n---- Insurance Policies ----")
            for policy_number, details in self.policies.items():
                print(f"Policy Number: {policy_number}")
                print(f"Customer: {details['customer_name']}")
                print(f"Coverage Amount: ${details['coverage_amount']:.2f}")
                print("----------------------------")

    def update_coverage(self, policy_number, new_coverage_amount):
        if policy_number in self.policies:
            self.policies[policy_number]["coverage_amount"] = new_coverage_amount
            print(f"Coverage amount for policy number {policy_number} updated to ${new_coverage_amount:.2f}.")
        else:
            print(f"Policy number '{policy_number}' not found.")

    def delete_policy(self, policy_number):
        if policy_number in self.policies:
            del self.policies[policy_number]
            print(f"Insurance policy number {policy_number} has been deleted.")
        else:
            print(f"Policy number '{policy_number}' not found.")

def menu():
    insurance_system = InsurancePolicy()

    while True:
        print("\n---- Insurance Policy System ----")
        print("1. Add a new insurance policy")
        print("2. View all insurance policies")
        print("3. Update the coverage amount of a policy")
        print("4. Delete an insurance policy")
        print("5. Exit")

        try:
            choice = int(input("Choose an option (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            policy_number = input("Enter policy number: ")
            customer_name = input("Enter customer's name: ")
            try:
                coverage_amount = float(input("Enter the coverage amount: $"))
                insurance_system.add_policy(policy_number, customer_name, coverage_amount)
            except ValueError:
                print("Invalid input! Please enter a valid coverage amount.")

        elif choice == 2:
            insurance_system.view_policies()

        elif choice == 3:
            policy_number = input("Enter policy number to update: ")
            try:
                new_coverage_amount = float(input("Enter new coverage amount: $"))
                insurance_system.update_coverage(policy_number, new_coverage_amount)
            except ValueError:
                print("Invalid input! Please enter a valid coverage amount.")

        elif choice == 4:
            policy_number = input("Enter policy number to delete: ")
            insurance_system.delete_policy(policy_number)

        elif choice == 5:
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option! Please choose a number between 1 and 5.")

# Running the menu
menu()
