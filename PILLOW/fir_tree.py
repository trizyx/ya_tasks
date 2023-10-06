from PIL import Image, ImageDraw
num = int(input())
image = Image.new('RGB', (24 * num, 40 * num), 'white')


def show(s, img):
    # Create drawing object
    im = ImageDraw.Draw(img)
    # Draw green triangles
    im.polygon((2 * s, 32 * s, 22 * s, 32 * s, 12 * s, 16 * s), fill='#00b050')
    im.polygon((4 * s, 20 * s, 20 * s, 20 * s, 12 * s, 8 * s), fill='#00b050')
    im.polygon((6 * s, 11 * s, 12 * s, 3 * s, 18 * s, 11 * s), fill='#00b050')
    # Draw brown rectangle
    im.rectangle((10.5 * s, 32 * s, 13.5 * s, 36 * s), fill='#7f6000')
    # Save image
    img.save('fir_tree.png')
    

show(num, image)
