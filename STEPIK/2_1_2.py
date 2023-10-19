from PIL import Image, ImageDraw

img = Image.new('RGB', (450, 300), 'white')
im = ImageDraw.Draw(img)
im.rectangle((0, 0, 450, 100), fill="#FFFFFF")
im.rectangle((0, 100, 450, 200), fill="#0000FF")
im.rectangle((0, 200, 450, 300), fill="#FF0000")
img.save('flag.png')
