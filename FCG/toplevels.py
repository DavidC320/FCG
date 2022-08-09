# 8/8/2022

from tkinter import *

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