# 4PINT Assessment 2 - Paul Stuart 000389223
# Login Class
# 16.06.21

import tkinter as tk
from abc import abstractmethod
from tkinter import messagebox, END


class Login:
    __correct_cred = False
    __correct_user = ""
    __correct_pw = ""

    @classmethod
    def set_correct_cred(cls, bool_val):
        cls.__correct_cred = bool_val

    @classmethod
    def is_correct_cred(cls):
        return cls.__correct_cred

    @classmethod
    def read_in(cls):
        credentials = []
        file = open('login_data.txt', 'r')
        for line in file:
            credentials.append(line.rstrip('\n'))
        cls.__correct_user = credentials[0]
        cls.__correct_pw = credentials[1]
        cls.__correct_user.strip()
        cls.__correct_pw.strip()

    @classmethod
    def login_gui(cls):

        cls.read_in()

        def check():
            user_name = user_n.get()
            pass_word = pw.get()
            popup = messagebox

            if user_name == "" and pass_word == "":
                popup.showinfo("", "Blank Not Allowed")
            elif user_name == cls.__correct_user and pass_word == cls.__correct_pw:
                popup.showinfo("", "Login Success")
                cls.set_correct_cred(True)
                root.destroy()
            else:
                popup.showinfo("", "Incorrect Username and Password")

        def getNumber(event):
            text = event.widget['text']
            if root.focus_get() == user_n:
                user_n.insert(END, text)
            elif root.focus_get() == pw:
                pw.insert(END, text)
            else:
                messagebox.showwarning('Error!', 'Please click into the box you wish to enter numbers for.')

        def clearAll():
            user_n.delete(0, END)
            pw.delete(0, END)

        root = tk.Tk()
        root.title("Admin Login to Dodgy Bros Interface")
        root.geometry("500x700")
        root.configure(bg='yellow')
        root.iconbitmap('carYellow.ico')

        # row configure
        root.rowconfigure(0, weight=3)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=3)
        root.rowconfigure(3, weight=3)
        root.rowconfigure(4, weight=3)
        root.rowconfigure(5, weight=3)

        # column configure
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)

        # defining widgets
        heading = tk.Label(root, text='DODGY BROTHERS LOG IN', font=('Verdana', 16, 'bold'), bg='yellow', fg='grey')
        pw = tk.Label(root, text='Username/PIN >', bg='yellow', fg='black', font=('Verdana', 8, 'bold'))
        user_n = tk.Entry(root)
        pw = tk.Entry(root, show='*')
        btn_width = 4
        btn_height = 4
        font_size = 16
        one = tk.Button(root, text='1', bg='white', width=btn_width, height=btn_height, relief='ridge',
                        font=('Verdana', font_size, 'bold'))
        two = tk.Button(root, text='2', bg='white', width=btn_width, height=btn_height,
                        font=('Verdana', font_size, 'bold'), relief='ridge')
        three = tk.Button(root, text='3', bg='white', width=btn_width, height=btn_height,
                          font=('Verdana', font_size, 'bold'), relief='ridge')
        four = tk.Button(root, text='4', bg='white', width=btn_width, height=btn_height,
                         font=('Verdana', font_size, 'bold'), relief='ridge')
        five = tk.Button(root, text='5', bg='white', width=btn_width, height=btn_height,
                         font=('Verdana', font_size, 'bold'), relief='ridge')
        six = tk.Button(root, text='6', bg='white', width=btn_width, height=btn_height,
                        font=('Verdana', font_size, 'bold'), relief='ridge')
        seven = tk.Button(root, text='7', bg='white', width=btn_width, height=btn_height,
                          font=('Verdana', font_size, 'bold'), relief='ridge')
        eight = tk.Button(root, text='8', bg='white', width=btn_width, height=btn_height,
                          font=('Verdana', font_size, 'bold'), relief='ridge')
        nine = tk.Button(root, text='9', bg='white', width=btn_width, height=btn_height,
                         font=('Verdana', font_size, 'bold'), relief='ridge')
        cancel = tk.Button(root, text='CANCEL\nCLEAR', bg='red', fg='white', width=btn_width, height=btn_height,
                           command=clearAll, font=('Verdana', font_size, 'bold'), relief='ridge')
        zero = tk.Button(root, text='0', bg='white', width=btn_width, height=btn_height,
                         font=('Verdana', font_size, 'bold'), relief='ridge')
        log_in = tk.Button(root, text='Log in', bg='green', fg='white', width=btn_width, height=btn_height,
                           command=check, font=('Verdana', font_size, 'bold'), relief='ridge')

        # defining grid
        heading.grid(row=0, column=0, rowspan=1, columnspan=3, sticky='nsew')
        pw.grid(row=1, column=0, sticky='nsew')
        user_n.grid(row=1, column=1, sticky='nsew', padx=(10, 10), pady=(10, 10))
        pw.grid(row=1, column=2, sticky='nsew', padx=(10, 20), pady=(10, 10))
        one.grid(row=2, column=0, sticky='nsew', padx=(20, 10), pady=(10, 10))
        two.grid(row=2, column=1, sticky='nsew', padx=(10, 10), pady=(10, 10))
        three.grid(row=2, column=2, sticky='nsew', padx=(10, 20), pady=(10, 10))
        four.grid(row=3, column=0, sticky='nsew', padx=(20, 10), pady=(10, 10))
        five.grid(row=3, column=1, sticky='nsew', padx=(10, 10), pady=(10, 10))
        six.grid(row=3, column=2, sticky='nsew', padx=(10, 20), pady=(10, 10))
        seven.grid(row=4, column=0, sticky='nsew', padx=(20, 10), pady=(10, 10))
        eight.grid(row=4, column=1, sticky='nsew', padx=(10, 10), pady=(10, 10))
        nine.grid(row=4, column=2, sticky='nsew', padx=(10, 20), pady=(10, 10))
        cancel.grid(row=5, column=0, sticky='nsew', padx=(20, 10), pady=(10, 20))
        zero.grid(row=5, column=1, sticky='nsew', padx=(10, 10), pady=(10, 20))
        log_in.grid(row=5, column=2, sticky='nsew', padx=(10, 20), pady=(10, 20))

        # Binding Functions to buttons
        one.bind('<Button-1>', getNumber)
        two.bind('<Button-1>', getNumber)
        three.bind('<Button-1>', getNumber)
        four.bind('<Button-1>', getNumber)
        five.bind('<Button-1>', getNumber)
        six.bind('<Button-1>', getNumber)
        seven.bind('<Button-1>', getNumber)
        eight.bind('<Button-1>', getNumber)
        nine.bind('<Button-1>', getNumber)
        zero.bind('<Button-1>', getNumber)

        root.mainloop()
