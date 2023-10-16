from PIL import Image
img = Image.open("jellyfish.png")
r_change = float(input())
g_change = float(input())
b_change = float(input())
color_list = [r_change, g_change, b_change]


def reduce_brightess(image, colors):
    x, y = image.size
    color_matrix = image.load()
    for rows in range(x):
        for cals in range(y):
            gray = int((colors[0] * color_matrix[rows, cals][0]) 
                       + (colors[1] * color_matrix[rows, cals][1]) 
                       + (colors[2] * color_matrix[rows, cals][2]))
            color_matrix[rows, cals] = (gray, gray, gray)

    image.save("gray_jelly.png")

    return image.show()


reduce_brightess(img, color_list)
