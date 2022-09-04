from constants import MATRIX_HEIGHT, MATRIX_WIDTH
from PIL import Image, ImageDraw, ImageFont
from numpy import asarray
import os 

MARGIN = 1

path = os.path.dirname(__file__)

#font = ImageFont.truetype(os.path.join(path, "rainyhearts.ttf"))
#img = Image.new('', (MATRIX_HEIGHT, 100))

img = Image.open(os.path.join(path, 'w.jpg'))

#d = ImageDraw.Draw(img)
#d.text((MARGIN, MARGIN), "Jessica", fill=(255,0,0), font=font)

# img.save('test.jpg')

data = asarray(img)

print(data)

print(data.shape)
text_animation = []

text_animation.append(data)
""" text_animation.append(
    [
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
        [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
    ]
) """
