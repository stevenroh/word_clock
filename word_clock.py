from flask import Flask, render_template, jsonify, request
from hw_iot import HWIOTUtils
from clock import Clock
from animations import *
from constants import ANIM_MODE, CLOCK_MODE

curr_mode = CLOCK_MODE
curr_animation = None
step = 0

app = Flask(__name__)
hw_iot = HWIOTUtils()

@app.route('/')
def render_clock():
  return render_template('clock.html')

@app.route('/settings')
def render_settings():
  return render_template('settings.html')


@app.route('/programs')
def render_programs():
  return render_template('programs.html')


@app.route('/text')
def render_text():
  return " ".join(Clock().get_words())


@app.route('/execute')
def execute():
  task = request.args.get('task')
  return "ok" if hw_iot.execute_if_valid(task) else "ko"


@app.route('/clock_mode')
def set_clock_mode():
  global curr_mode

  curr_mode = CLOCK_MODE
  return "ok"

@app.route('/show')
def show_animation():
  global curr_mode, curr_animation, step

  curr_mode = ANIM_MODE
  step = 0

  animation = request.args.get('animation')

  print(animation)

  if animation == "blink":
    curr_animation = blink_animation

  if animation == "snake":
    curr_animation = snake_animation

  return "ok"


@app.route('/leds')
def leds_status():
  global step, curr_animation

  if curr_mode == CLOCK_MODE:
    words = Clock().get_words()
    leds_on = Clock().get_leds_for_words(words)
  elif curr_mode == ANIM_MODE:
    leds_on = []

    print(curr_animation)

    if curr_animation is not None:
      leds_on = [item for sublist in curr_animation[step] for item in sublist]
      step += 1

      if step >= len(curr_animation):
        step = 0

  return jsonify({'mode': 'animation' if curr_mode == ANIM_MODE else 'time', 'leds': leds_on})


if __name__ == '__main__':
  app.run(host='::', port=8000, debug=True)
