import decimal

class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def check(self):
        print(self.name)
        print(self.balance)

    def validator(self, amount):
        try:
            return (decimal.Decimal(amount).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_DOWN))
        except decimal.InvalidOperation:
            print("{}!? U Sure?".format(amount))
            return 0


    def deposit(self, amount):
        self.balance += self.validator(amount)
        self.check()

    def withdraw(self, amount):
        if self.validator(amount) <= self.balance:
            self.balance -= self.validator(amount)
            self.check()
            
