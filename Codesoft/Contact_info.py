def add_contact(contacts):
    name = input("Enter the contact name: ")
    phone = int(input("Enter the phone number: "))
    email = input("Enter the email address: ")
    address = input("Enter the address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print("Contact added successfully!")
def view_contacts(contacts):
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
def search_contact(contacts):
    search_term = input("Enter the name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term in name or search_term == details['phone']:
            print(f"Found - Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
    if not found:
        print("No contact found.")
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Enter new details (press enter to skip):")
        phone = input("New phone number: ")
        email = input("New email address: ")
        address = input("New address: ")
        
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        print("Contact updated successfully!")
    else:
        print("Contact not found.")
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")
def main():
    contacts = {}
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_contact(contacts)
        elif choice == 2:
            view_contacts(contacts)
        elif choice == 3:
            search_contact(contacts)
        elif choice == 4:
            update_contact(contacts)
        elif choice == 5:
            delete_contact(contacts)
        elif choice == 6:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a choice between 1-6.")

if __name__ == "__main__":
    main()
