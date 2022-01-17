class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"{self.name} Balance is: ${self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

caden = User("Caden")
billy = User("Billy")
mandy = User("Mandy")
caden.make_deposit(100).make_deposit(90).make_deposit(60).make_withdrawal(150)
caden.display_user_balance()
# caden.transfer_money(billy,10)
# caden.display_user_balance()
# billy.display_user_balance()
