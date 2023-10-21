from PIL import Image, ImageDraw

def horizontal_blue_gradient(size=256):
    img = Image.new('RGB', (size, 100), 'white')
    im = ImageDraw.Draw(img)
    width_counter = 0
    r = 0
    g = 0
    b = 0
    while b <= 255 and width_counter <= size:
        im.line((width_counter, 0, width_counter+1, 200), fill=(r, g, int(b)), width=1)
        width_counter += 1
        b += 255/size
    img.save('horizontal_blue_gradient.png')
