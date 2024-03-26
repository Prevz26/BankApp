from csv import DictReader, DictWriter
from utils import Utils
import os

class File_IO():
    def __init__(self) -> None:
        self.db = "bank.csv"
        utils = Utils()
        self.headers = utils.headers()
        self.default = utils.default_val()  
        
    def read(self):
        data = []
        if os.path.isfile("bank.csv"):
            with open(self.db, "r") as file:
                csv_reader = DictReader(file)
                for row in csv_reader:
                    data.append(row)
        return data
            
    def write(self, data = list()):
        with open(self.db, "w", newline='') as file:
            file_empty = os.path.getsize(self.db) == 0
            csv_writer = DictWriter(file, fieldnames=self.headers)
            if file_empty:
                csv_writer.writeheader()
            csv_writer.writerows(data)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    io = File_IO() 
    data = [{'Name': 'Delight Ojogu', 'email': 'preciousojogu@gmail.com', 'password': '1133', 'bvn': '234545678', 'acct_num': '3324', 'acct_pin': '3234'}]
    io.read()
    io.write(data)
            
