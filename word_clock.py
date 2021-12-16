from flask import Flask, render_template, jsonify, request
from iot import IOTUtils
from clock import Clock
from animations import *
from constants import ANIM_MODE, TIME_MODE

import json

curr_mode = TIME_MODE
curr_animation = None

app = Flask(__name__)

iot = IOTUtils()
clock = Clock()


@app.route('/')
def render_clock():
  return render_template('clock.html')


@app.route('/settings')
def render_settings():
  return render_template('settings.html')


@app.route('/animations')
def render_animations():
  return render_template('animations.html')


@app.route('/text')
def render_text():
  return " ".join(clock.get_words())


@app.route('/execute')
def execute():
  task = request.args.get('task')
  return "ok" if iot.execute_if_valid(task) else "ko"


@app.route('/show')
def show_animation():
  global curr_mode

  curr_mode = ANIM_MODE

  print(curr_mode)

  animation = request.args.get('animation')
  print("Apply " + animation)
  print(blink_animation)
  return "ok"


@app.route('/leds')
def leds_status():
  print(curr_mode)

  if curr_mode == TIME_MODE:
    words = clock.get_words()
    leds_on = clock.get_leds_for_words(words)
  elif curr_mode == ANIM_MODE:
    leds_on = [1, 2]

  return jsonify({'mode': 'animation' if curr_mode == ANIM_MODE else 'time', 'leds': leds_on})


if __name__ == '__main__':
  app.run(host='::', port=8000, debug=True)
