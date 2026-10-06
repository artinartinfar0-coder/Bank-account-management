class Bankaccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
    def _show_balance(self):
        print("Balance:",self.__balance)
    def get_info(self):
        return f"Owner:{self.owner}"
class Savigsaccount(Bankaccount):
    def __init__(self, owner, balance,interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    def get_info(self):
            return f"{super().get_info()}interest rate:{self.interest_rate}"
accounts = []
while True:
    i = input("choose: 1.Add Normal Account 2. Add Savings Account 3. Show All Info 4. Exit\n")
    if i == "1":
        o = input("owner:")
        b = float(input("balance:"))
        save = Bankaccount(o,b)
        accounts.append(save)
    if i == "2":
        o = input("owner:")
        b = float(input("balance:"))
        i2 = float(input("interest rate:"))
        save2 = Savigsaccount(o,b,i2)
        accounts.append(save2)
    if i == "3":
        for item in accounts:
            print(item.get_info())
            item._show_balance()
    if i == "4":
        break
