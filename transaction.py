# -------------------------------------------------------------------------------------------
# Imports
# -------------------------------------------------------------------------------------------
import card
from datetime import datetime as dt
import random
import helper
import time

new_amnt = ''

class Transaction(card.Card):
    card_no = ''

    def __init__(self, trans_id, start_time, stop_time, is_success, trans_type):

        self.trans_id = trans_id
        self.start_time = start_time
        self.stop_time = stop_time
        self.is_success = is_success
        self.trans_type = trans_type

    def withdrawal(self, choices, customs):

        balance = helper.retrieve_balance()
        new_bal = helper.new_with(choices, customs)[0]

        if type(new_bal) is str:
            return 'insufficient'

        elif new_bal < balance:

            self.is_success = "YES"
        else:
            self.is_success = "NO"
        self.stop_time = dt.now().time()
        return new_bal

    def view_balance(self):

        balance = helper.retrieve_balance()
        self.start_time = dt.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self.is_success = 'YES'
        self.stop_time = dt.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        return balance

    def compare_pins(self):

        stored_pin = helper.retrieve_pin2()
        entered_pin = input('Enter current PIN:')
        if entered_pin == stored_pin:
            return True
        else:
            return False

    def change_pin(self, old, new):

        stored_pin = helper.retrieve_pin2()
        if old != stored_pin:
            return False
        else:

            new_pin = new    # int(input('Enter new PIN:'))
            if new_pin == stored_pin:
                return 'same pin error'   # raise ValueError('New PIN cannot be the same as previous one')
            else:
                card.Card.PIN = new_pin
                helper.create_pin(new_pin)
                self.stop_time = dt.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                if new_pin == helper.create_pin(new_pin):
                    self.is_success = 'YES'
                else:
                    self.is_success = 'NO'
                print('PIN updated')

    def make_deposit(self, deposit):

        balance = helper.retrieve_balance()
        amount = deposit      # int(input('Enter amount to deposit:'))
        new_balances = (balance + amount)
        helper.update_balance(new_balances)
        print(f"Your new balance is: {new_balances}")

        if new_balances == balance + amount:
            self.is_success = 'YES'
        else:
            self.is_success = 'NO'

        # helper.receipt_or_nah()
        self.stop_time = dt.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    def mobile_topup(self, mob_no, top_amnt):

        balance = helper.retrieve_balance()

        length = True
        while length:

            mobile_str = str(mob_no)
            mobile_no = tuple(mobile_str)

            if len(mobile_no) != 11:
                print(mobile_no)
                break

            else:
                length = False
                ant = helper.line(mobile_str[0:4])

                amount = int(top_amnt)
                if amount > balance:
                    helper.insufficient_funds()
                    self.is_success = 'NO'

                else:
                    print('Top-up successful')
                    helper.new_balance(amount)
                    self.is_success = 'YES'
                    return ant
        self.stop_time = dt.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    def use_time(self):
        return self.start_time

    def return_to_menu(self):
        condition = True
        while condition:

            while True:
                response = str(input("Would you like to carry out another transaction? y or n \n"))
                if response in ('y', 'n'):
                    break

            if response.lower() == 'y':
                print("we will now take you back to the main menu")
                return True

            elif response.lower() == 'n':
                print("Please collect your card")
                return False


def new_id():
    last4 = str(Transaction.card_no)[-4:]
    time_element = dt.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')

    random_element = random.randint(10 ** 3, (10 ** 4) - 1)

    newid = f'{last4}-{time_element}-{random_element}'
    return newid
