class BankAccount:
    """This class simulates a bank account for a client"""
    def __init__(self, client_id, num_account, amount):
        self.__client_id = client_id 
        self.__num_account = num_account
        self.__amount = amount
        
    def open_account(self):
        """this method opens a new account for a client"""
        print("Welcome, you will not be deceive for choosing our bank branch")
        
    def deposit(self):
        """This method deposit the specified amount into the client's account"""
        print("Please, give your account number")
        
    def withdrawal(self):
        """This method withdraws the specified amount from client's account"""
        print("Please, fill the form with your account number, your ID and the amount to withdraw")
    