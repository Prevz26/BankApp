import random

class Bank():
    def __init__(self, name: str, number: int, pin: int) -> None:
        self.acct_name = name
        self.acct_num = number
        self.acct_pin = pin
        
    def create_account(self):
        num_generation = list(range(10))
        self.acct_num = ''.join(map(str, random.sample(num_generation, k = 10)))
        self.acct_pin = ''.join(map(str, random.sample(num_generation, k=4)))
        if len(self.acct_pin) == 10 and self.acct_pin == 4:
            print(f"{self.acct_name} has successfully created an account with account number: {self.acct_num}")

def main():
    name = input("Enter your full name: ")
    acc1 = Bank(name, 0, 0)  
    acc1.create_account()

if __name__ == "__main__":
    main()
