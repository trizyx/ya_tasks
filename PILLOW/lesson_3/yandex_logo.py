from PIL import Image
img = Image.open("yandex_logo.png")
color = str(input())


def change_color(image, color_to_change):
    x, y = image.size
    flag = False
    color_matrix = image.load()
    if color_to_change == "black":
        for rows in range(x):
            for cals in range(y):
                if color_matrix[rows, cals] == (255, 0, 0):
                    color_matrix[rows, cals] = (0, 0, 0)

    elif color_to_change == "red":
        if image.getpixel((207, 222)) == (255, 0, 0):
            flag = True
        elif image.getpixel((207, 222)) == (0, 0, 0):
            flag = False
        for rows in range(x):
            for cals in range(y):
                if flag:
                    if color_matrix[rows, cals] == (0, 0, 0):
                        color_matrix[rows, cals] = (255, 0, 0)
                elif not flag:
                    if color_matrix[rows, cals] == (255, 0, 0):
                        color_matrix[rows, cals] = (0, 0, 0)
    
    image.save("ready.png")

    return image.show()


change_color(img, color)
