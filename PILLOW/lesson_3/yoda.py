from PIL import Image
img = Image.open('yoda.png')
num = int(input())


def reduce_brightness(image, amount):
    x, y = image.size
    color_matrix = image.load()
    for rows in range(x):
        for cals in range(y):
            dig = (max(color_matrix[rows, cals]) - min(color_matrix[rows, cals])) // amount
            color_matrix[rows, cals] = tuple([i + dig for i in color_matrix[rows, cals]])

    image.save('sense.png')

    return image.show()


reduce_brightness(img, num)
