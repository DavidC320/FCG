from PIL import Image, ImageFilter, ImageColor

def stuff():
    img1 = Image.open(r"Images\\penguin.jpg")
    print(img1.size)
    if img1.mode != "RGBA":
        img1 = img1.convert("RGBA")

    img2 = Image.open(r"Images\\hat3.png")
    img_clone = img2
    print(img2.size)
    if img2.mode != "RGBA":
        img2 = img2.convert("RGBA")
    img2 = img2.resize(img1.size)
    print(img2.size)

    intermediate = Image.alpha_composite(img1, img2)

    final = Image.alpha_composite(intermediate, img2)

    final.save("junk\\final.png")

    # lets back up a bit
    img2 = Image.open(r"Images\\hat3.png")
    img_clone = img2
    new_img = Image.new("RGBA", (624, 626), "white")

    new_img.paste(img1, (0,0))
    img_clone = img_clone.resize((int(920/3), int(668/3)))

    new_img.paste(img_clone, (150, -50))

    new_img.save("junk\\again.png", "png")

    # owl time
    img2 = Image.open(r"Images\\hat3.png")

    owl_img = Image.open(r"Images\\owl.png")
    owl_img = owl_img.resize(img1.size)

    thumb_img = Image.open(r"Images\\thumbsup2.png")
    thumb_img = thumb_img.resize((int(thumb_img.size[0]/3), int(thumb_img.size[1]/3)))
    thumb_img = thumb_img.convert("RGBA")

    new_img = Image.new("RGBA", (624, 626), "white")

    new_img.paste(owl_img, (0, 0))

    new_img.paste(thumb_img, (-50, 200))

    new_img.save("junk\\plunk.png")

stuff()

pfp = Image.open(r"Images\\PFP.png")
pfp = pfp.filter(ImageFilter.UnsharpMask())
print(pfp.mode)

color = ImageColor.getcolor("Gold", "RGBA")
print(color)

data = pfp.getdata()

new_image = []

for item in data:
        if item[0] in list(range(200, 256)):
            new_image.append((255, 215, 0, 255))

        elif item[0] in list(range(150, 200)):
            new_image.append((255-50, 215-50, 0, 255))

        elif item[0] in list(range(100, 150)):
            new_image.append((255-100, 215-100, 0, 255))

        elif item[0] in list(range(80, 100)):
            new_image.append((255-150, 215-150, 0, 255))

        else:
            new_image.append(item)

pfp.putdata(new_image)


pfp.save("junk\\puk.png")