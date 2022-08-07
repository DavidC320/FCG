# 8/5/2022
# Pil
# David Cruz

from math import ceil
from tkinter import CENTER
from PIL import Image, ImageTk, ImageFont, ImageDraw
from random import randint

def create_default_img():
    # inital image
    img = Image.new("RGBA", (550, 550), (250, 250, 250, 250))

    # draw lines
    canvas = Image.new("RGBA", (550, 550), (250, 250, 250, 0))
    draw = ImageDraw.Draw(img)
    draw.line(((0, 0), (550, 0), (550, 550), (0, 550), (0, 0)), fill=(1, 1, 1), width=10)

    draw.line((550/2, 0, 550/2, 550), fill=(1, 1, 1), width=10)
    draw.line((0, 550/2, 550, 550/2), fill=(1, 1, 1), width=10)

    #img = Image.alpha_composite(img, draw)

    img = ImageTk.PhotoImage(img)
    return img

def create_comic_panel(use_4 = True):
    if use_4:
        return four_paneled()

def four_paneled():
    panels = []

    for _ in range(4):
        panel = Image.new("RGBA", (275, 275), (randint(0, 250), randint(0, 250), randint(0, 250), 250))
        draw = ImageDraw.Draw(panel)

        text ="alkjsdhkjlsdfhghf;d;fjkghjghjkdfsghghj" # klnmopqrstuvwxyz123

        draw.rectangle(((0, 0), (275, 70)), fill="white", outline="black", width=5)

        comic_text_draw(text, draw)

        draw.line(((0, 0), (275, 0), (275, 275), (0, 275), (0, 0)), fill=(1, 1, 1), width=10)
        
        panels.append(panel)

    strip = Image.new("RGBA", (550, 550), (250, 250, 250, 250))

    strip.paste(panels[0], (0, 0))
    strip.paste(panels[1], (275, 0))
    strip.paste(panels[2], (0, 275))
    strip.paste(panels[3], (275, 275))

    img = ImageTk.PhotoImage(strip)
    return img

def comic_text_draw(str, img):
    max_char = 29*3

    lines = ceil(len(str) / 29)
    if lines > 3:
        lines = 3
        str[: max_char]

    divions = {
        1 : 1/2,
        2 : 1/3,
        3 : 1/4,
    }
    
    font = ImageFont.truetype(r"C:WINDOWS\\FONTS\\LTYPE.TTF", 15)
    if lines == 1:
        # code segmant from Vishal and Paul
        # https://stackoverflow.com/questions/4902198/pil-how-to-scale-text-size-in-relation-to-the-size-of-the-image
        font_size = 15
        while font.getsize(str)[0] < 270 and font.getsize(str)[1] < 60:
            font_size += 1
            font = ImageFont.truetype(r"C:WINDOWS\\FONTS\\LTYPE.TTF", font_size)
        font_size -= 1
        font = ImageFont.truetype(r"C:WINDOWS\\FONTS\\LTYPE.TTF", font_size)

    divid_by = divions.get(lines)
    start_index = 0
    end_index = 29
    for num in range(lines):
        if num == lines:
            text = str[start_index :]
        else:
            text = str[start_index : end_index]
        
        img.text((275/2, 60 * divid_by + 5), text, fill= "black", anchor="mm", font=font)

        start_index += 29
        end_index += 29
        divid_by += divid_by
    



