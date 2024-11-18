from accounts import Account
from datetime import date
from accounts import CheckingAccount
from accounts import SavingsAccount
new_account = Account('new 1', 100)
print(new_account)
print(Account.num_accounts)
new_account.deposit(20)
print(new_account)
new_account.withdraw(15)
print(new_account)

account2 = Account('Second account', 500)
account2.transfer(new_account, 75, date.today())
print(account2, new_account)

checking1 = CheckingAccount('new checking', 1001)
print(checking1)
checking1.PostACheck(101,200,'12-10-2019')
print(checking1)

account2 = SavingsAccount('Savings Account', 1000, 0.04)
print(account2)
print(Account.num_accounts)
account2.add_interest()
print(account2)