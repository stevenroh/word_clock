import datetime
from constants import WORDS_HOURS, WORDS_MINUTES

class Clock():
  def __init__(self, iot):
    self.iot = iot
    self.iot.init_gpio()


  def get_words(self):
    words = []

    words.append('il')
    words.append('est')

    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute - (now.minute % 5)

    # 24h to 12h
    if hours > 12:
        hours -= 12

    # Handle specific case when we want to display hours minus minutes
    if minutes >= 35:
        hours += 1

    # Display hour text
    words.append(WORDS_HOURS[hours])

    if hours == 1:
      words.append('heure')
    elif hours != 0 or hours != 12:  # No "hours" text for midnight
      words.append('heures')

    # Display minus or plus or nothing
    if minutes == 0:
      pass  # Display nothing
    elif minutes >= 35:
      words.append('moins')
      words.append(WORDS_MINUTES[minutes])
    else:
      if minutes == 15 or minutes == 30:
        words.append('et')
      words.append(WORDS_MINUTES[minutes])

    return words

  def get_led_for_word(self, word, is_minutes):
    switcher = {
      'il': [0, 1],
      'est': [3, 4, 5],
      'une': [26, 27, 28],
      'deux': [7, 8, 9, 10],
      'trois': [17, 18, 19, 20, 21],
      'quatre': [11, 12, 13, 14, 15, 16],
      'cinq': [40, 41, 42, 43],
      'six': [37, 38, 39],
      'sept': [29, 30, 31, 32],
      'huit': [33, 34, 35, 36],
      'neuf': [22, 23, 24, 25],
      'dix': [46, 47, 48],
      'onze': [55, 56, 57, 58],
      'midi': [44, 45, 46, 47],
      'minuit': [49, 50, 51, 52, 53, 54],
      'heure': [60, 61, 62, 63, 64],
      'heures': [60, 61, 62, 63, 64, 65],
    }

    minutes_switcher = {
      'moins': [66, 67, 68, 69, 70],
      'et': [77, 78],
      'cinq': [94, 95, 96, 97],
      'dix': [74, 75, 76],
      'quart': [80, 81, 82, 83, 84],
      'vingt': [88, 89, 90, 91, 92],
      'vingt-cinq': [88, 89, 90, 91, 92, 93, 94, 95, 96, 97],
      'demie': [102, 103, 104, 105, 106],
    }

    if is_minutes:
      return minutes_switcher.get(word, "Invalid word (minutes)")

    return switcher.get(word, "Invalid word")

  def get_leds_for_words(self, words):
    is_minutes = False
    leds_on = []

    for word in words:
      leds_on.extend(self.get_led_for_word(word, is_minutes))
      if "heure" in word: is_minutes = True
    
    return leds_on

  def power_on_leds(self, leds_arr):
    for led in leds_arr:
      self.iot.power_on_led(led)

