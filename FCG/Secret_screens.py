# 8/9/2022
# Secret screens

from os import stat
from tkinter import *
from PIL import ImageTk, Image
from pil_image_maker import save_image

class Secret1(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # settings
        self.title = "Secret"

        # Image
        self.img = Image.open(r"FCG\defualt_img\Angry.png")
        self.imgtk = ImageTk.PhotoImage(self.img)

        # Labels
        Label(self, image=self.imgtk).pack()

        # buttons
        Button(self, text="Save", command= lambda: save_image(self.img)).pack()