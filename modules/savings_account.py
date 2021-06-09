  
from .account import Account

class SavingsAccount(Account):
    minimum_balance = 10
    withdraw_fee = 2
    
    def __init__(self, id, balance, open_date, owner=None):
        super().__init__(id, balance, open_date, owner=owner)
        
        if balance < self.minimum_balance:
            raise ValueError(f"Invalid balance! Savings accounts need at least ${self.minimum_balance}")
        
    # def withdraw(self, amount):
    #     return super().withdraw(amount)
