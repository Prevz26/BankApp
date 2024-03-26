from test.test_data import Test_data
import os
import time
from typing import Union, Mapping, Sequence
from fileIO import File_IO
from utils import Utils

class Login:
    def __init__(self) -> None:
        self.IO: File_IO = File_IO()
        self.utils: Utils = Utils()
        self.data: Sequence[Mapping[str, str]] = self.utils.default_val()
        self.test_data:Test_data = Test_data()
        
        
    def user_data(self):
        # This is the test data, in production we'll use user input
        self._first_name:str = self.test_data.first_name()
        self._middle_name:str = self.test_data.middle_name()
        self._last_name:str = self.test_data.last_name()
        self._bvn:int = self.test_data.generate_num(4)
        self._email:str = self.test_data.email()
        self._password:int = self.test_data.generate_password(12)
        self._acct_num:int = 0
        self._acct_pin:int = 0
    
        #user data
        # self._first_name:str = input("Enter your first name: ")
        # self._middle_name:str = input("Enter your first name: ")
        # self._last_name:str = input("Enter your first name: ")
        # self._bvn:int = input("Enter your first name: ")
        # self._email:str = input("Enter your first name: ")
        # self._password:int = input("Enter your first name: ")
        # self._acct_num:int = 0
        # self._acct_pin:int = 0

    
        

    def validate_login(self, email, password) -> bool:
        self._email = email
        self._password = password
        """This method validates the login system"""
        login_counter = 0
        login_max = 3
        while login_counter < login_max:
                #read the csv file
                file_data = self.IO.read()
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
                            print("Incorrect Password. Please try again.")
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
        
        if len(self.password) >= 10:
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Generate full name
            self.full_name = f"{self.first_name} {self.middle_name} {self.last_name}"
            print(f"Signup successful. Welcome, {self.full_name}!")
            
            # Load existing user data from the CSV file
            existing_data = self.IO.read()
            
            new_profile = {}  # Create a new dictionary for the new user profile
            new_profile['Name'] = self.full_name
            new_profile['email'] = self.email
            new_profile["bvn"] = self.bvn
            new_profile["password"] = self.password
            
            # Append the new user profile to the existing list of profiles
            existing_data.append(new_profile)
            
            # Write the updated list of profiles back to the CSV file
            self.IO.write(existing_data)
        else:
            print("Enter a new password")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    data = Test_data()
    email = data.email()
    password = data.generate_password(12)
    
    user_login = Login()
    user_login.validate_login(email, password)
            
    