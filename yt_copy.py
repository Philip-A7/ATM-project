import tkinter as tk
import Main_P as Ent
from tkinter import messagebox as msg
from datetime import datetime as dt
import time


LARGE_FONT = ("Verdana", 12)
status = False
trans1 = Ent.Transaction(None, None, None, None, None)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.app_data = {"newbal": tk.StringVar(), "amount": tk.StringVar()}
        self.title("BARCLAYS")
        self.geometry('1000x480')
        self.pack_propagate(0)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, MainMenu, ViewBalance1, Withdrawal1, Withdrawal2, Withdrawal3, Withdrawal4, Deposit1, Deposit2,
                  Deposit3, Mobile1, Mobile2, ChangePin1, CollectCard, ThanksForBanking):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_name):
        for page in self.frames.values():
            if str(page.__class__.__name__) == page_name:
                return page
        return None


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        logo_img = tk.PhotoImage(file="background.png", width=3350, height=1809)
        bl = tk.Label(self, image=logo_img, compound=tk.TOP)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        bl.image = logo_img

        self.make_widget(controller)

    def make_widget(self, controller):

        customer = Ent.Acct.myaccess.acct_holder
        label = tk.Label(self, text=f"Welcome {customer}", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="START",
                           command=lambda: controller.show_frame(MainMenu))
        button.pack()

        button2 = tk.Button(self, text="EXIT",
                            command=lambda: controller.show_frame(ThanksForBanking))
        button2.pack()


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.mainframe = tk.LabelFrame(self)
        self.mainframe.grid(column=0, row=0)

        logo_img = tk.PhotoImage(file="background.png", width=3350, height=1809)
        bl = tk.Label(self.mainframe, image=logo_img, compound=tk.TOP)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        bl.image = logo_img

        self.make_widgets(controller)
        # -------------------------------------------------------------------------------------
        # Grid holders
        # -------------------------------------------------------------------------------------
    def make_widgets(self, controller):
        logo2_img = tk.PhotoImage(file="barc.png", width=200, height=63)


        user_label = tk.Label(self.mainframe, text="Barclays logo", image=logo2_img)
        user_label.grid(column=0, row=0)
        user_label.image = logo2_img

        user_label = tk.Label(self.mainframe, text="Middle big bits")
        user_label.grid(column=2, row=0, columnspan=1)

        user_label = tk.Label(self.mainframe, text="last column", width=24)
        user_label.grid(column=4, row=0)

        user_label = tk.Label(self.mainframe, text="             ")
        user_label.grid(column=2, row=1)

        user_label = tk.Label(self.mainframe, text="Button")
        user_label.grid(column=2, row=2, columnspan=2, rowspan=2)

        user_label = tk.Button(self.mainframe, text="      EXIT       ", command=lambda: self.winfo_toplevel().quit())
        user_label.grid(column=2, row=5, pady=40)

        # -------------------------------------------------------------------------------------
        # Adding a Textbox Entry widget
        # -------------------------------------------------------------------------------------
        scrol_w = 500
        scrol_h = 280
        self.scr = tk.Frame(self.mainframe, width=scrol_w, height=scrol_h, bd=10, bg='gray')
        self.scr.grid(column=2, row=2, columnspan=1, rowspan=3, padx=8, pady=8, sticky='n')
        self.scr.grid_propagate(False)


        ids = Ent.new_id()
        timestamp = dt.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

        def transaction_name(name):
            dictionary = {ViewBalance1:'View Balance', Withdrawal1: 'Withdrawal', Deposit1: 'Deposit',
                          ChangePin1: 'Change PIN', Mobile1: 'Mobile Top-up', CollectCard: 'Collect Card'}
            transaction_ = dictionary[name]
            return transaction_

        def create_trans_object(new_page):
            name = transaction_name(new_page)
            global trans1

            trans1.trans_id = ids
            trans1.start_time = timestamp
            trans1.trans_type = name

            controller.show_frame(new_page)

        but_img = tk.PhotoImage(file="buttons.png", width=30, height=30)
        but_img2 = tk.PhotoImage(file="buttons2.png", width=30, height=30)
        # image=but_img, compound=tk.TOP
        # self.action1.image = but_img
        but_img2 = tk.PhotoImage(file="buttons2.png", width=30, height=30)
        # image=but_img2, compound=tk.TOP
        # self.action1.image = but_img2


        # Create "action" button
        self.action1 = tk.Button(self.mainframe, command=lambda: create_trans_object(ViewBalance1),
                                 image=but_img, compound=tk.TOP)
        self.action1.grid(column=1, row=2, pady=2, sticky='s')
        self.action1.image = but_img

        self.action2 = tk.Button(self.mainframe, command=lambda: create_trans_object(Withdrawal1),
                                 image=but_img, compound=tk.TOP)
        self.action2.grid(column=1, row=3, pady=2)
        self.action2.image = but_img

        self.action3 = tk.Button(self.mainframe, command=lambda: create_trans_object(Deposit1),
                                 image=but_img, compound=tk.TOP)
        self.action3.grid(column=1, row=4, pady=2, sticky='n')
        self.action3.image = but_img

        self.action4 = tk.Button(self.mainframe, command=lambda: create_trans_object(ChangePin1),
                                 image=but_img2, compound=tk.TOP)
        self.action4.grid(column=3, row=2, pady=2, sticky='s')
        self.action4.image = but_img2

        self.action5 = tk.Button(self.mainframe, command=lambda: create_trans_object(Mobile1),
                                 image=but_img2, compound=tk.TOP)
        self.action5.grid(column=3, row=3, pady=2)
        self.action5.image = but_img2

        self.action6 = tk.Button(self.mainframe, command=lambda: create_trans_object(CollectCard),
                                 image=but_img2, compound=tk.TOP)
        self.action6.grid(column=3, row=4, pady=2, sticky='n')
        self.action6.image = but_img2

        arl2 = tk.Text(self.scr, height=16, width=70, bg='white')
        arl2.pack(expand=True, fill='both')
        arl2.insert('1.0', '                              MAIN MENU                     \n\n\n'
                           'View Balance                                               Change PIN\n\n\n\n'
                           'Withdrawal                                               Mobile Topup\n\n\n\n'
                           'Deposit                                                   Return Card')
        arl2.configure(state='disabled')


