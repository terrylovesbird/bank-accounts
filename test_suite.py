import unittest
from modules.account import Account

class BankTestSuite(unittest.TestCase):
    pass

class AccountTestSuite(unittest.TestCase):
    
    def test_create_check_initial_balance(self):
        initial_balance = 500
        a = Account(1, initial_balance)
        
        self.assertEqual(a.get_balance(), initial_balance)

    def test_withdraw_simple(self):
        initial_balance = 500
        a = Account(1, initial_balance)

        withdraw_amount = 100
        new_balance = a.withdraw(withdraw_amount)
        
        self.assertEqual(new_balance, initial_balance - withdraw_amount)

if __name__ == "__main__":
    unittest.main()