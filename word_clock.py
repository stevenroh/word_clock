from flask import Flask, render_template, jsonify
import json
import datetime

app = Flask(__name__)

WORDS_HOURS = {
  1: 'un',
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
  elif hours != 0 or hours != 12: # No "hours" text for midnight
    words.append('heures')

  # Display minus or plus or nothing
  if minutes == 0:
    pass # Display nothing
  elif minutes >= 35:
    words.append('moins')
    words.append(WORDS_MINUTES[minutes])
  else:
    if minutes == 15:
      words.append('et')
    words.append(WORDS_MINUTES[minutes])

  return words


def power_on_word(word):
  print(f'Power ON : {word}')

def leds_for_word(word):
  switcher = {
    'il': [0, 1],
    'est': [3, 4, 5],
    'un': [-99],
    'deux': [-99],
    'trois': [-99],
    'quatre': [-99],
    'cinq': [-99],
    'six': [-99],
    'sept': [-99],
    'huit': [-99],
    'neuf': [-99],
    'dix': [-99],
    'onze': [-99],
    'midi': [-99],
    'minuit': [-99],
    'cinq': [-99],
    'dix': [-99],
    'quart': [-99],
    'vingt': [-99],
    'vingt-cinq': [-99],
    'demie': [-99],
    'moins': [-99],
    'et': [-99],
    'heure': [-99],
    'heures': [-99],
  }
  return switcher.get(word, "Invalid word")


@app.route('/')
def hello():
  words = get_words()

  for word in words:
    power_on_word(word)

  return ' '.join(words)


@app.route('/time')
def time():
  return str(datetime.datetime.now())


@app.route('/leds')
def leds_status():
  words = get_words()
  leds_on = []

  for word in words:
    leds_on.extend(leds_for_word(word))

  return jsonify(leds_on)

@app.route('/clock')
def clock():
  return render_template('clock.html')


if __name__ == '__main__':
  app.run(host='::', port=8000, debug=True)