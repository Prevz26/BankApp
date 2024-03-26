import os
from login import Login
from helpers import Bankapp

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    user = None #set the current user to none

    while True:
        print("WELCOME TO OJOGU'S BANK")
        try:
            user_input = int(input('''1. Login: 
2. Sign-Up: '''))
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        except ValueError:
            print("Enter a number \n ")
            os.system('cls' if os.name == 'nt' else 'clear')

    if user_input == 1:
        email = input("Email: ")
        password = input("Password: ")
        user_login = Login()
        if user_login.validate_login(email, password):
            user = user_login  # Set user to the logged-in user
        else:
            print("Invalid login. Would you like to sign up? (yes/no)")
            if input().lower() == 'yes':
                user_login.signup()
                user = user_login  # Set user to the newly signed-up user 
                
    elif user_input == 2:
        user = Login()
        user.signup()

    if user:  # Check if user is set (either logged in or signed up)
        while True:
            print("1. Create account\n")
            print("2. View Account Details\n")
            print("3. Deposit Money\n")
            print("4. Withdraw Money\n")
            print("5. Check Balance\n")
            print("6. Transaction History\n")
            print("7. Update an account information\n")
            print("8. Exit\n")
                    
            choice = input("Enter your choice: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if choice.isdigit():
                choice = int(choice)
                customers = Bankapp()  
                if choice == 1:
                    customers.create_account()
                elif choice == 2:
                    customers.view_account_details()
                elif choice == 3:
                    customers.deposit()
                elif choice == 4:
                    customers.withdraw()
                elif choice == 5:
                    customers.check_balance()
                elif choice == 6:
                    customers.transaction_history()
                elif choice == 7:
                    customers.update_account_info()
                elif choice == 8:
                    break
                else:
                    print("Enter a valid choice")
    else:
        print("Enter a valid Option")  

if __name__ == "__main__":
    main()