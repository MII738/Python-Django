import json
from pathlib import Path

CONTACTS_FILE = Path(__file__).parent / "data" / "contacts.json"


def load_contacts():
    if not CONTACTS_FILE.exists():
        return []
    with open(CONTACTS_FILE, 'r') as f:
        return json.load(f)


def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Contact for {name} added successfully!")


def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for idx, contact in enumerate(contacts, 1):
        print(
            f"{idx}. {contact['name']} | {contact['phone']} | {contact['email']}")


def search_contact():
    query = input("Enter name or phone to search: ").lower()
    contacts = load_contacts()
    found = [c for c in contacts if query in c['name'].lower()
             or query in c['phone']]
    if not found:
        print("No matching contacts found.")
    else:
        for contact in found:
            print(
                f"{contact['name']} | {contact['phone']} | {contact['email']}")


def delete_contact():
    name = input("Enter name of contact to delete: ").lower()
    contacts = load_contacts()
    updated = [c for c in contacts if c['name'].lower() != name]
    if len(updated) == len(contacts):
        print("Contact not found.")
    else:
        save_contacts(updated)
        print("Contact deleted.")


def update_contact():
    name = input("Enter name of contact to update: ").lower()
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Leave blank to keep current value.")
            new_phone = input(
                f"New phone ({contact['phone']}): ") or contact['phone']
            new_email = input(
                f"New email ({contact['email']}): ") or contact['email']
            contact['phone'] = new_phone
            contact['email'] = new_email
            save_contacts(contacts)
            print("Contact updated.")
            return
    print("Contact not found.")


def menu():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

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
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
