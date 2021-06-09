from .account import Account
from .owner import Owner
import csv

# Create a Bank class which will contain your Account class and any future bank account logic.

class Bank():
    def __init__(self):
        self.accounts = []
        self.owners = []
        self.account_owners = []

    def load_all_data(self):
        self.load_accounts()
        self.load_owners()
        self.load_account_owners()

    def load_accounts(self):
        try:
            self.accounts = Account.all_accounts()
        except Exception as e:
            print(e)
            return None
        
        return self.accounts

    def load_owners(self):
        try:
            self.owners = Owner.all_owners()
        except Exception as e:
            print(e)
            return None
        
        return self.accounts

    def load_account_owners(self):
        accounts = []
        with open("./support/account_owners.csv") as accounts_file:
            data = csv.reader(accounts_file)
            for line in data:
                account_id = int(line[0])
                owner_id = int(line[1])

        return accounts


    def find_account_by_id(self, id):
        for a in self.accounts:
            if a.id == id:
                return a

        return None