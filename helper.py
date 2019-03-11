# --------------------------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------------------------
import Acct

r = ''

# --------------------------------------------------------------------------------------------------
# Helper functions
# --------------------------------------------------------------------------------------------------


def update_balance(balance):

    bal_file = open("acct_bal", 'w+')
    bal_file.write(f'{balance}')
    bal_file.close()

    # bal_file2 = open("hold_balance", 'w+')
    # bal_file2.write(f'{balance}')
    # bal_file2.close()
    return balance


def retrieve_balance():
    balfile = open("acct_bal", 'r')
    balance = float(balfile.read())
    balfile.close()
    return balance


def create_pin(pin):

    pin_file = open("stored_pin", 'w+')
    pin_file.write(f'{pin}')
    pin_file.close()
    return pin


def retrieve_pin2():

    pinfile = open("stored_pin", 'r')
    saved_pin = int(pinfile.read())
    pinfile.close()
    return saved_pin


def log(trans1):
    g = Acct.sub_myaccess
    this = f'{trans1.trans_type}____{g.acct_type}____{trans1.trans_id}____{trans1.start_time}____{trans1.stop_time}____{trans1.is_success}'

    with open("transaction_log", "a") as logs:
        logs.write(f'{this}\n')
        logs.close()


def insufficient_funds():
    print("Insufficient funds")


def new_balance(withdrawal_amount):
    new_bal = retrieve_balance() - withdrawal_amount
    update_balance(new_bal)
    print(f'Your new balance is {new_bal}')

    bal_file2 = open("hold_balance", 'w+')
    bal_file2.write(f'{new_bal}')
    bal_file2.close()
    return new_bal


def receipt_or_nah():
    response1 = str(input("Print receipt? y or n \n"))
    if response1.lower() == 'y':
        print("Take receipt")
    elif response1.lower() == 'n':
        print("That's good for the environment")
    global end
    end = False
    return end


def new_with(response, custom):

    main_condition = True
    while main_condition:

        defaults = {1: 10, 2: 20, 3: 50, 4: 100, 5: 200}

        if response == "6":
            condition = True
            while condition:

                preset_amounts = int(custom)
                if preset_amounts % 10 != 0:
                    print('Multiples of 10 only')

                else:
                    condition = False
                    main_condition = False
                    continue

        else:
            try:
                preset_amounts = defaults[int(response)]
                main_condition = False
                continue
            except KeyError:
                print('Select from 1 to 6')

    if preset_amounts > retrieve_balance():
        insufficient_funds()
        return 'insufficient'

    else:
        return new_balance(preset_amounts), preset_amounts


def line(first4):
    glo = ['0705', '0805', '0807', '0811', '0815', '0905']
    nine_mobile = ['0809', '0818', '0817', '0909', '0908']
    mtn = ['0703', '0703', '0803', '0806', '0810', '0813', '0814', '0816', '0903', '0906']
    airtel = ['0701', '0708', '0802', '0808', '0812', '0902']
    visafone = ['0702', '0704']

    if first4 in glo:
        print('Glo')
        return 'Glo'
    elif first4 in nine_mobile:
        print('9Mobile')
        return '9Mobile'
    elif first4 in mtn:
        print('MTN')
        return 'MTN'
    elif first4 in airtel:
        print('Airtel')
        return 'Airtel'
    elif first4 in visafone:
        print('Visafone')
        return 'Visafone'
    else:
        raise UserWarning('Mobile provider not supported')

