  
from modules.savings_account import SavingsAccount
from modules.account import Account
from modules.bank import Bank
from modules.owner import Owner

# a = None
# try: # attempt to execute
a = Account(1, 500, "")
a.owner = Owner(123, 'Tianlin', '352w')
#a.set_owner('Cai')
print(a)
#     a.withdraw(1000)
# except ValueError as e: # handle any raised exceptions
#     print(e) 
# else: # will ONLY execute if the try block succeed
#     print("Your balance", a.check_balance())
# finally: # will ALWAYS execute
#     if a is not None:
#         a.deposit(200)


b = Bank()
accounts = b.load_accounts()
# if accounts is not None:
#     for a in accounts:
#         print(a)

# a_found = b.find_account_by_id(15152)
# print(a_found)

try:
    sa = SavingsAccount(1, 20, "")
    print(sa.withdraw(5))
    print(sa.withdraw(3))
except Exception as e:
    print(e)
