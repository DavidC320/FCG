from PIL import Image, ImageFilter, ImageColor
from random import choice, randint, random

def converter(path, size, mode):
    img = Image.open(path)
    img = img.resize(size)
    img = img.convert(mode)
    return img

def create_drip(path, mode, resize_factor, pos, rotate, flip = False):
    img = Image.open(path)
    img = img.convert(mode)
    img = img.resize((int(img.size[0]/resize_factor), int(img.size[1]/resize_factor)))
    if flip or flip == 1:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img = img.rotate(randint(rotations[0], rotations[1]))
    return img, pos

characters = (r"Images\\penguin.jpg", r"Images\\owl.png")
drip = ((r"Images\\thumb.png", 3, (-50, 200)), (r"Images\\hat2.png", 2, (90, -150)))
rotations = (-20, 20)

char_img = converter(choice(characters), (624, 626), "RGBA")

two_drip = randint(0, 1)
equiped_drip = []
if two_drip == 0:
    for item in drip:
        equiped_drip.append(create_drip(item[0], "RGBA", item[1], item[2], rotations, randint(0, 1)))
else:
    item = choice(drip)
    equiped_drip.append(create_drip(item[0], "RGBA", item[1], item[2], rotations, randint(0, 1)))


# create image
new_img = Image.new("RGBA", (624, 626), "white")

new_img.paste(char_img, (0, 0))

for dripies in equiped_drip:
    new_img.paste(dripies[0], dripies[1], dripies[0])

new_img.save("junk\\test.png", format="Png")