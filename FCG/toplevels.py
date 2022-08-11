# 8/8/2022

from tkinter import *
from tkinter import messagebox
from text_list import codes
import Secret_screens

class Info(Toplevel):
    # code based off of Python Tutorial and GeeksforGeeks
    # https://www.pythontutorial.net/tkinter/tkinter-toplevel/
    # https://www.geeksforgeeks.org/python-tkinter-toplevel-widget/
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Info")

        # labels
        Label(self, text="Welcome to FCG!").pack()
        Label(self, text="FCG or Funny. Comic. Genorator\n is a generator for random blocks of comics").pack()

class Secret(Toplevel):
    def __init__(self, parents):
        super().__init__(parents)
        # top level settings
        self.title("Secrets")

        # Variable
        # code from Geeks for geeks
        # https://www.geeksforgeeks.org/python-tkinter-entry-widget/
        self.pass_var = StringVar()
        self.pass_var.set("Enter Password")

        # Frames
        self.screen = Frame(self, bg="Green", relief=SUNKEN, border=10)

        self.screen.pack()

        # Labels
        Label(self.screen, text="Enter password", font=("arial", 20), bg="Green").pack()

        # Entry
        Entry(self.screen, textvariable=self.pass_var, bg="Green").pack()

        # Buttons
        Button(self.screen, text = "Enter", command=self.enter_password, bg="Green").pack()

    def enter_password(self):
        # code from Geeks for geeks
        # https://www.geeksforgeeks.org/python-tkinter-entry-widget/
        code = self.pass_var.get()
        if code in codes.keys():
            number = codes.get(code)
            self.open_secrets(number)
        else:
            self.attributes('-disabled', True)
            messagebox.showinfo("Incorrect Password", "The Password you entered doesn't match.")
            self.attributes('-disabled', False)

        self.pass_var.set("Enter Password")

    def open_secrets(self, number):
        
        if number == 1:
            top3 = Secret_screens.Secret1(self)
        
        top3.grab_set()
