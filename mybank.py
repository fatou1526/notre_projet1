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