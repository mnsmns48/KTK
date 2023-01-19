from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

im = Image.open('app/font2.jpg')
today = datetime.now()
new_contract = ImageDraw.Draw(im)


def text_draw(word, width, height, font_size):
    font = ImageFont.truetype('app/arialmt.ttf', size=font_size)
    new_contract.text((width, height), str(word), font=font, fill='#000000')


text_draw(today.day, 1320, 1372, 58)
text_draw(today.month, 1555, 1372, 58)
text_draw(today.year, 1795, 1372, 58)

text_draw('Фамилия', 220, 446, 58)
text_draw('ГРИБОЕДОВ', 769, 2112, 58)
text_draw('НИКИТА', 220, 521, 58)
text_draw('СЕРГЕЕВИЧ', 220, 597, 58)

text_draw('3   2   4   5', 302, 925, 58)
text_draw('5   1   2   0   5   9', 302, 1000, 58)
text_draw('ФЕДЕРАЛЬНАЯ МИГРАЦИОННАЯ СЛУЖБА', 290, 1081, 25)
text_draw("  ".join('12 05 2015'), 75, 1198, 49)

text_draw('0   5           1   1          1   9   8   5', 75, 1324, 49)
text_draw('ГОРОД СИМФЕРОПОЛЬ, АВТОНОМНАЯ РЕСПУБЛИКА КРЫМ', 75, 1450, 25)

text_draw('+7(978)408-07-78', 1456, 103, 70)
text_draw('897013400000654398', 1456, 205, 70)
text_draw('Безлимитный интернет', 1651, 320, 58)

text_draw('Республика Крым', 1333, 522, 58)
text_draw('п. Ленино, ул. Молодёжная', 1333, 648, 58)
text_draw('32', 1345, 725, 58)
text_draw('17', 1914, 725, 58)

im.show()