class ViewBalance1(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.mainframe = tk.LabelFrame(self)
        self.mainframe.grid(column=0, row=0)

        logo_img = tk.PhotoImage(file="background.png", width=3350, height=1809)
        bl = tk.Label(self.mainframe, image=logo_img, compound=tk.TOP)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        bl.image = logo_img

        self.make_widgets(controller)

        # -------------------------------------------------------------------------------------
        # Grid holders
        # -------------------------------------------------------------------------------------
    def make_widgets(self, controller):

        logo2_img = tk.PhotoImage(file="barc.png", width=200, height=63)

        user_label = tk.Label(self.mainframe, text="Barclays logo", image=logo2_img)
        user_label.grid(column=0, row=0)
        user_label.image = logo2_img

        user_label = tk.Label(self.mainframe, text="last column", width=24)
        user_label.grid(column=4, row=0)

        user_label = tk.Label(self.mainframe, text="Middle big bits")
        user_label.grid(column=2, row=0, columnspan=1)


        user_label = tk.Label(self.mainframe, text="last column")
        user_label.grid(column=4, row=0)

        user_label = tk.Label(self.mainframe, text="             ")
        user_label.grid(column=2, row=1)

        user_label = tk.Label(self.mainframe, text="Button")
        user_label.grid(column=2, row=2, columnspan=2, rowspan=2)

        user_label = tk.Button(self.mainframe, text="      EXIT       ", command=lambda: self.winfo_toplevel().quit())
        user_label.grid(column=2, row=5, pady=40)

        # -------------------------------------------------------------------------------------
        # Adding a Textbox Entry widget
        # -------------------------------------------------------------------------------------
        scrol_w = 500
        scrol_h = 280
        self.scr = tk.Frame(self.mainframe, width=scrol_w, height=scrol_h, bd=10, bg='gray')
        self.scr.grid(column=2, row=2, columnspan=1, rowspan=3, padx=8, pady=8, sticky='n')
        self.scr.grid_propagate(False)

        but_img = tk.PhotoImage(file="buttons.png", width=30, height=30)
        but_img2 = tk.PhotoImage(file="buttons2.png", width=30, height=30)
        # image=but_img2, compound=tk.TOP
        # self.action1.image = but_img2

        # Create "action" button
        self.action1 = tk.Button(self.mainframe, command=lambda: controller.show_frame(StartPage),
                                 image=but_img, compound=tk.TOP)
        self.action1.grid(column=1, row=2, pady=2, sticky='s')
        self.action1.image = but_img

        self.action2 = tk.Button(self.mainframe, command=lambda: controller.show_frame(ViewBalance1),
                                 image=but_img, compound=tk.TOP)
        self.action2.grid(column=1, row=3, pady=2)
        self.action2.image = but_img

        self.action3 = tk.Button(self.mainframe, command=lambda: end_transaction(MainMenu),
                                 image=but_img, compound=tk.TOP)
        self.action3.grid(column=1, row=4, pady=2, sticky='n')
        self.action3.image = but_img

        self.action4 = tk.Button(self.mainframe, command=lambda: controller.show_frame(ViewBalance1),
                                 image=but_img2, compound=tk.TOP)
        self.action4.grid(column=3, row=2, pady=2, sticky='s')
        self.action4.image = but_img2

        self.action5 = tk.Button(self.mainframe, command=lambda: controller.show_frame(ViewBalance1),
                                 image=but_img2, compound=tk.TOP)
        self.action5.grid(column=3, row=3, pady=2)
        self.action5.image = but_img2

        self.action6 = tk.Button(self.mainframe, command=lambda: end_transaction(CollectCard),
                                 image=but_img2, compound=tk.TOP)
        self.action6.grid(column=3, row=4, pady=2, sticky='n')
        self.action6.image = but_img2




        def end_transaction(new_page):
            timestamp = dt.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            global trans1
            trans1.stop_time = timestamp
            trans1.is_success = 'YES'
            Ent.helper.log(trans1)
            controller.show_frame(new_page)

        balance = trans1.view_balance()

        arl2 = tk.Text(self.scr, height=16, width=70, bg='white')
        arl2.pack(expand=True, fill='both')
        arl2.insert('1.0', '                              VIEW BALANCE                     \n\n\n'        
                           '            Your balance is:                                    \n'
                          f'                                            {balance}                \n\n\n\n'
                           '            Would you like to carry out another transaction           \n\n\n\n'
                           ' YES                                                             NO')
        arl2.configure(state='disabled')


class Withdrawal1(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.mainframe = tk.LabelFrame(self)
        self.mainframe.grid(column=0, row=0)

        logo_img = tk.PhotoImage(file="background.png", width=3350, height=1809)
        bl = tk.Label(self.mainframe, image=logo_img, compound=tk.TOP)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        bl.image = logo_img

        # -------------------------------------------------------------------------------------
        # Grid holders
        # -------------------------------------------------------------------------------------
        logo2_img = tk.PhotoImage(file="barc.png", width=200, height=63)

        user_label = tk.Label(self.mainframe, text="Barclays logo", image=logo2_img)
        user_label.grid(column=0, row=0)
        user_label.image = logo2_img

        user_label = tk.Label(self.mainframe, text="last column", width=22)
        user_label.grid(column=4, row=0)

        user_label = tk.Label(self.mainframe, text="Middle big bits")
        user_label.grid(column=2, row=0, columnspan=1)

        user_label = tk.Label(self.mainframe, text="last column")
        user_label.grid(column=4, row=0)

        user_label = tk.Label(self.mainframe, text="             ")
        user_label.grid(column=2, row=1)

        user_label = tk.Label(self.mainframe, text="Button")
        user_label.grid(column=2, row=2, columnspan=2, rowspan=2)

        user_label = tk.Button(self.mainframe, text="      EXIT       ", command=lambda: self.winfo_toplevel().quit())
        user_label.grid(column=2, row=5, pady=40)

        # -------------------------------------------------------------------------------------
        # Adding a Textbox Entry widget
        # -------------------------------------------------------------------------------------
        scrol_w = 500
        scrol_h = 280
        self.scr = tk.Frame(self.mainframe, width=scrol_w, height=scrol_h, bd=10, bg='gray')
        self.scr.grid(column=2, row=2, columnspan=1, rowspan=3, padx=8, pady=8, sticky='n')
        self.scr.grid_propagate(False)

        def set_amount(amnt):
            presets = {1: 10, 2: 20, 3: 50, 4: 100, 5: 200}
            amount = presets[amnt]
            return amount

        def withdraw_and_change(choice, framed):
            a = Ent.Transaction.withdrawal(trans1, choice, None)
            set_amount(choice)
            end_transaction(framed)

            # controller.show_frame(framed)
            global status
            status = True
            print(a)

        def end_transaction(new_page):
            timestamp = dt.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            global trans1
            trans1.stop_time = timestamp
            trans1.is_success = 'YES'
            Ent.helper.log(trans1)
            controller.show_frame(new_page)

        but_img = tk.PhotoImage(file="buttons.png", width=30, height=30)
        but_img2 = tk.PhotoImage(file="buttons2.png", width=30, height=30)
        # image=but_img2, compound=tk.TOP
        # self.action1.image = but_img2

        # Create "action" button
        self.action1 = tk.Button(self.mainframe, command=lambda: withdraw_and_change(1, Withdrawal3),
                                 image=but_img, compound=tk.TOP)
        self.action1.grid(column=1, row=2, pady=2, sticky='s')
        self.action1.image = but_img

        self.action2 = tk.Button(self.mainframe, command=lambda: withdraw_and_change(3, Withdrawal3),
                                 image=but_img, compound=tk.TOP)
        self.action2.grid(column=1, row=3, pady=2)
        self.action2.image = but_img

        self.action3 = tk.Button(self.mainframe, command=lambda: withdraw_and_change(5, Withdrawal3),
                                 image=but_img, compound=tk.TOP)
        self.action3.grid(column=1, row=4, pady=2, sticky='n')
        self.action3.image = but_img

        self.action4 = tk.Button(self.mainframe, command=lambda: withdraw_and_change(2, Withdrawal3),
                                 image=but_img2, compound=tk.TOP)
        self.action4.grid(column=3, row=2, pady=2, sticky='s')
        self.action4.image = but_img2

        self.action5 = tk.Button(self.mainframe, command=lambda: withdraw_and_change(4, Withdrawal3),
                                 image=but_img2, compound=tk.TOP)
        self.action5.grid(column=3, row=3, pady=2)
        self.action5.image = but_img2

        self.action6 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Withdrawal2),
                                 image=but_img2, compound=tk.TOP)
        self.action6.grid(column=3, row=4, pady=2, sticky='n')
        self.action6.image = but_img2

        arl2 = tk.Text(self.scr, height=16, width=70, bg='white')
        arl2.pack(expand=True, fill='both')
        arl2.insert('1.0', '                              WITHDRAWAL 1                         \n'
                           'Select an amount                                                 \n\n\n'
                           '£10                                                               £20\n\n\n\n'
                           '£50                                                              £100\n\n\n\n'
                           '£200                                                           Custom')
        arl2.configure(state='disabled')


