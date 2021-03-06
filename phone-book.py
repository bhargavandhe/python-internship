import json
from os import getcwd, path

cwd = getcwd()
try:
    contacts = json.load(open(path.join(cwd, 'contacts.json'), 'r'))
except FileNotFoundError:
    open(path.join(cwd, 'contacts.json'), 'w').write('{}')
    contacts = json.load(open(path.join(cwd, 'contacts.json'), 'r'))
i = 1


def create_contact(name='', phone='', group=''):
    if name == '' and phone == '' and group == '':
        print('Add a new contact'.rjust(50, '-'))
        name = input('Enter name: ').lower()
        phone = input('Enter phone-number: ')
        group = input('Enter group (default=""): ').lower()

    if name not in contacts:
        contacts[name] = {
            'phone': phone,
            'group': group
        }
        print('Added to contact list'.rjust(50, '-'))
    else:
        print('Contact already exists!')
        print('-' * 50)


def edit():
    name = input('Enter name of contact to be edited: ').lower()
    if name in contacts:
        print('Earlier contact'.rjust(50, '-'))
        display(name)
        new_name = input('Enter new name: ').lower()
        new_phone = input('Enter new phone number: ')
        new_group = input('Enter new group (default=""): ').lower()

        contacts.pop(name)
        create_contact(new_name, new_phone, new_group)
    else:
        print('No such contact exists!')
        print('-' * 50)


def delete():
    name = input('Enter name of contact to be deleted: ').lower()
    if name in contacts:
        display(name)
        if input('Are you sure, you want to delete this contact(Y/N)? ').lower()[0] == 'y':
            contacts.pop(name)
            print(f'Deleted {name.title()} from contact list'.rjust(50, '-'))
    else:
        print('Not found', name.title(), 'in contact list!')
        print('-' * 50)


def display(name=''):
    if name == '':
        if contacts:
            print('Showing contact list'.rjust(50, '-'))
            for contact in contacts:
                print('Full name:', contact.title())
                print('Phone-number:', contacts[contact]['phone'])
                print('Group:', contacts[contact]['group'])
                print('=' * 30)
            print('End of contacts'.rjust(50, '-'))
        else:
            print('Your contact list is empty!')
            print('-' * 50)
    else:
        if name in contacts:
            print('-' * 50)
            print('Full name:', name.title())
            print('Phone-number:', contacts[name]['phone'])
            print('Group:', contacts[name]['group'])
            print('-' * 50)
        else:
            print('Not found', name, 'in contact list!')
            print('-' * 50)


def show_menu():
    global i
    if i == 1:
        i += 1
        print('  Contacts app  '.center(50, '*'))

    print('1. Create a new contact')
    print('2. Search for a contact')
    print('3. Edit a contact')
    print('4. Delete a contact')
    print('5. Display existing contacts')
    print('6. Display contacts by groups')
    print('7. Exit')
    choice = int(input('>> Enter choice: ')[0])
    return choice if 0 <= choice <= 7 else print('Invalid choice!') or show_menu()


def display_group(g):
    for contact in contacts:
        if contacts[contact]['group'] == g:
            display(contact)


def main():
    menu = show_menu()
    if menu == 1:
        create_contact()
    elif menu == 2:
        name = input('Enter name of contact to be searched: ')
        display(name)
    elif menu == 3:
        edit()
    elif menu == 4:
        delete()
    elif menu == 5:
        display()
    elif menu == 6:
        if contacts:
            groups = []
            for contact in contacts:
                group = contacts[contact]['group']
                if group not in groups:
                    groups.append(group)

            print(groups)
            group = input('Choose a group: ')
            if group in groups:
                display_group(group)
            else:
                print('No such group found!')
        else:
            print('Your contact list is empty!')
            print('-' * 50)
    elif menu == 7:
        print('Exiting'.rjust(50, '-'))
        exit(0)
    json.dump(contacts, open(path.join(cwd, 'contacts.json'), 'w+'), indent=2)
    main()


if __name__ == '__main__':
    main()
