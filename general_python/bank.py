class Bank:
    def __init__(self, balance):
        self.balance = "$" + balance

    def check_balance(self):
        return f"Your balance is {self.balance}"

    def deposit(self):
        pass

    def withdraw(self):
        pass

    def pay_bill(self):
        pass

"1" = Bank
Bank.check_balance(100)