class Withdrawal2(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.mainframe = tk.LabelFrame(self)
        self.mainframe.grid(column=0, row=0)

        logo_img = tk.PhotoImage(file="background.png", width=3350, height=1809)
        bl = tk.Label(self.mainframe, image=logo_img, compound=tk.TOP)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        bl.image = logo_img


        but_img = tk.PhotoImage(file="buttons.png", width=50, height=50)
        # -------------------------------------------------------------------------------------
        # Grid holders
        # -------------------------------------------------------------------------------------
        logo2_img = tk.PhotoImage(file="barc.png", width=200, height=63)

        user_label = tk.Label(self.mainframe, text="Barclays logo", image=logo2_img)
        user_label.grid(column=0, row=0)
        user_label.image = logo2_img

        user_label = tk.Label(self.mainframe, text="Middle big bits")
        user_label.grid(column=2, row=0, columnspan=1)

        user_label = tk.Label(self.mainframe, text="last column", width=22)
        user_label.grid(column=4, row=0)

        user_label = tk.Label(self.mainframe, text="             ")
        user_label.grid(column=2, row=1)

        user_label = tk.Label(self.mainframe, text="Button")
        user_label.grid(column=2, row=2, columnspan=2, rowspan=2)

        user_label = tk.Button(self.mainframe, text="      EXIT       ", command=lambda: self.winfo_toplevel().quit())
        user_label.grid(column=2, row=5, pady=40)

        # -------------------------------------------------------------------------------------
        # Adding a Textbox Entry widget
        # -------------------------------------------------------------------------------------
        scrol_w = 500
        scrol_h = 280
        self.scr = tk.Frame(self.mainframe, width=scrol_w, height=scrol_h, bd=10, bg='gray')
        self.scr.grid(column=2, row=2, columnspan=1, rowspan=3, padx=8, pady=8, sticky='n')
        self.scr.grid_propagate(False)

        def withdraw_and_change(choice, framed):
            a = Ent.Transaction.withdrawal(trans1, str(choice), float(self.withdrawal_entered.get()))
            if a == 'insufficient':
                self.insufficient_funds_message()
                end_transaction(Withdrawal2, 0)
            else:
                end_transaction(framed, 1)
                global status
                status = True

        def end_transaction(new_page, sufficiency):
            timestamp = dt.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            global trans1
            trans1.stop_time = timestamp
            if sufficiency == 1:
                trans1.is_success = 'YES'
            else:
                trans1.is_success = 'NO'
            Ent.helper.log(trans1)
            controller.show_frame(new_page)

        trans1 = Ent.Transaction(None, None, None, None, 'Withdrawal')

        but_img = tk.PhotoImage(file="buttons.png", width=30, height=30)
        but_img2 = tk.PhotoImage(file="buttons2.png", width=30, height=30)
        # image=but_img2, compound=tk.TOP
        # self.action1.image = but_img2



        # Create "action" button
        self.action1 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Withdrawal2),
                                 image=but_img, compound=tk.TOP)
        self.action1.grid(column=1, row=2, pady=2, sticky='s')
        self.action1.image = but_img

        self.action2 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Withdrawal2),
                                 image=but_img, compound=tk.TOP)
        self.action2.grid(column=1, row=3, pady=2)
        self.action2.image = but_img

        self.action3 = tk.Button(self.mainframe, command=lambda: withdraw_and_change(6, Withdrawal3),
                                 image=but_img, compound=tk.TOP)
        self.action3.grid(column=1, row=4, pady=2, sticky='n')
        self.action3.image = but_img

        self.action4 = tk.Button(self.mainframe, text="Button 4", command=lambda: controller.show_frame(Withdrawal2),
                                 image=but_img2, compound=tk.TOP)
        self.action4.grid(column=3, row=2, pady=2, sticky='s')
        self.action4.image = but_img2

        self.action5 = tk.Button(self.mainframe, text="Button 5", command=lambda: controller.show_frame(Withdrawal2),
                                 image=but_img2, compound=tk.TOP)
        self.action5.grid(column=3, row=3, pady=2)
        self.action5.image = but_img2

        self.action6 = tk.Button(self.mainframe, text="Button 6", command=lambda: controller.show_frame(CollectCard),
                                 image=but_img2, compound=tk.TOP)
        self.action6.grid(column=3, row=4, pady=2, sticky='n')
        self.action6.image = but_img2

        arl2 = tk.Text(self.scr, height=16, width=70, bg='white')
        arl2.pack(expand=True, fill='both')
        arl2.insert('1.0', '                              WITHDRAWAL 2                                 \n'
                           'Enter an amount in multiples of £10                                    \n\n\n\n'
                           '                               £                                       \n\n\n\n'
                           'CONFIRM                                                         CANCEL')
        arl2.configure(state='disabled')

        self.withdrawal_entered = tk.Entry(arl2, width=8, textvariable=controller.app_data["amount"])
        self.withdrawal_entered.place(x=200, y=95)
        self.withdrawal_entered.focus()

    def insufficient_funds_message(self):

        msg.showwarning('Warning', 'You do not have enough funds to make this withdrawal')
        self.withdrawal_entered.delete(0, 'end')


def get_bal():
    bal = open("hold_balance", 'r')
    var1 = bal.read()
    bal.close()
    return var1


class Withdrawal3(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.mainframe = tk.LabelFrame(self)
        self.mainframe.grid(column=0, row=0)

        logo_img = tk.PhotoImage(file="background.png", width=3350, height=1809)
        bl = tk.Label(self.mainframe, image=logo_img, compound=tk.TOP)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        bl.image = logo_img

        # -------------------------------------------------------------------------------------
        # Grid holders
        # -------------------------------------------------------------------------------------
        logo2_img = tk.PhotoImage(file="barc.png", width=200, height=63)

        user_label = tk.Label(self.mainframe, text="Barclays logo", image=logo2_img)
        user_label.grid(column=0, row=0)
        user_label.image = logo2_img

        user_label = tk.Label(self.mainframe, text="Middle big bits")
        user_label.grid(column=2, row=0, columnspan=1)

        user_label = tk.Label(self.mainframe, text="last column", width=22)
        user_label.grid(column=4, row=0)

        user_label = tk.Label(self.mainframe, text="             ")
        user_label.grid(column=2, row=1)

        user_label = tk.Label(self.mainframe, text="Button")
        user_label.grid(column=2, row=2, columnspan=2, rowspan=2)

        user_label = tk.Button(self.mainframe, text="      EXIT       ", command=lambda: self.winfo_toplevel().quit())
        user_label.grid(column=2, row=5, pady=40)

        # -------------------------------------------------------------------------------------
        # Adding a Textbox Entry widget
        # -------------------------------------------------------------------------------------
        scrol_w = 500
        scrol_h = 280
        self.scr = tk.Frame(self.mainframe, width=scrol_w, height=scrol_h, bd=10, bg='gray')
        self.scr.grid(column=2, row=2, columnspan=1, rowspan=3, padx=8, pady=8, sticky='n')
        self.scr.grid_propagate(False)

        but_img = tk.PhotoImage(file="buttons.png", width=30, height=30)
        # image=but_img, compound=tk.TOP
        # self.action1.image = but_img
        but_img2 = tk.PhotoImage(file="buttons2.png", width=30, height=30)
        # image=but_img2, compound=tk.TOP
        # self.action1.image = but_img2

        # Create "action" button
        self.action1 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Withdrawal3),
                                 image=but_img, compound=tk.TOP)
        self.action1.grid(column=1, row=2, pady=2, sticky='s')
        self.action1.image = but_img

        self.action2 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Withdrawal3),
                                 image=but_img, compound=tk.TOP)
        self.action2.grid(column=1, row=3, pady=2)
        self.action2.image = but_img

        self.action3 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Withdrawal3),
                                 image=but_img, compound=tk.TOP)
        self.action3.grid(column=1, row=4, pady=2, sticky='n')
        self.action3.image = but_img

        self.action4 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Withdrawal3),
                                 image=but_img2, compound=tk.TOP)
        self.action4.grid(column=3, row=2, pady=2, sticky='s')
        self.action4.image = but_img2

        self.action5 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Withdrawal3),
                                 image=but_img2, compound=tk.TOP)
        self.action5.grid(column=3, row=3, pady=2)
        self.action5.image = but_img2

        self.action6 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Withdrawal3),
                                 image=but_img2, compound=tk.TOP)
        self.action6.grid(column=3, row=4, pady=2, sticky='n')
        self.action6.image = but_img2

        arl2 = tk.Text(self.scr, height=16, width=70, bg='white')
        arl2.pack(expand=True, fill='both')
        arl2.insert('1.0', '                              WITHDRAWAL 3                     \n\n\n'
                           '                                                                        \n'
                           '         Please collect your card, your cash will follow shortly           \n\n\n\n'
                           '                  Thanks for banking with Barclays                         \n\n\n\n'
                           '                                                  ')
        arl2.configure(state='disabled')


