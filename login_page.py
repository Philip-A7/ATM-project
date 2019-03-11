# ===================
# Imports
# ===================
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import Main_P as MP
import yt_copy as mp
fl = 0
user = ''



class OOP:
    # Create instance
    def __init__(self):
        self.win = tk.Tk()

        # Add title
        self.win.title("Barclays")
        self.create_widgets2()

    # Functions
    def sign_in(self):
        card_length = MP.take_credentials(self.username_entered.get(), self.password_entered.get())
        self.counter()

        if card_length is False:
            self.message_box()
        else:

            if MP.pin_status is not True:
                print('FAIL')

            else:
                user = card_length[0]
                pass1 = card_length[1]
                self.win.destroy()
                MP.Transaction.card_no = user
                oop2 = mp.SeaofBTCapp()   # user, pass1
                oop2.mainloop()

        # Grid holders

    def create_widgets2(self):

        # Container frame for all other widgets
        self.mainframe = ttk.LabelFrame(self.win, text=' Main Frame ')
        self.mainframe.grid(column=0, row=0)
        but_img = tk.PhotoImage(file="buttons.png", width=50, height=50)
        logo_img = tk.PhotoImage(file="barclays logo1.png", width=270, height=110)
        icon_img = tk.PhotoImage(file="userhead.png", width=80, height=80)
        card_img = tk.PhotoImage(file="mastercard.png", width=90, height=90)
        card_img2 = tk.PhotoImage(file="visacard.png", width=90, height=90)

        user_label1 = ttk.Label(self.mainframe, width=20, text="          ")
        user_label1.grid(column=0, row=0)

        user_label2 = ttk.Label(self.mainframe, text="Blank space", image=card_img2)
        user_label2.grid(column=3, row=0)
        user_label2.image = card_img2

        user_label3 = ttk.Label(self.mainframe, text="Card pngs", image=card_img)
        user_label3.grid(column=4, row=0)
        user_label3.image = card_img

        user_label4 = ttk.Label(self.mainframe, text="Login Image", image=icon_img)
        user_label4.grid(column=1, row=2, rowspan=2)
        user_label4.image = icon_img

        user_label5 = tk.Label(self.mainframe, text="Barclays Logo", image=logo_img)
        user_label5.grid(column=1, row=1, columnspan=2)
        user_label5.image = logo_img

        user_label7 = ttk.Label(self.mainframe, text="Button")
        user_label7.grid(column=2, row=5)

        # Username and password --------------------------------------------------------------------
        user_label8 = ttk.Label(self.mainframe, text="Username")
        user_label8.grid(column=2, row=2)

        user_label9 = ttk.Label(self.mainframe, text="Password")
        user_label9.grid(column=2, row=3)

        # Adding a Textbox Entry widget --------------------------------------------------------------------
        self.username = tk.StringVar()
        self.username_entered = ttk.Entry(self.mainframe, width=12, textvariable=self.username, text="Card Number")
        self.username_entered.grid(column=2, row=2)

        self.password = tk.StringVar()
        self.password_entered = ttk.Entry(self.mainframe, width=12, textvariable=self.password, text="PIN", show='*')
        self.password_entered.grid(column=2, row=3)

        # Creating check button --------------------------------------------------------------------
        chVarUn = tk.IntVar()
        self.check2 = tk.Checkbutton(self.mainframe, text="Keep me logged in", variable=chVarUn)
        self.check2.deselect()
        self.check2.grid(column=2, row=4, sticky=tk.W, pady=10)

        # Create "sign-in" button --------------------------------------------------------------------
        self.action = tk.Button(self.mainframe, text='SIGN IN', command=self.sign_in)
        self.action.grid(column=2, row=5, sticky=tk.N, pady=20)
        # self.action.image = but_img

        self.username_entered.focus()

    def message_box(self):

        length = MP.take_credentials(self.username_entered.get(), self.password_entered.get())

        while length is False:
            if msg.askretrycancel('Error', 'Your card number must be 16 digits long') is False:
                self.win.destroy()
            else:
                self.username_entered.delete(0, 'end')
                return length
        else:
            pass

    def counter(self):
        global fl
        conf = MP.gtb.check_pin(self.password_entered.get())

        while conf is False:
            while fl < 2:
                if msg.askretrycancel('Error', f'Incorrect PIN, try again [{2 - fl} attempt(s) left]') is True:
                    self.password_entered.delete(0, 'end')
                    fl += 1
                    return fl
                else:
                    self.win.destroy()

            else:
                msg.showinfo('Warning', 'Card Deactivated. \n Please contact your bank')
                self.win.destroy()
                break
        else:
            MP.pin_status = True

# ======================
# Start GUI
# ======================


oop = OOP()
oop.win.mainloop()

