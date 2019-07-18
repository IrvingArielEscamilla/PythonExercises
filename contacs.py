import csv

class Contact:

    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name,phone,email)
        self._contacts.append(contact)
        self._save()


    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def _print_contact(self, contact):
        print('--------------------------------------')
        print('Name: {}'.format(contact.name))
        print('Phone: {}'.format(contact.phone))
        print('Emal: {}'.format(contact.email))
        print('--------------------------------------')

    def delete_contact(self,name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self,name):

        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def _not_found(self):
        print('*****************')
        print('not found !!!')

    def update(self,name):
        for idx, contact in enumerate(self._contacts):
            if(contact.name.lower() == name.lower()):
                contact.name = str(input('New name:'))
                contact.phone = str(input('New phone:'))
                contact.email = str(input('New email'))
                self._contacts[idx] = contact
                self._save()
                break

            else:
                self._not_found()

    def _save(self):
        with open ('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone','email'))

            for contact in self._contacts:
                writer.writerow((contact.name,contact.phone,contact.email))

def run():

    contact_book = ContactBook()
    with open('contacts.csv','r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx ==0:
                continue

            contact_book.add(row[0],row[1],row[2])

    while True:
        command = str(input('''
        
        ************ContactBook************
        
        Choose an option:
        
        [a]dd contact
        [u]pdate contact
        [s]earch contact
        [d]elete contact
        [p]rint list
        [e]exit
        
        
        '''))

        if command == 'a':
            print('Add contact')
            name = str(input('Name:'))
            phone = str(input('Phone:'))
            email = str(input('Email @:'))
            contact_book.add(name,phone,email)

        elif command == 'u':
            print('Update contact')
            name = str(input('Name to update: '))
            contact_book.update(name)


        elif command == 's':
            print('Search contact')
            name = str(input('Name to search:'))
            contact_book.search(name)

        elif command == 'd':
            print('Delete contact')
            name = str(input('Name to delete:'))
            contact_book.delete_contact(name)

        elif command == 'p':
            print("Print list")
            contact_book.show_all()

        elif command == 'e':
            print('Bye ...')
            break

        else:
            print('Invalid Option')

run()