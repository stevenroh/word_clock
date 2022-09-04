from flask import Flask, render_template, jsonify, request
from hw_iot import HWIOTUtils
from clock import Clock
from animations import *

app = Flask(__name__)
hw_iot = HWIOTUtils()

@app.route('/')
def render_clock():
    "Show html clock"
    return render_template('clock.html')

@app.route('/settings')
def render_settings():
    "Show settings page"
    return render_template('settings.html')


@app.route('/programs')
def render_programs():
    "Show programs page"
    return render_template('programs.html')


@app.route('/text')
def render_text():
    "Show textual time using words"
    return " ".join(Clock().get_words())


@app.route('/execute')
def execute():
    "Execute a task if valid"
    task = request.args.get('task')
    return "ok" if hw_iot.execute_if_valid(task) else "ko"


@app.route('/clock_mode')
def set_clock_mode():
    "Set clock mode"
    hw_iot.set_animation_playing(False)
    return "ok"

@app.route('/show')
def show_animation():
    "Play specific animation"

    animation = request.args.get('animation')
    speed = float(request.args.get('speed'))
    param = request.args.get('param')

    if speed is None:
        speed = 0.2

    if animation == "blink":
        curr_animation = blink_animation

    if animation == "snake":
        curr_animation = snake_animation

    if animation == "fill":
        curr_animation = fill_animation

    if animation == "water":
        curr_animation = water_animation

    if animation == "water2":
        curr_animation = water2_animation

    if animation == "text":
        curr_animation = text_animation

    hw_iot.set_animation(curr_animation, speed)

    return "ok"


@app.route('/leds')
def leds_status():
    "Show leds status"

    words = Clock().get_words()
    leds_on = Clock().get_leds_for_words(words)
    return jsonify(leds_on)


if __name__ == '__main__':
    app.run(host='::', port=8000, debug=True)
