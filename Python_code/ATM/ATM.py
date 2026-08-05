

choice = input('Do you want to deposit or withdraw: ').strip().lower()
account = input('What account (1 or 2): ')

pin = ""
balance = 0 

if account == '1':
    pin = '4234234'
    balance = 1000  
elif account == '2':
    pin = '8340138'
    balance = 5000  

else:
    print("Invalid account selected.")
    exit ()

confirm_pin = input('What is your pin: ')

if confirm_pin != pin:
    print("Incorrect PIN. Access denied.")

else:
    
    if choice == 'deposit':
        amount = int(input('How much do you want to deposit? '))
        balance += amount
        print(f"Transaction successful. New balance: ${balance}")
        print(f'You have successfully deposited: ${amount}')
        exit()

    elif choice == 'withdraw':
        amount = int(input('How much do you want to withdraw? '))

        if amount > balance:
            print(f'Declined: You only have ${balance} available.')
        else:
            balance -= amount
            print(f"Transaction successful. New balance: ${balance}")
            print(f'You have successfully withdrawn: ${amount}')
            
    else:
        print("Invalid choice. Please choose 'deposit' or 'withdraw'.")