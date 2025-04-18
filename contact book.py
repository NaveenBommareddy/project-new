import os

# Dictionary to store contacts
contacts = {}

# Function to display the menu
def menu():
    print("\n--- Contact Book ---")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Save contacts to file")
    print("7. Load contacts from file")
    print("8. Exit")

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ").capitalize()
    if name in contacts:
        print("Contact already exists.")
    else:
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact for {name} added successfully!")

# Function to view all contacts
def view_contacts():
    if contacts:
        print("\n--- All Contacts ---")
        for name, info in contacts.items():
            print(f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\n")
    else:
        print("No contacts available.")

# Function to search for a specific contact
def search_contact():
    name = input("Enter the name of the contact to search: ").capitalize()
    if name in contacts:
        print(f"\nContact found: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ").capitalize()
    if name in contacts:
        print(f"\nCurrent details for {name}:")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        
        phone = input("Enter new phone number (press enter to skip): ")
        email = input("Enter new email (press enter to skip): ")

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email

        print(f"Contact for {name} updated successfully!")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ").capitalize()
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} deleted.")
    else:
        print("Contact not found.")

# Function to save contacts to a file
def save_to_file():
    with open("contacts.txt", "w") as file:
        for name, info in contacts.items():
            file.write(f"{name},{info['phone']},{info['email']}\n")
    print("Contacts saved to file!")

# Function to load contacts from a file
def load_from_file():
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts[name] = {"phone": phone, "email": email}
        print("Contacts loaded from file!")
    else:
        print("No saved contacts found.")

# Main program loop
def main():
    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            save_to_file()
        elif choice == '7':
            load_from_file()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()