from constants import MATRIX_HEIGHT, MATRIX_WIDTH
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from animations.colors import OFF, RED
import os 

MARGIN = 0

path = os.path.dirname(__file__)

# font = ImageFont.truetype(os.path.join(path, "rainyhearts.ttf"))
# img = Image.new("RGB", (MATRIX_HEIGHT, 100))

img = Image.open(os.path.join(path, 'w.jpg'))

# d = ImageDraw.Draw(img)
# d.text((MARGIN, MARGIN), "Jessica", fill=RED, font=font)

# img.save('test.jpg')

data = np.asarray(img)
arr = np.transpose(data, (1, 0, 2))

print(arr)

text_animation = []
text_animation.append(arr)

"""text_animation = []

text_animation.append(
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
)
"""