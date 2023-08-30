class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"


class ContactManager:
    # Contacts List
    contacts = []
    # ADD Method
    def add_contact(self, contact):
        self.contacts.append(contact)
        print("New contact added: " + contact.name)
    # DELETE Method
    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                # Send notification
                print("Contact removed: " + contact.name)
                print("Contact deleted successfully")
                break
        return None

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found")
            return
        for contact in self.contacts:
            print(contact)

    def menu(self):
        print("Contact Manager")
        print("1. Add contact")
        print("2. Delete contact")
        print("3. Search contact")
        print("4. Display contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")
        return choice

    def run(self):
        while True:
            choice = self.menu()

            if choice == "1":
                # Add contact
                name = input("Enter contact name: ")
                phone = input("Enter contact phone number: ")
                email = input("Enter contact email address: ")
                contact = Contact(name, phone, email)
                self.add_contact(contact)

            elif choice == "2":
                # Delete contact
                name = input("Enter contact name: ")
                contact = self.search_contact(name)
                if contact:
                    self.remove_contact(name)
                else:
                    print("Contact not found")

            elif choice == "3":
                # Search contact
                name = input("Enter contact name: ")
                contact = self.search_contact(name)
                if contact:
                    print(contact)
                else:
                    print("Contact not found")

            elif choice == "4":
                # Display contacts
                self.display_contacts()

            elif choice == "5":
                # Exit
                break
            
if __name__ == "__main__":
    manager = ContactManager()
    manager.run()
