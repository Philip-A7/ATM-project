# -------------------------------------------------------------------------------------------
# Imports
# -------------------------------------------------------------------------------------------
from card import *
from transaction import *
from datetime import datetime as dt
import time
import helper
import Acct

transact_obj =''
pin_status = ''
# -------------------------------------------------------------------------------------------
# Check length of card number
# -------------------------------------------------------------------------------------------
gtb = Card('P O KARIBO ALALIBO', '21/06/20', '', 432, saved_pin)


def take_credentials(number, pin):
    if len(str(number)) == 16:

        Transaction.card_no = number
        gtb.card_no = number
        # check_expiry()

        return number, pin

    else:
        print("Card number should be 16 digits long")
        return False
        # -------------------------------------------------------------------------------------------
        # Create new card instance.          NOTE!! Make this something the user creates at the start
        # -------------------------------------------------------------------------------------------


def welcome():
    print('Welcome to Barclays Bank PLC')
    print(f'User: {Acct.myaccess.acct_holder}')
    print(f'Card type: {card.Card.card_type(gtb)}')


# -------------------------------------------------------------------------------
# Check expiry of created card
# -------------------------------------------------------------------------------
def check_expiry():
    if gtb.is_card_expired() == 'Card valid':
        print('Login successful')

        # -------------------------------------------------------------------------------
        # Main menu loop. Used to return to main menu after each transaction
        # -------------------------------------------------------------------------------
        menu_start = True
        while menu_start is True:

            action = int(input(
                "What would you like to do? \n "
                "1) View balance \n "
                "2) Withdraw cash \n "
                "3) Change PIN \n "
                "4) Make Deposit \n "
                "5) Mobile Top-up \n"))

            # -------------------------------------------------------------------------------
            # Create transaction ID and timestamp variables
            # -------------------------------------------------------------------------------
            ids = new_id()
            timestamp = dt.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

            # -------------------------------------------------------------------------------
            # Main menu
            # -------------------------------------------------------------------------------
            if action == 1:
                trans1 = Transaction(ids, timestamp, None, None, 'View balance')
                global transact_obj
                transact_obj = trans1
                trans1.view_balance()
                helper.log(trans1)
                menu_start = trans1.return_to_menu()

            elif action == 2:
                trans1 = Transaction(ids, timestamp, None, None, 'Withdrawal')
                trans1.withdrawal()
                helper.log(trans1)
                menu_start = trans1.return_to_menu()

            elif action == 3:
                trans1 = Transaction(ids, timestamp, None, None, 'Change PIN')
                trans1.change_pin()
                helper.log(trans1)
                menu_start = trans1.return_to_menu()

            elif action == 4:
                trans1 = Transaction(ids, timestamp, None, None, 'Deposit')
                trans1.make_deposit()
                helper.log(trans1)
                menu_start = trans1.return_to_menu()

            elif action == 5:
                trans1 = Transaction(ids, timestamp, None, None, 'Mobile topup')
                trans1.mobile_topup()
                helper.log(trans1)
                menu_start = trans1.return_to_menu()


# -------------------------------------------------------------------------------
# Expired Card
# -------------------------------------------------------------------------------
    else:
        print('Card expired')

