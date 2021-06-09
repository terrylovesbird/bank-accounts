# Create an Account class which should have the following functionality:
from .owner import Owner
import csv
import os

class Account():
    minimum_balance = 0
    withdraw_fee = 0

    # A new account should be created with an ID and an initial balance
    # A new account cannot be created with initial negative balance - this should raise an Exception (leverage those Googling skills!)
    def __init__(self, id, balance, open_date, owner = None):
        
        if id == 666:
            raise Exception("Bad account number")
        self.id = id

        if balance < self.minimum_balance:
            raise ValueError("Invalid balance! Please set a positive amount")
        self.balance = balance

        self.open_date = open_date
        self.owner = owner
        

    def __str__(self):
        owner_name = self.owner.name if self.owner is not None else "[no name]"
        return f"This account is owned by {owner_name} and the current balance is ${self.get_balance()}"


    def set_owner(self, owner):
        if self.owner is not None:
            raise Exception("Can not change an owner once one has been set")
        self.owner = owner

    # Should have a withdraw method that accepts a single parameter which represents the amount of money that will be withdrawn. This method should return the updated account balance.
    def withdraw(self, amount):
        new_balance = self.balance - amount - self.withdraw_fee 
        if new_balance < self.minimum_balance:
            raise ValueError("Can not withdraw amount specified.")

        self.balance = new_balance
        return self.balance

    # Should have a deposit method that accepts a single parameter which represents the amount of money that will be deposited. This method should return the updated account balance.
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    # Should be able to access the current balance of an account at any time.
    def get_balance(self):
        return self.balance


    
    # Update the Account class to be able to handle all of these fields from the CSV file used as input.
    @classmethod
    def all_accounts(cls):
        accounts = []
        with open("./support/accounts.csv") as accounts_file:
            data = csv.reader(accounts_file)
            for line in data:
                id = int(line[0])
                balance = int(line[1]) / 100
                open_date = line[2]

                account = cls(id, balance, open_date)
                accounts.append(account)

        return accounts

# a = Account(1212,1235667,1999-03-27 11:30:09 -0800, Tian)
# print(a)


    #     For example, manually choose the data from the first line of the CSV file and ensure you can create a new instance of your Account using that data
    # Add the following class methods to your existing Account class
    #     .all_accounts - returns a collection of Account instances, representing all of the Accounts described in the CSV. See below for the CSV file specifications
    #     .find(id) - returns an instance of Account where the value of the id field in the CSV matches the passed parameter