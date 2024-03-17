class Utils():
    def headers(self) -> list[str]:
        return ["Name", "email", "password", "bvn", "acct_num", "acct_pin"]
    
    def default_val(self):
        return [{"Name": "", "email": "", "password": "", "bvn": "", "acct_num": "", "acct_pin": ""}]

    