from PIL import Image
img = Image.open('fruits.png')
queue = str(input())


def swap(image, order):
    x, y = image.size
    cherry = image.crop((0, 0, x // 2, y // 2))
    raspberry = image.crop((x // 2, 0, x, y // 2))
    melon = image.crop((0, y // 2, x // 2, y))
    plum = image.crop((x // 2, y // 2, x, y))

    cropped_images = {
        '1': [cherry, (0, 0, x // 2, y // 2)],
        '2': [raspberry, (x // 2, 0, x, y // 2)],
        '3': [melon, (0, y // 2, x // 2, y)],
        '4': [plum, (x // 2, y // 2, x, y)]
    }
    counter = "1"
    for i in order:
        print(cropped_images[counter][1])
        if i == "1":
            image.paste(cropped_images[i][0], cropped_images[counter][1])
        elif i == "2":
            image.paste(cropped_images[i][0], cropped_images[counter][1])
        elif i == "3":
            image.paste(cropped_images[i][0], cropped_images[counter][1])
        elif i == "4":
            image.paste(cropped_images[i][0], cropped_images[counter][1])

        counter = str(int(counter) + 1)

    image.save('cycle.png')

    return image.show()


swap(img, queue)
