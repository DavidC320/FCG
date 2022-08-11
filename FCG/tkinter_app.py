# 8/4/2022
# stuff
# David Cruz

from tkinter import *
from tkinter import ttk
from pil_image_maker import create_comic_panel, save_image
from toplevels import Info, Secret

class Image_app(Tk):
    def __init__(self):
        super().__init__()

        # window settings
        self.title("Image shop")
        self.style = ttk.Style(self)
        self.style.theme_use("vista")
        # icon_image = PhotoImage(file= r"")

        # Menu
        mainmenu = Menu(self)
        # menu items
        mainmenu.add_command(label = "Info", command=self.open_info)
        mainmenu.add_command(label = "Settings", state = DISABLED)
        mainmenu.add_command(label = "Secrets", command=self.open_secret)

        self.config(menu=mainmenu)
        
        # Main frame
        self.frame = Frame(self)
        self.frame.grid(column=0, row=0)

        # tab
        self.tab_menu = ttk.Notebook(self)
        # create tabs
        tab1 = Generator(self.tab_menu)
        # add tabs
        self.tab_menu.add(tab1, text="Generator")
        # pack tabs
        self.tab_menu.grid(column=0, row=0)

    def open_info(self):
        # code based off of Python Tutorial and GeeksforGeeks
        # https://www.pythontutorial.net/tkinter/tkinter-toplevel/
        # https://www.geeksforgeeks.org/python-tkinter-toplevel-widget/
        lev2 = Info(self)
        lev2.grab_set()

    def open_secret(self):
        lev2 = Secret(self)
        lev2.grab_set()

class Generator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, padx=50, pady=50, bg="#faefca")
        stuff = create_comic_panel()
        self.comic_img = stuff[0]
        self.comic_imgtk = stuff[1]

        ################################################################################################ frames
        self.comic_holder = Frame(self, bg="#bbc0d4", width=550, height=550, relief="sunken", border=10)
        self.comic_cont_panel = Frame(self, bg="#bbc0d4", width=275, height=550, relief="ridge", border=10)
        self.panel_controlls = Frame(self.comic_cont_panel, bg="#d4bbc0", height=458, width=275, relief="sunken", border=5)

        self.comic_holder.grid(column=0, row=1)
        self.comic_cont_panel.grid(column=1, row=1)
        self.panel_controlls.grid(column=0, row=0, pady=(0, 20))
        
        ################################################################################################ labels
        Label(self, text="Comic", font=("arial", 20), relief="groove").grid(column=0, row=0, sticky="WE")
        Label(self, text="Controls", font=("arial", 20), relief="groove").grid(column=1, row=0, sticky="WE")
        self.image_label = Label(self.comic_holder, image=self.comic_imgtk)
        self.image_label.grid(column=0, row=0)

        ################################################################################################ buttons
        #lucita was here:)
        self.randomize_comic = Button(self.comic_cont_panel, text="Random", command=self.random_comic)
        self.save_comic = Button(self.comic_cont_panel, text="Save", command=lambda: save_image(self.comic_img))

        self.randomize_comic.grid(column=0, row=1, sticky="WE")
        self.save_comic.grid(column=0, row=2, sticky="WE")

    def random_comic(self):
        self.comic_img, self.comic_imgtk = create_comic_panel()
        self.image_label.config(image=self.comic_imgtk)

if __name__ == "__main__":
    app = Image_app()
    app.mainloop()