import random
from fileIO import File_IO
from login import Login
import os

class Bankapp():
    def __init__(self) -> None:
        self.file_io = File_IO()
        self.login = Login()
        
    def create_account(self): 
        file_data = self.file_io.read()
        print(file_data, '\n')
        
        while True:
            acct_name = input("Enter your full name: ").title()
            name_found = False
            for profile in file_data:
                if profile["Name"] == acct_name:
                    name_found = True
                    print(profile["Name"])
                    num_generation = list(range(10))
                    acct_num = ''.join(map(str, random.sample(num_generation, k=10)))
                    acct_pin = ''.join(map(str, random.sample(num_generation, k=4)))
                    print(f"{acct_name} has successfully created an account with account number: {acct_num} and PIN: {acct_pin}")
                    profile["acct_num"] = acct_num
                    profile["acct_pin"] = acct_pin
                    break  
            
            if name_found:
                print(file_data)
                self.file_io.write(file_data)
                break  
            else:
                print("Incorrect Name! Please try again or type 'exit' to quit.")
                if input().lower() == 'exit':
                    break


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    test = Bankapp()
    test.create_account()
