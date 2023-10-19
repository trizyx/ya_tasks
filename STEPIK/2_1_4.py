from PIL import Image, ImageDraw


def draw_star(star_color="#FFFFFF", back_color="#000000"):
    img = Image.new('RGB', (100, 100), back_color)
    im = ImageDraw.Draw(img)
    im.polygon(((51, 13), (61, 42), (92, 45), (68, 63), (77, 93),
                (51, 77), (27, 93), (34, 63), (10, 45), (41, 42)), fill=star_color)
    img.save('star.png')
