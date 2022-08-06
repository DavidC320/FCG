# 8/4/2022
# stuff
# David Cruz

from cProfile import label
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageFont, ImageDraw

class Image_app(Tk):
    def __init__(self):
        super().__init__()

        # window settings
        self.title("Image shop")
        self.style = ttk.Style(self)
        self.style.theme_use("vista")
        # icon_image = PhotoImage(file= r"")

        # Menu
        menu_frame = Frame(self).grid(column=0, row=0)
        mainmenu = Menu(menu_frame)
        # menu items
        mainmenu.add(label = "Info")

        self.config(menu=mainmenu)
        
        # Main frame
        self.frame = Frame(self)
        self.frame.pack()

        # tabs
        self.tabMenu = ttk.Notebook(self.frame)

        # frame tabs
        tab1 = Frame(self.tabMenu)

        # add tabs
        self.tabMenu.add(tab1, text="FCG")

        # pack taabs
        self.tabMenu.grid(column=0, row=0)

        # Notebook

if __name__ == "__main__":
    app = Image_app()
    app.resizable(False, False)
    app.mainloop()