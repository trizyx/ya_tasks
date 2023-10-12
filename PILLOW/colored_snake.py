from PIL import Image, ImageDraw
width = 400
l_rings = int(input())
height = 200 + 250 * l_rings + 130 * (l_rings - 1)
l_color = input()
r_color = input()
image = Image.new('RGB', (width, height), '#777')


def show(img, lefts_rings_am, color1, color2):
    y_counter = 100
    flag_right = lefts_rings_am - 1
    im = ImageDraw.Draw(img)
    for i in range(lefts_rings_am):
        if i == flag_right:
            im.arc((75, y_counter, 325, y_counter + 250), 90, -90, fill=str(color1), width=60)
        else:
            im.arc((75, y_counter, 325, y_counter + 250), 90, -90, fill=str(color1), width=60)
            im.arc((75, y_counter + 190, 325, y_counter + 440), -90, 90, fill=str(color2), width=60)
            y_counter += 380

    img.save('colored_snake.png')


show(image, l_rings, l_color, r_color)
