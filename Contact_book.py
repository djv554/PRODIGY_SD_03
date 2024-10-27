import os

contacts_file = 'contacts.txt'

def load_contacts():
    contacts = {}
    if os.path.exists(contacts_file):
        with open(contacts_file, 'r') as file:
            for line in file:
                name, phone, email = line.strip().split(',')
                contacts[name] = {"phone":phone, "email":email}
    return contacts

def save_contacts(contacts):
    with open(contacts_file, 'w') as file:
        for name, info in contacts.items():
            file.write(f"{name}, {info['phone']},{info['email']}\n")


def add_contact(contacts):
    name = input("Enter contact's name:").strip()
    phone = input("Enter contact's phone number: ").strip()
    email = input("Enter contact's email address: ").strip()
    if name in contacts:
        print(f"the contact {name} already exists!")
    else:
        contacts[name]= {"phone":phone, "email":email}
        save_contacts(contacts)
        print(f"Contact {name} added successfully.")  

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\n-----Contact List-----")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
        print("-------------------------\n")

def edit_contact(contacts):
    name = input("Enter the name of the contacts to edit:").strip()
    if name in contacts:
        print(f"Current details of {name} --> Phone:{contacts[name]['phone']}, Email: {contacts[name]['email']}")
        phone = input("Enter new phone number:").strip()
        email = input("Enter new email address:").strip()

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        
        save_contacts(contacts)
        print(f"Contact {name} updated successfully.")

    else:
        print(f"No contact found with the name {name}.")
    
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete:").strip()
    if name in contacts:
        confirm = input(f"Are you sure you want to delete the contact {name}? (yes/no):").strip().lower()
        if confirm == "yes":
            del contacts[name]
            save_contacts(contacts)
            print(f"Contro; {name} deleted successfully.")
        else:
            print("Delete operation cancelled.")
    else:
        print(f"No contact found with the name {name}.")

def main_menu():
    contacts = load_contacts()
    while True:
        print("\n-----Contact Book-----")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option:").strp()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            print("Exiting Contact Book. Goodbye! ")
            break 
        else: 
            print("Invalid choice. Please try again. ")

if __name__=="__main__":
    main_menu()