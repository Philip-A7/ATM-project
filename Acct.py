

class Account:

    def __init__(self, acct_holder):
        self.acct_holder = acct_holder


class SubAccount(Account):

    def __init__(self, acct_number, acct_type):
        self.acct_number = acct_number
        self.acct_type = acct_type


myaccess = Account('Philip K. Alalibo')
sub_myaccess = SubAccount(10244012, 'Savings')


