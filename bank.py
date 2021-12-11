class Account:
    """This class simulates a bank account for a client"""
    def __init__(self, num_account, amount):
        self.__num_account = num_account
        self.__amount = amount
    def open_account(self):
        print("Welcome, you will not be deceive for choosing our bank branch")
    def deposit(self):
        print("Please, give your account number")
    def withdrawal(self):
        print("Please, fill the form with your account number, your ID and the amount to withdraw")
    