# -------------------------------------------------------------------------------------------
# Imports
# -------------------------------------------------------------------------------------------
from datetime import datetime as dt
import helper


class Card:
    m = ''
    # saved_pin = helper.retrieve_pin2()

    def __init__(self, name, exp_date, card_no, CCV, PIN):

        self.name = name
        self.exp_date = exp_date
        self.card_no = card_no
        self.CCV = CCV
        self.PIN = PIN

    def check_pin(self, pin):

        if int(pin) == self.PIN:
            return True
        else:
            return False

    def is_card_expired(self):

        today = dt.now()
        expiry_date = dt.strptime(self.exp_date, "%d/%m/%y")

        if expiry_date > today:
            Card.m = 1
            return 'Card valid'
        else:
            Card.m = 0
            return 'Card expired'

    def retrieve_user_pin(self):

        entered_pin = int(input("Please enter 4 digit PIN:"))

        if type(entered_pin) != int:
            raise ValueError('Not a number')

        if len(str(entered_pin)) != 4:
            raise ValueError('Enter 4 digits')

        else:
            return entered_pin

    def card_type(self):
        tp = int(str(self.card_no)[0])

        type_dict = {3: 'Travelex', 4: 'Visa', 5: 'Mastercard', 6: 'Discover Card' }
        response = type_dict[tp]
        return response


# -------------------------------------------------------------------------------------------
#
# -------------------------------------------------------------------------------------------
saved_pin = helper.retrieve_pin2()