class Withdrawal4(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.mainframe = tk.LabelFrame(self)
        self.mainframe.grid(column=0, row=0)

        logo_img = tk.PhotoImage(file="background.png", width=3350, height=1809)
        bl = tk.Label(self.mainframe, image=logo_img, compound=tk.TOP)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        bl.image = logo_img

        but_img = tk.PhotoImage(file="buttons.png", width=50, height=50)
        # -------------------------------------------------------------------------------------
        # Grid holders
        # -------------------------------------------------------------------------------------
        logo2_img = tk.PhotoImage(file="barc.png", width=200, height=63)

        user_label = tk.Label(self.mainframe, text="Barclays logo", image=logo2_img)
        user_label.grid(column=0, row=0)
        user_label.image = logo2_img

        user_label = tk.Label(self.mainframe, text="Middle big bits")
        user_label.grid(column=2, row=0, columnspan=1)

        user_label = tk.Label(self.mainframe, text="last column", width=22)
        user_label.grid(column=4, row=0)

        user_label = tk.Label(self.mainframe, text="             ")
        user_label.grid(column=2, row=1)

        user_label = tk.Label(self.mainframe, text="Button")
        user_label.grid(column=2, row=2, columnspan=2, rowspan=2)

        user_label = tk.Button(self.mainframe, text="      EXIT       ", command=lambda: self.winfo_toplevel().quit())
        user_label.grid(column=2, row=5, pady=40)

        # -------------------------------------------------------------------------------------
        # Adding a Textbox Entry widget
        # -------------------------------------------------------------------------------------
        scrol_w = 500
        scrol_h = 280
        self.scr = tk.Frame(self.mainframe, width=scrol_w, height=scrol_h, bd=10, bg='gray')
        self.scr.grid(column=2, row=2, columnspan=1, rowspan=3, padx=8, pady=8, sticky='n')
        self.scr.grid_propagate(False)

        # Create "action" button
        self.action1 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Withdrawal4))
        self.action1.grid(column=1, row=2, pady=2, sticky='s')

        self.action2 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Withdrawal4))
        self.action2.grid(column=1, row=3, pady=2)

        self.action3 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Withdrawal1))
        self.action3.grid(column=1, row=4, pady=2, sticky='n')

        self.action4 = tk.Button(self.mainframe, text="Button 4", command=lambda: controller.show_frame(Withdrawal4))
        self.action4.grid(column=3, row=2, pady=2, sticky='s')

        self.action5 = tk.Button(self.mainframe, text="Button 5", command=lambda: controller.show_frame(Withdrawal4))
        self.action5.grid(column=3, row=3, pady=2)

        self.action6 = tk.Button(self.mainframe, text="Button 6", command=lambda: controller.show_frame(CollectCard))
        self.action6.grid(column=3, row=4, pady=2, sticky='n')

        arl2 = tk.Text(self.scr, height=16, width=70, bg='white')
        arl2.pack(expand=True, fill='both')
        arl2.insert('1.0', '                              WITHDRAWAL 4                     \n\n\n'
                           '                                                              \n\n\n\n'
                           '                            Insufficient funds                      \n\n\n\n'
                           'BACK                                                               EXIT')
        arl2.configure(state='disabled')


class Deposit1(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        self.mainframe = tk.LabelFrame(self)
        self.mainframe.grid(column=0, row=0)

        logo_img = tk.PhotoImage(file="background.png", width=3350, height=1809)
        bl = tk.Label(self.mainframe, image=logo_img, compound=tk.TOP)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        bl.image = logo_img

        but_img = tk.PhotoImage(file="buttons.png", width=50, height=50)
        # -------------------------------------------------------------------------------------
        # Grid holders
        # -------------------------------------------------------------------------------------
        logo2_img = tk.PhotoImage(file="barc.png", width=200, height=63)

        user_label = tk.Label(self.mainframe, text="Barclays logo", image=logo2_img)
        user_label.grid(column=0, row=0)
        user_label.image = logo2_img

        user_label = tk.Label(self.mainframe, text="Middle big bits")
        user_label.grid(column=2, row=0, columnspan=1)

        user_label = tk.Label(self.mainframe, text="last column", width=22)
        user_label.grid(column=4, row=0)

        user_label = tk.Label(self.mainframe, text="             ")
        user_label.grid(column=2, row=1)

        user_label = tk.Label(self.mainframe, text="Button")
        user_label.grid(column=2, row=2, columnspan=2, rowspan=2)

        user_label = tk.Button(self.mainframe, text="      EXIT       ", command=lambda: self.winfo_toplevel().quit())
        user_label.grid(column=2, row=5, pady=40)

        # -------------------------------------------------------------------------------------
        # Adding a Textbox Entry widget
        # -------------------------------------------------------------------------------------
        scrol_w = 500
        scrol_h = 280
        self.scr = tk.Frame(self.mainframe, width=scrol_w, height=scrol_h, bd=10, bg='gray')
        self.scr.grid(column=2, row=2, columnspan=1, rowspan=3, padx=8, pady=8, sticky='n')
        self.scr.grid_propagate(False)

        def gui_deposit(deposit, framed):
            Ent.Transaction.make_deposit(trans1, deposit)
            self.get_amount(deposit)
            controller.show_frame(framed)

        but_img = tk.PhotoImage(file="buttons.png", width=30, height=30)
        # image=but_img, compound=tk.TOP
        # self.action1.image = but_img
        but_img2 = tk.PhotoImage(file="buttons2.png", width=30, height=30)
        # image=but_img2, compound=tk.TOP
        # self.action1.image = but_img2


        # Create "action" button
        trans1 = Ent.Transaction(None, None, None, None, 'Withdrawal')
        self.action1 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Deposit1),
                                 image=but_img, compound=tk.TOP)
        self.action1.grid(column=1, row=2, pady=2, sticky='s')
        self.action1.image = but_img

        self.action2 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Deposit1),
                                 image=but_img, compound=tk.TOP)
        self.action2.grid(column=1, row=3, pady=2)
        self.action2.image = but_img

        self.action3 = tk.Button(self.mainframe, command=lambda: gui_deposit(int(self.deposit_entered.get()), Deposit2),
                                 image=but_img, compound=tk.TOP)
        self.action3.grid(column=1, row=4, pady=2, sticky='n')
        self.action3.image = but_img

        self.action4 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Deposit1),
                                 image=but_img2, compound=tk.TOP)
        self.action4.grid(column=3, row=2, pady=2, sticky='s')
        self.action4.image = but_img2

        self.action5 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Deposit1),
                                 image=but_img2, compound=tk.TOP)
        self.action5.grid(column=3, row=3, pady=2)
        self.action5.image = but_img2

        self.action6 = tk.Button(self.mainframe, command=lambda: controller.show_frame(ThanksForBanking),
                                 image=but_img2, compound=tk.TOP)
        self.action6.grid(column=3, row=4, pady=2, sticky='n')
        self.action6.image = but_img2

        arl2 = tk.Text(self.scr, height=16, width=70, bg='white')
        arl2.pack(expand=True, fill='both')
        arl2.insert('1.0', '                              DEPOSIT 1                                 \n'
                           'Enter an amount                                    \n\n\n\n\n'
                           '                           £                                \n\n\n\n'
                           'CONFIRM                                                         CANCEL')
        arl2.configure(state='disabled')

        self.deposit_entered = tk.Entry(arl2, width=8, textvariable=controller.app_data["amount"])
        self.deposit_entered.place(x=200, y=95)
        self.deposit_entered.focus()

    def get_amount(self, aye):
        self.controller.app_data["amount"].set(aye)


