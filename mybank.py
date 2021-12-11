class BankAccount:
    """This class simulates a bank account for a client"""
    def __init__(self, client_id, num_account, amount):
        self.client_id = client_id 
        self.__num_account = num_account
        self.__amount = amount

    @property
    def num_account(self):
        return f"{self.__num_account}"

    @num_account.setter
    def num_account(self, num_account):
        assert isinstance(num_account, int), "Give me an integer, not a %r!" % type(num_account)  

    def open_account(self):
        """this method opens a new account for a client"""
        print("Welcome, you will not be deceived for choosing our bank branch")
        print(f"My id is {self.client_id}")
        number = self.num_account
        return number
        
    def deposit(self):
        """This method deposit the specified amount into the client's account"""
        print("Please, give your account number")
        
    def withdrawal(self):
        """This method withdraws the specified amount from client's account"""
        print("Please, fill the form with your account number, your ID and the amount to withdraw")
    