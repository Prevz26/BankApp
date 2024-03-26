from test.test_data import Test_data
class Utils():
    def __init__(self) -> None:
        self.test_data = Test_data()
        print(self.test_data)
        
    
    def headers(self) -> list[str]:
        return ["Name", "email", "password", "bvn", "acct_num", "acct_pin"]
    
    def default_val(self):
        return [{"Name": "", "email": "", "password": "", "bvn": "", "acct_num": "", "acct_pin": ""}]

if __name__ == "__main__":
    obj = Utils()