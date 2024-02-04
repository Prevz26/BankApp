from csv import DictWriter, DictReader
import os
import time

class Login:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
        

    def validate_login(self):
        """This method validates the login system"""
        login_counter = 0
        login_max = 3
        while login_counter < login_max:
            with open("bank.csv", "r") as file:
                csv_reader = DictReader(file)
                email_found = False  # Flag to track if email is found
                for row in csv_reader:
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
                            print("Incorrect password. Please try again.")
                            # print(login_counter)
                            login_counter += 1
                            print(login_counter)
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
        first_name = input("Enter your First Name: ")
        middle_name = input("Enter your Middle Name: ")
        last_name = input("Enter your Last Name: ")
        bvn = input("Enter your BVN: ")
        if len(self.password)>=10:
            print("valid password")
            # Generate full name
            full_name = f"{first_name} {middle_name} {last_name}"
            fieldnames = ["Name", "email", "password", "bvn"]
            # Store the details of created accounts in a CSV
            with open("bank.csv", "a", newline='') as file:
                csv_writer = DictWriter(file, fieldnames=fieldnames)
                csv_writer.writerow({"Name": full_name, "email": self.email, "password": self.password, "bvn": bvn})
                print(f"Signup successful. Welcome, {full_name}!")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Enter a valid password")

# Example usage
if __name__ == "__main__":
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    user_login = Login(email, password)
    if not user_login.validate_login():
        print("Would you like to sign up? (yes/no)")
        if input().lower() == 'yes':
            user_login.signup()
            
    