from PIL import Image, ImageOps

def vertical_reflection():
    img = Image.open('image.png')
    img = ImageOps.mirror(img)
    img.save('res.png')

vertical_reflection()
