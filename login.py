# from csv import DictWriter, DictReader

import os
import time
from fileIO import File_IO
from utils import Utils

class Login:
    def __init__(self) -> None:
        self.IO = File_IO()
        self.utils = Utils()
        self.data = self.utils.default_val()

    def validate_login(self, email, password) -> bool:
        self.email = email
        self.password = password
        """This method validates the login system"""
        login_counter = 0
        login_max = 3
        while login_counter < login_max:
                #read the csv file
                file_data = self.IO.read()
                print(file_data)
                email_found = False  # Flag to track if email is found
                for row in file_data:
                    #checks if the email is found
                    if row["email"] == self.email:
                        #flag the email to true
                        email_found = True
                        #checks if the password is found
                        if row["password"] == self.password:
                            print("Login successful!")
                            time.sleep(3)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            return True

                        #when email is found but password is incorrect
                        else:
                            print("Incorrect Email or password. Please try again.")
                            login_counter += 1
                            if login_counter < login_max:
                                # Prompt for new login details
                                self.email = input("Enter your email: ")
                                self.password = input("Enter your password: ")
                            else:
                                print("Exceeded maximum login attempts. Exiting.")
                                exit()
                #when email is not found
                if not email_found:
                    print("Account does not exist. Please signup\n")
                    self.signup()
                    break

    def signup(self):
        """This method handles the sign-up process"""
        self.first_name = input("Enter your First Name: ")
        self.middle_name = input("Enter your Middle Name: ")
        self.last_name = input("Enter your Last Name: ")
        self.bvn = input("Enter your BVN: ")
        self.email = input("Enter your Email: ")
        self.password = input("Enter your password: ")
        self.acct_num = 0
        self.acct_pin = 0
        
        if len(self.password) >= 10:
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            # Generate full name
            self.full_name = f"{self.first_name} {self.middle_name} {self.last_name}"
            print(f"Signup successful. Welcome, {self.middle_name}!")
            
            new_profile = {}  # Create a new dictionary for each profile
            
            for profile in self.data:
                print(profile, '\n')
                print(self.data, '\n')
                new_profile['Name'] = self.full_name
                new_profile['email'] = self.email
                new_profile["bvn"] = self.bvn
                new_profile["password"] = self.password
                
            print(new_profile, '\n')
            self.data.append(new_profile)  # Append the new profile dictionary to the data list
            print(self.data)
            self.IO.write(self.data)
        else:
            print("Enter a valid password")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    user_login = Login()
    user_login.validate_login(email, password)
            
    