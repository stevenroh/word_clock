"All the constants definined for this software"

UPDATE_TIME_SECONDS = 30
NUM_PIXELS = 110
BRIGHTNESS = 0.5
MATRIX_WIDTH = 11
MATRIX_HEIGHT = 10

WORDS_HOURS = {
  1: 'une',
  2: 'deux',
  3: 'trois',
  4: 'quatre',
  5: 'cinq',
  6: 'six',
  7: 'sept',
  8: 'huit',
  9: 'neuf',
  10: 'dix',
  11: 'onze',
  12: 'midi',
  0: 'minuit',
}

WORDS_MINUTES = {
  5: 'cinq',
  55: 'cinq',
  10: 'dix',
  50: 'dix',
  15: 'quart',
  45: 'quart',
  20: 'vingt',
  40: 'vingt',
  25: 'vingt-cinq', # h+25
  35: 'vingt-cinq', # h-25
  30: 'demie',
}

COMMANDS = {
  'poweroff': 'shutdown -h now',
  'reboot': 'reboot',
  'test': 'echo test > /tmp/test.txt',
}
