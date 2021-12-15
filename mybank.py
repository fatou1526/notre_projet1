"""class BankAccount:
    This class simulates a bank account for a client
    def __init__(self, client_id, num_account, amount, phone, adress, source_of_funds):
        self.phone = phone
        self.adress = adress
        self.source_of_funds = source_of_funds
        self.__client_id = client_id 
        self.__num_account = num_account
        self.__amount = amount
    @property
    def num_account(self):
        return self.__num_account
    @num_account.setter
    def num_account(self, num_account):
        assert isinstance(num_account, int), "Give me an integer, not a %r!" % type(num_account)   
    def open_account(self):
        this method opens a new account for a client
        print("Welcome, you will not be deceived for choosing our bank branch")
        print(f"My id is {self.client_id}")
        number = self.__num_account()
        return number
    """  
def deposit(id, num_account, amount, source_of_funds, phone, adress):
    """This method deposit the specified amount into the client's account"""
    tofill = {}
    print("Kindly, give the informations required in this form")
    tofill["Identity"].append(id) 
    tofill["Account number"].append(num_account)
    tofill["Amount"].append(amount)
    tofill["Source of funds"].append(source_of_funds)
    tofill["Phone"].append(phone)
    tofill["Adress"].append(adress)
    print(tofill)
def deposit_to_another_account(self, id, num_account, amount, source_of_funds, phone, adress, rec_name, rec_num_account): 
    """This method deposit the specified amount into someone else account giving his/her name and his/her account number"""
    tofill = {}
    print("Kindly, give the informations required in this form")
    tofill["Identity"].append(id) 
    tofill["Account number"].append(num_account)
    tofill["Receiver name"].append(rec_name)
    tofill["Receiver account"].append(rec_num_account)
    tofill["Amount"].append(amount)
    tofill["Source of funds"].append(source_of_funds)
    tofill["Phone"].append(phone)
    tofill["Adress"].append(adress)
    print(tofill)
    