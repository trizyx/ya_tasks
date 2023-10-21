from PIL import Image, ImageDraw

def draw_grad():
    img = Image.new('RGB', (100, 100), 'white')
    im = ImageDraw.Draw(img)
    width_counter = 0
    r = 0
    g = 0
    b = 0
    while g <= 255 and width_counter <= 100:
        im.line((width_counter, 0, width_counter+1, 200), fill=(r, int(g), b), width=1)
        width_counter += 1
        g += 2.55
    img.save('horizontal_green_gradient.png')

draw_grad()
