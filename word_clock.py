from flask import Flask, render_template, jsonify, request
from iot import IOTUtils
from clock import Clock
import json

app = Flask(__name__)

iot = IOTUtils()
clock = Clock()


@app.route('/')
def render_clock():
  return render_template('clock.html')


@app.route('/settings')
def render_settings():
  return render_template('settings.html')


@app.route('/text')
def render_text():
  return " ".join(clock.get_words())


@app.route('/execute')
def execute():
  task = request.args.get('task')
  return "ok" if iot.execute_if_valid(task) else "ko"


@app.route('/leds')
def leds_status():
  words = clock.get_words()
  leds_on = clock.get_leds_for_words(words)

  return jsonify(leds_on)


if __name__ == '__main__':
  app.run(host='::', port=8000, debug=True)
