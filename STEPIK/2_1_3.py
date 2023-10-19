from PIL import Image, ImageDraw


def draw_circle(x, y):
    r = 10
    img = Image.new('RGB', (150, 150), 'white')
    im = ImageDraw.Draw(img)
    im.ellipse((x - r, y - r, x + r, y + r), width=2, outline='#0000FF')
    img.save('res.png')
