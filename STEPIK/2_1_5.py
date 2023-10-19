from PIL import Image, ImageDraw, ImageFont
rocket1 = r"""      /\
    / () \
    (CCCP)
    (    )
   /|/||\|\
  /_/|VV|\_\
"""


def ascii_art(size_x=120, size_y=100, top_indent=10, left_margin_count=10, left_margin_image=42,
          back_color="#FFFFFF", count_color="#000000", rocket_color="#000000",
          count_start=5, count_finish="CTAPT", ascii_image=rocket1):

    img = Image.new('RGB', (size_x, size_y), back_color)
    font = ImageFont.load_default()
    im = ImageDraw.Draw(img)
    top_indent2 = top_indent
    im.text((left_margin_image, top_indent), text=ascii_image, font=font, fill=rocket_color)
    while count_start != 0:
        im.text((left_margin_count, top_indent2), text=str(count_start), font=font, fill=count_color)
        top_indent2 += 15
        count_start -= 1

    im.text((left_margin_count, top_indent2), count_finish, font=font, fill=count_color)
    img.save('rocket.png')