class Deposit2(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.mainframe = tk.LabelFrame(self)
        self.mainframe.grid(column=0, row=0)

        logo_img = tk.PhotoImage(file="background.png", width=3350, height=1809)
        bl = tk.Label(self.mainframe, image=logo_img, compound=tk.TOP)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        bl.image = logo_img

        but_img = tk.PhotoImage(file="buttons.png", width=50, height=50)
        # -------------------------------------------------------------------------------------
        # Grid holders
        # -------------------------------------------------------------------------------------
        logo2_img = tk.PhotoImage(file="barc.png", width=200, height=63)

        user_label = tk.Label(self.mainframe, text="Barclays logo", image=logo2_img)
        user_label.grid(column=0, row=0)
        user_label.image = logo2_img

        user_label = tk.Label(self.mainframe, text="Middle big bits")
        user_label.grid(column=2, row=0, columnspan=1)

        user_label = tk.Label(self.mainframe, text="last column", width=22)
        user_label.grid(column=4, row=0)

        user_label = tk.Label(self.mainframe, text="             ")
        user_label.grid(column=2, row=1)

        user_label = tk.Label(self.mainframe, text="Button")
        user_label.grid(column=2, row=2, columnspan=2, rowspan=2)

        user_label = tk.Button(self.mainframe, text="      EXIT       ", command=lambda: self.winfo_toplevel().quit())
        user_label.grid(column=2, row=5, pady=40)
        # -------------------------------------------------------------------------------------
        # Adding a Textbox Entry widget
        # -------------------------------------------------------------------------------------
        scrol_w = 500
        scrol_h = 280
        self.scr = tk.Frame(self.mainframe, width=scrol_w, height=scrol_h, bd=10, bg='gray')
        self.scr.grid(column=2, row=2, columnspan=1, rowspan=3, padx=8, pady=8, sticky='n')
        self.scr.grid_propagate(False)

        but_img = tk.PhotoImage(file="buttons.png", width=30, height=30)
        # image=but_img, compound=tk.TOP
        # self.action1.image = but_img
        but_img2 = tk.PhotoImage(file="buttons2.png", width=30, height=30)
        # image=but_img2, compound=tk.TOP
        # self.action1.image = but_img2

        # Create "action" button
        self.action1 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Deposit2),
                                 image=but_img, compound=tk.TOP)
        self.action1.grid(column=1, row=2, pady=2, sticky='s')
        self.action1.image = but_img

        self.action2 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Deposit2),
                                 image=but_img, compound=tk.TOP)
        self.action2.grid(column=1, row=3, pady=2)
        self.action2.image = but_img

        self.action3 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Deposit2),
                                 image=but_img, compound=tk.TOP)
        self.action3.grid(column=1, row=4, pady=2, sticky='n')
        self.action3.image = but_img

        self.action4 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Deposit2),
                                 image=but_img2, compound=tk.TOP)
        self.action4.grid(column=3, row=2, pady=2, sticky='s')
        self.action4.image = but_img2

        self.action5 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Deposit2),
                                 image=but_img2, compound=tk.TOP)
        self.action5.grid(column=3, row=3, pady=2)
        self.action5.image = but_img2

        self.action6 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Deposit3),
                                 image=but_img2, compound=tk.TOP)
        self.action6.grid(column=3, row=4, pady=2, sticky='n')
        self.action6.image = but_img2

        arl2 = tk.Text(self.scr, height=16, width=70, bg='white')
        arl2.pack(expand=True, fill='both')
        arl2.insert('1.0', '                              DEPOSIT 2                     \n\n\n'
                           'Insert Cash                                               \n\n\n\n'
                           '                                                           \n\n\n\n'
                           '                                                               COUNT')
        arl2.configure(state='disabled')


class Deposit3(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.mainframe = tk.LabelFrame(self)
        self.mainframe.grid(column=0, row=0)

        logo_img = tk.PhotoImage(file="background.png", width=3350, height=1809)
        bl = tk.Label(self.mainframe, image=logo_img, compound=tk.TOP)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        bl.image = logo_img

        but_img = tk.PhotoImage(file="buttons.png", width=50, height=50)
        # -------------------------------------------------------------------------------------
        # Grid holders
        # -------------------------------------------------------------------------------------
        logo2_img = tk.PhotoImage(file="barc.png", width=200, height=63)

        user_label = tk.Label(self.mainframe, text="Barclays logo", image=logo2_img)
        user_label.grid(column=0, row=0)
        user_label.image = logo2_img

        user_label = tk.Label(self.mainframe, text="Middle big bits")
        user_label.grid(column=2, row=0, columnspan=1)

        user_label = tk.Label(self.mainframe, text="last column", width=22)
        user_label.grid(column=4, row=0)

        user_label = tk.Label(self.mainframe, text="             ")
        user_label.grid(column=2, row=1)

        user_label = tk.Label(self.mainframe, text="Button")
        user_label.grid(column=2, row=2, columnspan=2, rowspan=2)

        user_label = tk.Button(self.mainframe, text="      EXIT       ", command=lambda: self.winfo_toplevel().quit())
        user_label.grid(column=2, row=5, pady=40)

        # -------------------------------------------------------------------------------------
        # Adding a Textbox Entry widget
        # -------------------------------------------------------------------------------------
        scrol_w = 500
        scrol_h = 280
        self.scr = tk.Frame(self.mainframe, width=scrol_w, height=scrol_h, bd=10, bg='gray')
        self.scr.grid(column=2, row=2, columnspan=1, rowspan=3, padx=8, pady=8, sticky='n')
        self.scr.grid_propagate(False)

        def end_transaction(new_page):
            timestamp = dt.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            global trans1
            trans1.stop_time = timestamp
            trans1.is_success = 'YES'
            Ent.helper.log(trans1)
            controller.show_frame(new_page)

        but_img = tk.PhotoImage(file="buttons.png", width=30, height=30)
        # image=but_img, compound=tk.TOP
        # self.action1.image = but_img
        but_img2 = tk.PhotoImage(file="buttons2.png", width=30, height=30)
        # image=but_img2, compound=tk.TOP
        # self.action1.image = but_img2

        # Create "action" button
        self.action1 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Deposit3),
                                 image=but_img, compound=tk.TOP)
        self.action1.grid(column=1, row=2, pady=2, sticky='s')
        self.action1.image = but_img

        self.action2 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Deposit3),
                                 image=but_img, compound=tk.TOP)
        self.action2.grid(column=1, row=3, pady=2)
        self.action2.image = but_img

        self.action3 = tk.Button(self.mainframe, command=lambda: end_transaction(ThanksForBanking),
                                 image=but_img, compound=tk.TOP)
        self.action3.grid(column=1, row=4, pady=2, sticky='n')
        self.action3.image = but_img

        self.action4 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Deposit3),
                                 image=but_img2, compound=tk.TOP)
        self.action4.grid(column=3, row=2, pady=2, sticky='s')
        self.action4.image = but_img2

        self.action5 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Deposit3),
                                 image=but_img2, compound=tk.TOP)
        self.action5.grid(column=3, row=3, pady=2)
        self.action5.image = but_img2

        self.action6 = tk.Button(self.mainframe, command=lambda: controller.show_frame(MainMenu),
                                 image=but_img2, compound=tk.TOP)
        self.action6.grid(column=3, row=4, pady=2, sticky='n')
        self.action6.image = but_img2

        arl2 = tk.Text(self.scr, height=16, width=70, bg='white')
        arl2.pack(expand=True, fill='both')
        arl2.insert('1.0', '                              DEPOSIT 3                     \n\n\n'
                           '                   Your amount to be deposited is:                \n\n\n\n'
                          f'                          £                                       \n\n\n\n'
                           'CONFIRM                                                        CANCEL')
        arl2.configure(state='disabled')

        self.m = Deposit1(parent, controller)

        self.deposit_entered = tk.Entry(arl2, width=8, textvariable=controller.app_data["amount"],
                                        state="readonly")
        self.deposit_entered.place(x=200, y=95)
        self.deposit_entered.focus()


    def get_amount(self):
        a = self.controller.app_data["amount"].get()
        return a


