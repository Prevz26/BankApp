from faker import Faker
import sys

class Test_data:
    def __init__(self):
        self.fake = Faker()
        self.fake.locale = "en_NG"

    def first_name(self):
        return self.fake.first_name()
    
    def last_name(self):
        return self.fake.last_name()

    def middle_name(self):
        return self.fake.last_name() 
    
    def email(self):
        return self.fake.email()

    def phone_number(self):
        return self.fake.phone_number()
    
    def generate_password(self,length):
        password = self.fake.password(length=length, special_chars=True, digits=True, upper_case=True, lower_case=True)
        return password
    
    def generate_num(self, length):
        return self.fake.random_number(digits=length)

if __name__ == "__main__":
    # print(sys.path)
    data = Test_data()
    print("Generated Name:", data.first_name())
    print("Generated Name:", data.last_name())
    print("Generated Name:", data.middle_name())
    print("Generated Email:", data.email())
    print("Generated Phone Number:", data.phone_number())
    print("Generated Password:", data.generate_password(12))
    print("Generated Number:", data.generate_num(4))


