from PIL import Image, ImageDraw
width, height = map(int, input().split())
r, g, b = map(int, input().split())
image = Image.new('RGB', (width, height), 'white')


def show(img, wid, red, green, blue):
    # Create drawing object
    im = ImageDraw.Draw(img)
    counter = 0
    for _ in range(width // 2 + 10):
        if red >= 255 and green >= 255 and blue >= 255:
            # Save image
            img.save('sunrise.png')
        else:
            im.line((0, counter, wid, counter), fill=(red, green, blue), width=2)
            counter += 2
            red += 2
            green += 2
            blue += 2
        

show(image, width, r, g, b)
