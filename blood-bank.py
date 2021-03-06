isLogin: bool = False


def login():
    username = input('Enter username: ')
    password = input('Enter password: ')
    # usernames, passwords = getData()


def register():
    pass


def main():
    print('***** XYZ BLOOD-BANK *****')
    print('1. Login\n2. Register\n3. Exit')
    choice = input('Enter choice: ')[0]

    if choice == '1':
        login()
    elif choice == '2':
        register()
    elif choice == '3':
        exit(0)
    else:
        print('Invalid choice!')
        main()
