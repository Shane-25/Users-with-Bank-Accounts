class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self

    def display_user_balance(self):
        print(f'User: {self.name}, Balance: {self.account.balance}')
        return self

class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Interest Rate: {self.int_rate}, Balance: {self.balance}')
        return self

    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self

jonny = User("Jonny be Good", "jonny@codingdojo.com")
python = User("Python Monster", "python@codingdojo.com")
boaty = User("Boaty McBoatface", "boaty@codingdojo.com")

jonny.make_deposit(100).make_deposit(500).make_deposit(3000).make_withdrawal(200).display_user_balance()

python.make_deposit(100).make_deposit(800).make_withdrawal(100).make_withdrawal(50).display_user_balance()

boaty.make_deposit(2000).make_withdrawal(100).make_withdrawal(300).make_withdrawal(10).display_user_balance()

jonny.transfer_money(boaty,200).display_user_balance()
boaty.display_user_balance()