class Mobile1(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.mainframe = tk.LabelFrame(self)
        self.mainframe.grid(column=0, row=0)

        logo_img = tk.PhotoImage(file="background.png", width=3350, height=1809)
        bl = tk.Label(self.mainframe, image=logo_img, compound=tk.TOP)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        bl.image = logo_img

        self.make_widgets(controller)

        # -------------------------------------------------------------------------------------
        # Grid holders
        # -------------------------------------------------------------------------------------

    def make_widgets(self, controller):
        but_img = tk.PhotoImage(file="buttons.png", width=50, height=50)
        self.ant2 = ''
        self.ant3 = ''

        logo2_img = tk.PhotoImage(file="barc.png", width=200, height=63)

        user_label = tk.Label(self.mainframe, text="Barclays logo", image=logo2_img)
        user_label.grid(column=0, row=0)
        user_label.image = logo2_img

        user_label = tk.Label(self.mainframe, text="Middle big bits")
        user_label.grid(column=2, row=0, columnspan=1)

        user_label = tk.Label(self.mainframe, text="last column", width=22)
        user_label.grid(column=4, row=0)

        user_label = tk.Label(self.mainframe, text="             ")
        user_label.grid(column=2, row=1)

        user_label = tk.Label(self.mainframe, text="Button")
        user_label.grid(column=2, row=2, columnspan=2, rowspan=2)

        user_label = tk.Button(self.mainframe, text="      EXIT       ", command=lambda: self.winfo_toplevel().quit())
        user_label.grid(column=2, row=5, pady=40)

        # -------------------------------------------------------------------------------------
        # Adding a Textbox Entry widget
        # -------------------------------------------------------------------------------------
        scrol_w = 500
        scrol_h = 280
        self.scr = tk.Frame(self.mainframe, width=scrol_w, height=scrol_h, bd=10, bg='gray')
        self.scr.grid(column=2, row=2, columnspan=1, rowspan=3, padx=8, pady=8, sticky='n')
        self.scr.grid_propagate(False)

        def gui_mobile(_mobile, _amount, framed):
            ant21 = Ent.Transaction.mobile_topup(trans1, _mobile, _amount)
            self.controller.show_frame(framed)

            self.ant2 = ant21
            self.ant3 = _amount

        def end_transaction(new_page):
            timestamp = dt.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            global trans1
            trans1.stop_time = timestamp
            trans1.is_success = 'YES'
            Ent.helper.log(trans1)
            controller.show_frame(new_page)

        trans1 = Ent.Transaction(None, None, None, None, 'Withdrawal')

        but_img = tk.PhotoImage(file="buttons.png", width=30, height=30)
        # image=but_img, compound=tk.TOP
        # self.action1.image = but_img
        but_img2 = tk.PhotoImage(file="buttons2.png", width=30, height=30)
        # image=but_img2, compound=tk.TOP
        # self.action1.image = but_img2

        # Create "action" button
        self.action1 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Mobile1),
                                 image=but_img, compound=tk.TOP)
        self.action1.grid(column=1, row=2, pady=2, sticky='s')
        self.action1.image = but_img

        self.action2 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Mobile1),
                                 image=but_img, compound=tk.TOP)
        self.action2.grid(column=1, row=3, pady=2)
        self.action2.image = but_img

        self.action3 = tk.Button(self.mainframe, command=lambda: gui_mobile(
                                                                                             self.mobile_entered.
                                                                                             get(), self.topup_amount_entered2.get(), Mobile2), image=but_img, compound=tk.TOP)
        self.action3.grid(column=1, row=4, pady=2, sticky='n')
        self.action3.image = but_img

        self.action4 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Mobile1),
                                 image=but_img2, compound=tk.TOP)
        self.action4.grid(column=3, row=2, pady=2, sticky='s')
        self.action4.image = but_img2

        self.action5 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Mobile1),
                                 image=but_img2, compound=tk.TOP)
        self.action5.grid(column=3, row=3, pady=2)
        self.action5.image = but_img2

        self.action6 = tk.Button(self.mainframe, command=lambda: controller.show_frame(MainMenu),
                                 image=but_img2, compound=tk.TOP)
        self.action6.grid(column=3, row=4, pady=2, sticky='n')
        self.action6.image = but_img2

        arl2 = tk.Text(self.scr, height=16, width=70, bg='white')
        arl2.pack(expand=True, fill='both')

        self.amount = tk.StringVar()
        self.topup_amount_entered2 = tk.Entry(arl2, width=15, textvariable=self.amount)
        self.topup_amount_entered2.place(x=250, y=95)
        self.topup_amount_entered2.focus()

        self.mobile = tk.StringVar()
        self.mobile_entered = tk.Entry(arl2, width=15, textvariable=self.mobile)
        self.mobile_entered.place(x=250, y=50)

        arl2.insert('1.0', '                              MOBILE 1                   \n\n\n\n'
                           '            Enter mobile number:                             \n\n\n'
                           '            Enter top up amount:                           \n\n\n\n'
                           'CONFIRM                                                        CANCEL')
        arl2.configure(state='disabled')

    def set_number(self, num):
        self.controller.app_data["amount"].set(num)


class Mobile2(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.mainframe = tk.LabelFrame(self)
        self.mainframe.grid(column=0, row=0)

        logo_img = tk.PhotoImage(file="background.png", width=3350, height=1809)
        bl = tk.Label(self.mainframe, image=logo_img, compound=tk.TOP)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        bl.image = logo_img

        self.make_widgets2(controller)
        # -------------------------------------------------------------------------------------
        # Grid holders
        # -------------------------------------------------------------------------------------

    def make_widgets2(self, controller):


        logo2_img = tk.PhotoImage(file="barc.png", width=200, height=63)

        user_label = tk.Label(self.mainframe, text="Barclays logo", image=logo2_img)
        user_label.grid(column=0, row=0)
        user_label.image = logo2_img

        user_label = tk.Label(self.mainframe, text="Middle big bits")
        user_label.grid(column=2, row=0, columnspan=1)

        user_label = tk.Label(self.mainframe, text="last column", width=22)
        user_label.grid(column=4, row=0)

        user_label = tk.Label(self.mainframe, text="             ")
        user_label.grid(column=2, row=1)

        user_label = tk.Label(self.mainframe, text="Button")
        user_label.grid(column=2, row=2, columnspan=2, rowspan=2)

        user_label = tk.Button(self.mainframe, text="      EXIT       ", command=lambda: self.winfo_toplevel().quit())
        user_label.grid(column=2, row=5, pady=40)

        # -------------------------------------------------------------------------------------
        # Adding a Textbox Entry widget
        # -------------------------------------------------------------------------------------
        scrol_w = 500
        scrol_h = 280
        self.scr = tk.Frame(self.mainframe, width=scrol_w, height=scrol_h, bd=10, bg='gray')
        self.scr.grid(column=2, row=2, columnspan=1, rowspan=3, padx=8, pady=8, sticky='n')
        self.scr.grid_propagate(False)

        but_img = tk.PhotoImage(file="buttons.png", width=30, height=30)
        # image=but_img, compound=tk.TOP
        # self.action1.image = but_img
        but_img2 = tk.PhotoImage(file="buttons2.png", width=30, height=30)
        # image=but_img2, compound=tk.TOP
        # self.action1.image = but_img2

        # Create "action" button
        self.action1 = tk.Button(self.mainframe,  command=lambda: controller.show_frame(Mobile2), image=but_img, compound=tk.TOP)
        self.action1.grid(column=1, row=2, pady=2, sticky='s')
        self.action1.image = but_img

        self.action2 = tk.Button(self.mainframe,  command=lambda: controller.show_frame(Mobile2), image=but_img, compound=tk.TOP)
        self.action2.grid(column=1, row=3, pady=2)
        self.action2.image = but_img

        self.action3 = tk.Button(self.mainframe, command=lambda: self.print_it(arl2), image=but_img, compound=tk.TOP)
        self.action3.configure(command=lambda: self.print_it(arl2))
        self.action3.grid(column=1, row=4, pady=2, sticky='n')
        self.action3.image = but_img

        self.action4 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Mobile2),
                                 image=but_img2, compound=tk.TOP)
        self.action4.grid(column=3, row=2, pady=2, sticky='s')
        self.action4.image = but_img2

        self.action5 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Mobile2),
                                 image=but_img2, compound=tk.TOP)
        self.action5.grid(column=3, row=3, pady=2)
        self.action5.image = but_img2

        self.action6 = tk.Button(self.mainframe, command=lambda: controller.show_frame(Mobile1),
                                 image=but_img2, compound=tk.TOP)
        self.action6.grid(column=3, row=4, pady=2, sticky='n')
        self.action6.image = but_img2

        arl2 = tk.Text(self.scr, height=16, width=70, bg='white')
        arl2.pack(expand=True, fill='both')
        arl2.insert('1.0', '                              MOBILE 2                     \n\n\n'
                           '                                                             \n\n'
                           '                           Confirm top-up                  \n\n\n'
                           '                                                         \n\n\n\n'
                           'CONFIRM                                                        CANCEL')
        arl2.configure(state='disabled')

    def end_transaction(self, new_page, sufficiency):
        timestamp = dt.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        global trans1
        trans1.stop_time = timestamp
        if sufficiency == 1:
            trans1.is_success = 'YES'
        else:
            trans1.is_success = 'NO'
        Ent.helper.log(trans1)
        self.controller.show_frame(new_page)

    def insufficient_funds_message(self):
        msg.showwarning('Warning', 'You do not have enough funds to make this transaction')


    def print_it(self, Texts):
        Texts.destroy()

        startpage = self.controller.get_page("Mobile1")
        startpage.mobile_entered.delete(0, 100)

        value = startpage.ant3
        startpage.topup_amount_entered2.delete(0, 100)

        def delete2():
            self.end_transaction(Mobile1, 0)
            arl3 = tk.Text(self.scr, height=16, width=70, bg='white')
            arl3.pack(expand=True, fill='both')
            arl3.insert('1.0', '                              MOBILE 2                     \n\n\n'
                               '                                                             \n\n'
                               '                           Confirm top-up                  \n\n\n'
                               '                                                         \n\n\n\n'
                               'CONFIRM                                                        CANCEL')
            arl3.configure(state='disabled')
            self.action3.configure(command=lambda: self.print_it(arl3))

        if float(value) > Ent.helper.retrieve_balance():
            print('Insufficient funds')
            self.insufficient_funds_message()
            self.end_transaction(Mobile1, 0)
            delete2()

            global trans1
            trans1.is_success = 'NO'
            trans1.stop_time = dt.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            # self.action3.configure(command=lambda: self.print_it(arl2))
            self.action6.configure(command=lambda: self.end_transaction(ThanksForBanking, 0))

        else:
            print(f"Topup amount is: {value}")

            phone_line = startpage.ant2
            arl2 = tk.Text(self.scr, height=16, width=70, bg='white')
            arl2.place(bordermode='inside')
            arl2.insert('1.0', '                              MOBILE 2                     \n\n\n'
                              f'                       Your line is {phone_line}                \n\n'
                              f'                       Your top up amount is: £{value}          \n\n\n'
                               '            Would you like to carry out another transaction?   \n\n\n\n'
                               'YES                                                            NO')
            arl2.configure(state='disabled')
            self.action3.configure(command=lambda: delete2())
            self.action6.configure(command=lambda: self.end_transaction(ThanksForBanking, 1))

        def delete2():
            self.end_transaction(MainMenu, 1)
            arl2.destroy()
            arl3 = tk.Text(self.scr, height=16, width=70, bg='white')
            arl3.pack(expand=True, fill='both')
            arl3.insert('1.0', '                              MOBILE 2                     \n\n\n'
                               '                                                             \n\n'
                               '                           Confirm top-up                  \n\n\n'
                               '                                                         \n\n\n\n'
                               'CONFIRM                                                        CANCEL')
            arl3.configure(state='disabled')
            self.action3.configure(command=lambda: self.print_it(arl3))


