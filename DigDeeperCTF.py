import random

class MiningCompany:
    def __init__(self):
        self.data = {
            "miners": {
                "Joe Miner": {
                    "age": 40,
                    "position": "Mining Engineer",
                    "salary": 90000,
                    "ssn": "123-45-6789"
                },
                "Johnn Smith": {
                    "age": 32,
                    "position": "Geologist",
                    "salary": 80000,
                    "ssn": "987-65-4321"
                }
            },
            "financial_data": {
                "revenue": 1000000,
                "expenses": 700000,
                "profit": 300000
            }
        }

    def get_flag(self):
        return "MineFlag{Th3_M1n1ng_Fl4g_1s_H3re!}"

class Hacker:
    def __init__(self):
        self.stolen_data = {}

    def hack(self, target):
        self.stolen_data = target.data
        print("Hacker: I've successfully breached the mining company's security!")
        print("Hacker: Let's see what valuable data I've stolen...")
        print("Hacker: ", self.stolen_data)

        flag = self.find_flag()
        if flag:
            print("Hacker: Hooray! I found the flag:", flag)
        else:
            print("Hacker: Darn! No flag found.")

    def find_flag(self):
        for key, value in self.stolen_data.items():
            if isinstance(value, dict):
                flag = self.find_flag_in_dict(value)
                if flag:
                    return flag
            elif isinstance(value, str) and "flag" in value.lower():
                return value
        return None

    def find_flag_in_dict(self, data):
        for key, value in data.items():
            if isinstance(value, dict):
                flag = self.find_flag_in_dict(value)
                if flag:
                    return flag
            elif isinstance(value, str) and "flag" in value.lower():
                return value
        return None

mining_company = MiningCompany()
hacker = Hacker()

hacker.hack(mining_company)
