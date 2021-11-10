from flask import Flask
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
  25: 'vingt-cinq',
  35: 'vingt-cinq',
  30: 'demie',
}

def get_words():
  words = []

  words.append('il')
  words.append('est')

  now = datetime.datetime.now()
  hours = now.hour
  minutes = now.minute - (now.minute % 5)

  # 24h to 12h format
  if hours > 12:
    hours -= 12

  # Handle specific case when we want to display hours minus minutes
  if minutes >= 35:
    hours += 1
  
  # Display hour text
  words.append(WORDS_HOURS[hours])
  
  if hours == 1:
    words.append('heure')
  elif hours != 0 or hours != 12:
    words.append('heures')

  # Display minus or plus or nothing
  if minutes == 0:
    pass
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


@app.route('/')
def hello():
  words = get_words()

  for word in words:
    power_on_word(word)

  return ' '.join(words)


@app.route('/time')
def time():
  return str(datetime.datetime.now())

if __name__ == '__main__':
  app.run(host='::', port=8000, debug=True)