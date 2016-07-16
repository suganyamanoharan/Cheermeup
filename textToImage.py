from PIL import Image, ImageDraw, ImageFont
import textwrap
import random

def textToImage(astr):
    para = textwrap.wrap(astr, width=23)
    num = random.randint(1,4)
    im = Image.open("static/Images//"+str(num)+".jpg")
    MAX_W , MAX_H = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(
        'Pacifico.ttf', 50)

    current_h, pad = 110, 10
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w) / 2, (current_h)), line, font=font)
        current_h += h + pad

    name = random.randint(1,1000000)
    im.save('static/Images/personal/' + str(name)+'.png')
