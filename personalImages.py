import os


def pullPersonalPictures():
    l = os.listdir("static/Images/personal/")

    out = []
    for el in l:
        out.append("Images/personal/" + el)

    return out
