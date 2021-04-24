from contact import Contact
print("Welcome to the Contact List Application")
choice, contacts = 'y', []
print("\nAdd new contacts - ")
while choice.lower() == 'y':
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    email = input('Enter email: ')
    phone = input('Enter phone (###-###-####): ')
    contacts.append(Contact(first_name, last_name, email, phone))
    print()
    choice = input('Add another contact? (y/n)')
    print()
choice = 'y'
while choice.lower() == 'y':
    contact_name = input('Enter first name of contact: ')
    contact_found = False
    for contact in contacts:
        if contact_name == contact.first_name:
            contact.print_contact()
            print()
            contact_found = True
    if contact_found:
        choice = input('Find another contact? (y/n): ')
    else:
        print('Contact not found. Please try again')
    print()
print('Goodbye')