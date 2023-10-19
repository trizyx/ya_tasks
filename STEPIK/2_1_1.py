from PIL import Image, ImageDraw

img = Image.new('RGB', (200, 200), 'white')
im = ImageDraw.Draw(img)
im.line((200, 0, 0, 200), fill="#00FF00", width=3)
img.save('res.png')
