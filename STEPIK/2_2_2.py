from PIL import Image, ImageDraw


def sailboat(file_name, width, height, sky_color='#75BBFD',
            sea_color='#465efd', wood_color='#3f1702',
            sail_color='#ffffff', sun_color='#FFDB00'):
    img = Image.new('RGB', (width, height), sky_color)
    im = ImageDraw.Draw(img)
    im.rectangle((0, int(0.8 * height), width, height), fill=sea_color)    #SEA
    im.ellipse((int(-0.2 * width), int(-0.2 * height),
                int(0.2 * width), int(0.2 * height)), fill=sun_color)    #SUN

    im.ellipse((int(0.25 * width), int(0.4   * height),
                int(0.65 * width), int(0.7 * height)), fill=sail_color)
    
    im.ellipse((int(0.3 * width), int(0.4 * height),
                int(0.7 * width), int(0.7 * height)), fill=sky_color)

    im.rectangle((int(0.46 * width), int(0.4 * height),
                  int(0.48 * width), int(0.7 * height)), fill=wood_color)
    
    im.polygon(((int(0.2 * width), int(0.7 * height)),
                (int(0.35 * width), int(0.85 * height)),
                (int(0.6 * width), int(0.85 * height)),
                (int(0.65 * width), int(0.7 * height)),
                ), fill=wood_color)    #SAIL`S BASE

    img.save(file_name)
