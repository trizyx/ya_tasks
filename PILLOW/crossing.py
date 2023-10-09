from PIL import Image, ImageDraw

width, height, line_width = map(int, input().split())
image = Image.new('RGB', (width, height), 'white')


def show(img, wid, heigh, s):
    # Create drawing object
    im = ImageDraw.Draw(img)
    x_counter = 0
    while x_counter <= wid:
        # Draw white rectangle
        im.rectangle((x_counter, 0, x_counter + s, heigh), fill='white')
        x_counter += s
        # Draw black rectangle
        im.rectangle((x_counter, 0, x_counter + (s // 4), heigh), fill='black')
        # Draw orange rectangle
        im.rectangle((x_counter + (s // 4), 0, x_counter + (s + s // 4), heigh), fill=(255, 192, 0))
        # Draw black rectangle
        im.rectangle((x_counter + (s + s // 4), 0, x_counter + (s + s // 4 * 2), heigh), fill='black')
        x_counter += s // 4 * 2 + s

    img.save('crossing.png')


show(image, width, height, line_width)
