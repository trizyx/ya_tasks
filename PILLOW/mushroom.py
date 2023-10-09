from PIL import Image, ImageDraw
background_rgb = list(map(int, input().split()))
cell_size = int(input())
width = 20 * cell_size
height = 22 * cell_size
image = Image.new('RGB', (width, height), (background_rgb[0], background_rgb[1], background_rgb[2]))


def show(img, size, rgb):
    # Create drawing object
    im = ImageDraw.Draw(img)
    im.ellipse((7 * size, 7 * size, 13 * size, 21 * size), fill=(255, 250, 235))
    im.rectangle((3 * size, 19 * size, 17 * size, 20 * size), fill=(146, 208, 80))
    im.rectangle((0, 20 * size, 20 * size, 22 * size), fill=(rgb[0], rgb[1], rgb[2]))
    im.pieslice(((3 * size, 3 * size), (17 * size, 17 * size)), 180, 0, fill=(192, 0, 0), width=1)
    im.ellipse((5 * size, 7 * size, 7 * size, 9 * size), fill=(255, 255, 255))
    im.ellipse((9 * size, 4 * size, 11 * size, 6 * size), fill=(255, 255, 255))
    im.ellipse((13 * size, 7 * size, 15 * size, 9 * size), fill=(255, 255, 255))
    # Save image
    img.save('mushroom.png')


show(image, cell_size, background_rgb)
