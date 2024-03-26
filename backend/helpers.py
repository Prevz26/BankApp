import random
from fileIO import File_IO
from login import Login
import os
import test.test_data
class Bankapp():
    def __init__(self) -> None:
        self.file_io = File_IO()
        self.login = Login()
        self.test_data = test.Test_data()
        
    def create_account(self): 
        file_data = self.file_io.read()
        
        while True:
            acct_name = input("Enter your full name: ").title()
            name_found = False
            for profile in file_data:
                if acct_name == profile["Name"] and acct_name == self.login.user_data():
                    self.login.full_name
                    name_found = True
                    print(profile["Name"])
                    
                    #test data
                    acct_num = self.test_data.generate_num(5)
                    acct_pin = self.test_data.generate_num(5)
                    
                    # num_generation = list(range(10))
                    # acct_num = ''.join(map(str, random.sample(num_generation, k=10)))
                    # acct_pin = ''.join(map(str, random.sample(num_generation, k=4)))
                    print(f"{acct_name} has successfully created an account with account number: {acct_num} and PIN: {acct_pin}")
                    profile["acct_num"] = acct_num
                    profile["acct_pin"] = acct_pin
                    break 
                else:
                    print("Enter a valid name!")
                    continue 
            
            if name_found:
                self.file_io.write(file_data)
                break  
            else:
                print("Incorrect Name! Please try again or type 'exit' to quit.")
                if input().lower() == 'exit':
                    break
                
    def view_account_details():
        pass


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    test = Bankapp()
    test.create_account()
