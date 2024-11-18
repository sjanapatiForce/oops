class Account():
    num_accounts = 0 # Class variable
    def __init__ (self, name, balance):
        self.name = name
        self.balance = balance 
        Account.num_accounts += 1

    def __repr__(self):
        return f'Account name: {self.name} Bal: {self.balance}'
    
    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
    
    
    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount

    def transfer(self, to_account, amount, transfer_date):
        if self.balance > amount:
            self.withdraw(amount)
            to_account.deposit(amount)

class CheckingAccount(Account):
    def __init__(self, account_name, initial_deposit):
        super().__init__(account_name, initial_deposit)
        self.checks = []

    def PostACheck(self, check_number, check_amount, post_date):
        self.checks.append((check_number, check_amount, post_date ))
        self.withdraw

class SavingsAccount(Account):
    def __init__(self, account_name, initial_deposit, interest_rate):
        super().__init__(account_name, initial_deposit)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance = self.balance * (1 + self.interest_rate/12)