class ChangePin1(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.mainframe = tk.LabelFrame(self)
        self.mainframe.grid(column=0, row=0)

        logo_img = tk.PhotoImage(file="background.png", width=3350, height=1809)
        bl = tk.Label(self.mainframe, image=logo_img, compound=tk.TOP)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        bl.image = logo_img

        self.make_widgets(controller)

    def make_widgets(self, controller):
        # -------------------------------------------------------------------------------------
        # Grid holders
        # -------------------------------------------------------------------------------------
        logo2_img = tk.PhotoImage(file="barc.png", width=200, height=63)

        user_label = tk.Label(self.mainframe, text="Barclays logo", image=logo2_img)
        user_label.grid(column=0, row=0)
        user_label.image = logo2_img

        user_label = tk.Label(self.mainframe, text="last column", width=22)
        user_label.grid(column=4, row=0)

        user_label = tk.Label(self.mainframe, text="Middle big bits")
        user_label.grid(column=2, row=0, columnspan=1)


        user_label = tk.Label(self.mainframe, text="             ")
        user_label.grid(column=2, row=1)

        user_label = tk.Label(self.mainframe, text="Button")
        user_label.grid(column=2, row=2, columnspan=2, rowspan=2)

        user_label = tk.Button(self.mainframe, text="      EXIT       ", command=lambda: self.winfo_toplevel().quit())
        user_label.grid(column=2, row=5, pady=40)

        # -------------------------------------------------------------------------------------
        # Adding a Textbox Entry widget
        # -------------------------------------------------------------------------------------
        scrol_w = 500
        scrol_h = 280
        self.scr = tk.Frame(self.mainframe, width=scrol_w, height=scrol_h, bd=10, bg='gray')
        self.scr.grid(column=2, row=2, columnspan=1, rowspan=3, padx=8, pady=8, sticky='n')
        self.scr.grid_propagate(False)

        def change_pin(old, new, framed):
            ant1 = Ent.Transaction.change_pin(trans1, old, new)
            if ant1 is False:
                self.incorrect_pin_message()
                end_transaction(framed, 0)
            elif ant1 == 'same pin error':
                self.illegal_pin_message()
                end_transaction(framed, 0)

            else:
                end_transaction(framed, 1)
                self.success()

        def end_transaction(new_page, sufficiency):
            timestamp = dt.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            global trans1
            trans1.stop_time = timestamp
            if sufficiency == 1:
                trans1.is_success = 'YES'
            else:
                trans1.is_success = 'NO'
            Ent.helper.log(trans1)
            controller.show_frame(new_page)

        but_img = tk.PhotoImage(file="buttons.png", width=30, height=30)
        # image=but_img, compound=tk.TOP
        # self.action1.image = but_img
        but_img2 = tk.PhotoImage(file="buttons2.png", width=30, height=30)
        # image=but_img2, compound=tk.TOP
        # self.action1.image = but_img2

        # Create "action" button
        self.action1 = tk.Button(self.mainframe, command=lambda: controller.show_frame(ChangePin1),
                                 image=but_img, compound=tk.TOP)
        self.action1.grid(column=1, row=2, pady=2, sticky='s')
        self.action1.image = but_img

        self.action2 = tk.Button(self.mainframe,  command=lambda: controller.show_frame(ChangePin1),
                                 image=but_img, compound=tk.TOP)
        self.action2.grid(column=1, row=3, pady=2)
        self.action2.image = but_img

        self.action3 = tk.Button(self.mainframe, command=lambda: change_pin(int(self.current_pin.get()),
                                                                                             int(self.new_pin.get()),
                                                                                             MainMenu), image=but_img, compound=tk.TOP)
        self.action3.grid(column=1, row=4, pady=2, sticky='n')
        self.action3.image = but_img

        self.action4 = tk.Button(self.mainframe, command=lambda: controller.show_frame(ChangePin1),
                                 image=but_img2, compound=tk.TOP)
        self.action4.grid(column=3, row=2, pady=2, sticky='s')
        self.action4.image = but_img2

        self.action5 = tk.Button(self.mainframe, command=lambda: controller.show_frame(ChangePin1),
                                 image=but_img2, compound=tk.TOP)
        self.action5.grid(column=3, row=3, pady=2)
        self.action5.image = but_img2

        self.action6 = tk.Button(self.mainframe, command=lambda: controller.show_frame(MainMenu),
                                 image=but_img2, compound=tk.TOP)
        self.action6.grid(column=3, row=4, pady=2, sticky='n')
        self.action6.image = but_img2

        arl2 = tk.Text(self.scr, height=16, width=70, bg='white')
        arl2.pack(expand=True, fill='both')
        arl2.insert('1.0', '                              CHANGE PIN                     \n\n\n\n'
                           '            Enter current PIN                                              \n\n'
                           '                Enter new PIN                                          \n\n\n\n'
                           'CONFIRM                                                         CANCEL')

        self.current = tk.StringVar()
        self.current_pin = tk.Entry(arl2, width=15, textvariable=self.current, show='*')
        self.current_pin.place(x=230, y=50)
        self.current_pin.focus()

        self.new = tk.StringVar()
        self.new_pin = tk.Entry(arl2, width=15, textvariable=self.new, show='*')
        self.new_pin.place(x=230, y=95)

    def incorrect_pin_message(self):

        msg.showerror('Error', 'Incorrect PIN')
        self.current_pin.delete(0, 'end')
        self.new_pin.delete(0, 'end')

    def illegal_pin_message(self):

        msg.showwarning('Warning', 'New PIN cannot match previous one. Choose another PIN')
        self.current_pin.delete(0, 'end')
        self.new_pin.delete(0, 'end')

    def success(self):
        msg.showinfo('Success', 'PIN successfully updated')


class CollectCard(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.mainframe = tk.LabelFrame(self)
        self.mainframe.grid(column=0, row=0)

        logo_img = tk.PhotoImage(file="background.png", width=3350, height=1809)
        bl = tk.Label(self.mainframe, image=logo_img, compound=tk.TOP)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        bl.image = logo_img

        # -------------------------------------------------------------------------------------
        # Grid holders
        # -------------------------------------------------------------------------------------
        logo2_img = tk.PhotoImage(file="barc.png", width=200, height=63)

        user_label = tk.Label(self.mainframe, text="Barclays logo", image=logo2_img)
        user_label.grid(column=0, row=0)
        user_label.image = logo2_img

        user_label = tk.Label(self.mainframe, text="last column", width=22)
        user_label.grid(column=4, row=0)

        user_label = tk.Label(self.mainframe, text="Middle big bits")
        user_label.grid(column=2, row=0, columnspan=1)

        user_label = tk.Label(self.mainframe, text="             ")
        user_label.grid(column=2, row=1)

        user_label = tk.Label(self.mainframe, text="Button")
        user_label.grid(column=2, row=2, columnspan=2, rowspan=2)

        user_label = tk.Button(self.mainframe, text="      EXIT       ", command=lambda: self.winfo_toplevel().quit())
        user_label.grid(column=2, row=5, pady=40)

        # -------------------------------------------------------------------------------------
        # Adding a Textbox Entry widget
        # -------------------------------------------------------------------------------------
        scrol_w = 500
        scrol_h = 280
        self.scr = tk.Frame(self.mainframe, width=scrol_w, height=scrol_h, bd=10, bg='gray')
        self.scr.grid(column=2, row=2, columnspan=1, rowspan=3, padx=8, pady=8, sticky='n')
        self.scr.grid_propagate(False)

        but_img = tk.PhotoImage(file="buttons.png", width=30, height=30)
        # image=but_img, compound=tk.TOP
        # self.action1.image = but_img
        but_img2 = tk.PhotoImage(file="buttons2.png", width=30, height=30)
        # image=but_img2, compound=tk.TOP
        # self.action1.image = but_img2

        # Create "action" button
        self.action1 = tk.Button(self.mainframe,  command=lambda: controller.show_frame(CollectCard),
                                 image=but_img, compound=tk.TOP)
        self.action1.grid(column=1, row=2, pady=2, sticky='s')
        self.action1.image = but_img

        self.action2 = tk.Button(self.mainframe,  command=lambda: controller.show_frame(CollectCard),
                                 image=but_img, compound=tk.TOP)
        self.action2.grid(column=1, row=3, pady=2)
        self.action2.image = but_img

        self.action3 = tk.Button(self.mainframe,  command=lambda: controller.show_frame(CollectCard),
                                 image=but_img, compound=tk.TOP)
        self.action3.grid(column=1, row=4, pady=2, sticky='n')
        self.action3.image = but_img

        self.action4 = tk.Button(self.mainframe, command=lambda: controller.show_frame(CollectCard), image=but_img2, compound=tk.TOP)
        self.action4.grid(column=3, row=2, pady=2, sticky='s')
        self.action4.image = but_img2

        self.action5 = tk.Button(self.mainframe, command=lambda: controller.show_frame(CollectCard),
                                 image=but_img2, compound=tk.TOP)
        self.action5.grid(column=3, row=3, pady=2)
        self.action5.image = but_img2

        self.action6 = tk.Button(self.mainframe, command=lambda: controller.show_frame(CollectCard),
                                 image=but_img2, compound=tk.TOP)
        self.action6.grid(column=3, row=4, pady=2, sticky='n')
        self.action6.image = but_img2

        arl2 = tk.Text(self.scr, height=16, width=70, bg='white')
        arl2.pack(expand=True, fill='both')
        arl2.insert('1.0', '                              COLLECT CARD                     \n\n\n'
                           '                        Please collect your card                \n\n\n\n'
                           '                                                                \n\n\n\n'
                           '                                                                       ')
        arl2.configure(state='disabled')


class ThanksForBanking(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.mainframe = tk.LabelFrame(self)
        self.mainframe.grid(column=0, row=0)

        logo_img = tk.PhotoImage(file="background.png", width=3350, height=1809)
        bl = tk.Label(self.mainframe, image=logo_img, compound=tk.TOP)
        bl.place(x=0, y=0, relwidth=1, relheight=1)
        bl.image = logo_img

        # -------------------------------------------------------------------------------------
        # Grid holders
        # -------------------------------------------------------------------------------------
        logo2_img = tk.PhotoImage(file="barc.png", width=200, height=63)

        user_label = tk.Label(self.mainframe, text="Barclays logo", image=logo2_img)
        user_label.grid(column=0, row=0)
        user_label.image = logo2_img

        user_label = tk.Label(self.mainframe, text="last column", width=22)
        user_label.grid(column=4, row=0)

        user_label = tk.Label(self.mainframe, text="Middle big bits")
        user_label.grid(column=2, row=0, columnspan=1)

        user_label = tk.Label(self.mainframe, text="             ")
        user_label.grid(column=2, row=1)

        user_label = tk.Label(self.mainframe, text="Button")
        user_label.grid(column=2, row=2, columnspan=2, rowspan=2)

        user_label = tk.Button(self.mainframe, text="      EXIT       ", command=lambda: self.winfo_toplevel().quit())
        user_label.grid(column=2, row=5, pady=40)

        # -------------------------------------------------------------------------------------
        # Adding a Textbox Entry widget
        # -------------------------------------------------------------------------------------
        scrol_w = 500
        scrol_h = 280
        self.scr = tk.Frame(self.mainframe, width=scrol_w, height=scrol_h, bd=10, bg='gray')
        self.scr.grid(column=2, row=2, columnspan=1, rowspan=3, padx=8, pady=8, sticky='n')
        self.scr.grid_propagate(False)

        but_img = tk.PhotoImage(file="buttons.png", width=30, height=30)
        # image=but_img, compound=tk.TOP
        # self.action1.image = but_img
        but_img2 = tk.PhotoImage(file="buttons2.png", width=30, height=30)
        # image=but_img2, compound=tk.TOP
        # self.action1.image = but_img2

        # Create "action" button
        self.action1 = tk.Button(self.mainframe,  command=lambda: controller.show_frame(ThanksForBanking),
                                 image=but_img, compound=tk.TOP)
        self.action1.grid(column=1, row=2, pady=2, sticky='s')
        self.action1.image = but_img

        self.action2 = tk.Button(self.mainframe,  command=lambda: controller.show_frame(ThanksForBanking),
                                 image=but_img, compound=tk.TOP)
        self.action2.grid(column=1, row=3, pady=2)
        self.action2.image = but_img

        self.action3 = tk.Button(self.mainframe,  command=lambda: controller.show_frame(ThanksForBanking),
                                 image=but_img, compound=tk.TOP)
        self.action3.grid(column=1, row=4, pady=2, sticky='n')
        self.action3.image = but_img

        self.action4 = tk.Button(self.mainframe, command=lambda: controller.show_frame(ThanksForBanking),
                                 image=but_img2, compound=tk.TOP)
        self.action4.grid(column=3, row=2, pady=2, sticky='s')
        self.action4.image = but_img2

        self.action5 = tk.Button(self.mainframe, command=lambda: controller.show_frame(ThanksForBanking),
                                 image=but_img2, compound=tk.TOP)
        self.action5.grid(column=3, row=3, pady=2)
        self.action5.image = but_img2

        self.action6 = tk.Button(self.mainframe, command=lambda: controller.show_frame(ThanksForBanking),
                                 image=but_img2, compound=tk.TOP)
        self.action6.grid(column=3, row=4, pady=2, sticky='n')
        self.action6.image = but_img2

        arl2 = tk.Text(self.scr, height=16, width=70, bg='white')
        arl2.pack(expand=True, fill='both')
        arl2.insert('1.0', '                                                   \n\n\n'
                           '   \n\n\n\n'
                           '                 Thanks for banking with barclays           \n\n\n\n'
                           '')
        arl2.configure(state='disabled')


class ValueHolders:

    def __init__(self):
        pass


    def bring_back(self, value):
        return value

    def update_value(self, here):
        bal_file = open("val_file", 'w+')
        bal_file.write(f'{here}')
        bal_file.close()

    def return_value(self):
        balfile = open("val_file", 'r')
        balance = balfile.read()
        balfile.close()
        return balance


# app = SeaofBTCapp()
# app.wm_attributes('-alpha', 0.7)
#app.mainloop()
