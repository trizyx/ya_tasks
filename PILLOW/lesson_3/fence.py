from PIL import Image, ImageDraw
color = input()


def fence(paint):
    img = Image.open("flowers.png")
    im = ImageDraw.Draw(img)
    x = 0
    while x <= img.size[0]:
        im.rectangle((x, 480, x + 30, 600), fill=paint)
        x += 50

    img.save('fence.png')


fence(color)
