# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 03:22:34 2021

@author: Mamadou Seybane KEBE
"""

class BankAccount:
    """This class simulates a bank account for a client"""
    def __init__(self, client_id, num_account, balance):
        self.__client_id = client_id 
        self.__num_account = num_account
        self.__balance = balance
        
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
    
    def overdraft(self, amount):
        """This method allow the account to be overdrawn by 10% of the current balance"""
        if self.get_current_balance() < amount:
            amount = self.balance + (self.balance * .1)
            self.balance -= amount
            print(f"You have overdrawn your account by {amount}, current balance is {self.balance}")
            return amount

    def withdrawal(self,  amount):
        """This method withdraws the specified amount from client's account"""
        if self.get_current_balance() >= amount:
            self.balance -= amount
            print(f"You withdrew : {amount}, your current balance is {self.balance}")
        else: 
            self.overdraft(amount)
           # print(f"You do not have sufficient fund to withdraw {amount}")
    
    
    
b = BankAccount("1552KL", 159863, 0)

b.open_account(500)
b.get_current_balance()
b.deposit(1000)
b.withdrawal(200)
b.withdrawal(2000)
    