from cgi import print_directory


class User:
    def __init__(self, name, checking, savings):
        self.name = name
        self.account = {
            "checking": BankAccount(checking),
            "savings": BankAccount(savings)
        }
    def display_user_balance(self):
        print(f"User: {self.name} Checking Balance: {self.account['checking'].display_balance()}")
        print(f"User: {self.name} Checking Balance: {self.account['savings'].display_balance()}")
        return self

class BankAccount:
    bank_name = "Bank Of Caden"
    accounts = []
    def __init__(self, balance):
        self.id = len(BankAccount.accounts)
        self.int_rate = 0.002
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawal(self, amount):
        self.balance -= amount
        return self
    def display_balance(self):
        print(f"{self.id} ${self.balance}")
        return self
    def yeild_interest(self):
        self.balance += (self.balance*self.int_rate)
        return self
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_balance()

caden = User("Caden Wilcox", 100, 100)
mandy = User("Mandy Jefferson", 600, 1000)
# account_two = BankAccount(600)
caden.account['checking'].deposit(100).deposit(40).deposit(40).withdrawal(100).yeild_interest().display_balance()
# caden.account['checking'].display_balance()
mandy.account['checking'].deposit(100).deposit(40).withdrawal(200).withdrawal(100).withdrawal(60).yeild_interest().display_balance()
# BankAccount.print_all_accounts()
print(len(BankAccount.accounts))

# caden = User("Caden")
# billy = User("Billy")
# mandy = User("Mandy")
# caden.make_deposit(100).make_deposit(90).make_deposit(60).make_withdrawal(150)
# caden.display_user_balance()
# billy.make_deposit(60).make_deposit(100).make_withdrawal(40).make_withdrawal(80).display_user_balance()
# mandy.make_deposit(460).make_withdrawal(20).make_withdrawal(60).make_withdrawal(180).display_user_balance()
# caden.transfer_money(billy,10)
# caden.display_user_balance()
# billy.display_user_balance()

