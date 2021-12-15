# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 03:22:34 2021

@author: Mamadou Seybane KEBE
"""

class BankAccount:
    """This class simulates a bank account for a client"""
    def __init__(self, client_id, num_account, account_type, balance):
        self.__client_id = client_id 
        self.__num_account = num_account
        self.__balance = balance
        self.__account_type = account_type
        
    @property
    def num_account(self):
        return self.__num_account

    @num_account.setter
    def num_account(self, num_account):
        assert isinstance(num_account, int), "Give me an integer, not a %r!" % type(num_account)  
        self.__num_account = num_account
        
    @property
    def client_id(self):
        return self.__client_id
    
    @client_id.setter
    def client_id(self, client_id):
        self.__client_id = client_id
        
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, balance):
        self.__balance = balance
        
    @property
    def account_type(self):
        return self.__account_type 
    
    @account_type.setter
    def account_type(self, account_type):
        self.__account_type = account_type

    def get_current_balance(self):
        """This method returns the account's current balance"""
        print(f"The current balance is : {self.balance}")
        return self.balance
        
    def open_account(self, amount):
        """this method opens a new account for a client"""
        if amount > 0:
           self.balance = amount
           print(f"New account created with the number {self.num_account} and a balance of {self.balance}.")
        else: print("you cannot open an account with no money")
        
    def deposit(self, amount):
        """This method deposit the specified amount into the client's account"""
        self.balance += amount
        print(f"You deposited {amount}, New balance is {self.balance}")
        return self.balance
    
    def overdraft(self, amount, deadline=7):
        """This method allow the account to be overdrawn by 10% of the current balance"""
        if self.get_current_balance() < amount:
            amount = self.balance + (self.balance * .1)
            self.balance -= amount
            print(f"You have overdrawn your account by {amount}, current balance is {self.balance} which sould be paid in {deadline} days")
            return amount

    def withdrawal(self,  amount):
        """This method withdraws the specified amount from client's account"""
        if self.get_current_balance() >= amount:
            self.balance -= amount
            print(f"You withdrew : {amount}, your current balance is {self.balance}. {self.account_type}  Account closed.")
        else: 
            self.overdraft(amount)
            
    def close_account(self, num_account):
        if self.balance > 0:
            self.withdrawal(self.balance)
        elif self.balance == 0:
            print("There is nothing to withdraw. {self.account_type} Account closed")
        else:
            print(f"{self.account_type} Account cannot be closed you own {self.balance} to the bank")
            
    
    
    
b = BankAccount("1552KL", 159863, "Checking", 0)

b.open_account(500)
b.get_current_balance()
b.deposit(1000)
b.withdrawal(200)
b.withdrawal(2000)
b.close_account(159863)
    