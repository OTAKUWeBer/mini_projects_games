bank = {'siam': 2000, 'weber': 20000, 'saadi': 1500, 'samu': 10000}

while True:
    choose = input('1 to check balance\n2 to check full dict\n3 to upgrade balance\n')
    
    if choose == "1":
        name = input('Enter name to check: ')
        if name in bank:
            print(f'{name} has {bank[name]}.')
        else:
            print('There is no account with such username.')
            create_new = input('Do you want to create a new one? (yes/no): ')
            if create_new.lower() == "yes":
                new_name = input('Enter name to add: ')
                try:
                    balance = int(input('Enter balance: '))
                    bank[new_name] = balance
                    print('Account created.')
                except ValueError:
                    print('Invalid input! Please enter a valid number for balance.')
            elif create_new.lower() == 'no':
                continue
            else:
                print('Please enter yes or no.')
        
    elif choose == '2':
        print(bank)
    
    elif choose == '3':
        username = input('Enter your username to edit balance: ')
        if username in bank:
            try:
                balance = int(input('Enter your new balance: '))
                bank[username] = balance
            except ValueError:
                print('Invalid input! Please enter a valid number for balance.')
        else:
            print('There is no account with such username.')
            create_new = input('Do you want to create a new one? (yes/no): ')
            if create_new.lower() == "yes":
                new_name = input('Enter name to add: ')
                try:
                    balance = int(input('Enter balance: '))
                    bank[new_name] = balance
                    print('Account created.')
                except ValueError:
                    print('Invalid input! Please enter a valid number for balance.')
            elif create_new.lower() == 'no':
                continue
            else:
                print('Please enter yes or no.')
    else:
        print('Invalid input! Please choose a valid option.')
