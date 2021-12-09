from flask import Flask, render_template, jsonify, request
import json
from observer import Publisher
from iot import IOTUtils
from clock import Clock

app = Flask(__name__)

pub = Publisher()
iot = IOTUtils("IOT utils")
clock = Clock("Clock")
pub.register(iot)
pub.register(clock)

@app.route('/')
def render():
  return render_template('clock.html')


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
