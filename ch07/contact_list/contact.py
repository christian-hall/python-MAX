class Contact:
    """Contact has information for reaching people"""

    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def print_contact(self):
        print()
        print('--------------------------------------------')
        print('---- Current Contact -----------------------')
        print('--------------------------------------------')
        print(f'Name\t\t{self.first_name} {self.last_name}')
        print(f'Email Address\t{self.email}')
        print(f'Phone Number\t{self.phone}')
        print('--------------------------------------------')
        print()