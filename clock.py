import datetime
from constants import WORDS_HOURS, WORDS_MINUTES
from utils import prepare_matrix

class Clock():
  @staticmethod
  def get_words():
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

  @staticmethod
  def get_led_for_word(word, is_minutes):
    switcher = {
      'il': [108, 109],
      'est': [104, 105, 106],
      'une': [81, 82, 83],
      'deux': [99, 100, 101, 102],
      'trois': [88, 89, 90, 91, 92],
      'quatre': [93, 94, 95, 96, 97, 98],
      'cinq': [66, 67, 68, 69],
      'six': [70, 71, 72],
      'sept': [77, 78, 79, 80],
      'huit': [73, 74, 75, 76],
      'neuf': [84, 85, 86, 87],
      'dix': [61, 62, 63],
      'onze': [51, 52, 53, 54],
      'midi': [62, 63, 64, 65],
      'minuit': [55, 56, 57, 58, 59, 60],
      'heure': [45, 46, 47, 48, 49],
      'heures': [44, 45, 46, 47, 48, 49],
    }

    minutes_switcher = {
      'moins': [39, 40, 41, 42, 43],
      'et': [31, 32],
      'cinq': [12, 13, 14, 15],
      'dix': [33, 34, 35],
      'quart': [25, 26, 27, 28, 29],
      'vingt': [17, 18, 19, 20, 12],
      'vingt-cinq': [12, 13, 14, 15, 16, 17, 18, 19, 20],
      'demie': [3, 4, 5, 6, 7],
    }

    if is_minutes:
      return minutes_switcher.get(word, "Invalid word (minutes)")

    return switcher.get(word, "Invalid word")
  
  @staticmethod
  def get_leds_for_words(words):
    is_minutes = False
    leds_on = []

    for word in words:
      leds_on.extend(Clock().get_led_for_word(word, is_minutes))
      if "heure" in word: is_minutes = True
    
    prepared_leds_on = prepare_matrix(leds_on)

    return prepared_leds_on
