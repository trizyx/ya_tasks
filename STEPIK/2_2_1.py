from PIL import Image, ImageDraw, ImageFont


def target(file_name, side):

    img = Image.new('RGB', (side, side), 'white')
    im = ImageDraw.Draw(img)
    im.ellipse((int(0.2 * side), int(0.2 * side), int(0.8 * side), int(0.8 * side)),
               outline='black', width=int(0.01 * side))
    im.line((int(0.5 * side), int(0.1 * side), int(0.5 * side), int(0.4 * side)), fill='black', width=1)
    im.line((int(0.5 * side), int(0.6 * side), int(0.5 * side), int(0.9 * side)), fill='black', width=1)
    im.line((int(0.1 * side), int(0.5 * side), int(0.4 * side), int(0.5 * side)), fill='black', width=1)
    im.line((int(0.6 * side), int(0.5 * side), int(0.9 * side), int(0.5 * side)), fill='black', width=1)

    img.save(file_name)
