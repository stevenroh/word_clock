import threading
import os
import board
import neopixel
import time
from clock import Clock
from constants import COMMANDS
from animations import colors
from animations import *
from utils import get_fixed_led_id

INVALID_TASK = "Invalid task"
LEDS_PIN = board.D18
NUM_PIXELS = 110
BRIGHTNESS = 1
ORDER = neopixel.GRB

class HWIOTUtils():
  def __init__(self):
    self.playing_animation = False
    self.pixels = neopixel.NeoPixel(
      LEDS_PIN, NUM_PIXELS, brightness=BRIGHTNESS, auto_write=False, pixel_order=ORDER
    )

    self.power_off_all()

    for i in range(NUM_PIXELS):
      self.power_on_led(i, colors.WHITE)
      time.sleep(0.01)
    
    threading.Timer(5.0, self.update_hw).start()

  def update_hw(self):  
    if not self.playing_animation:
      print("update_hw")
      words = Clock().get_words()
      leds_on = Clock().get_leds_for_words(words)

      print(words)

      self.power_off_all()
      self.power_on_leds(leds_on, colors.WHITE)

  def power_off_all(self):
    self.pixels.fill(colors.OFF)
    self.pixels.show()

  def execute_if_valid(self, task):
    command = COMMANDS.get(task, INVALID_TASK)

    if command is not INVALID_TASK:
        os.system(command)
        return True

    return False

  def set_animation_playing(self, status):
    self.playing_animation = status

  def set_animation(self, animation, speed):
    self.playing_animation = True
    animation_length = len(animation)

    for step in range(animation_length):
      leds = [item for sublist in animation[step] for item in sublist]
      print(leds)

      for idx, val in enumerate(leds):
        print(val)
        self.power_on_led(get_fixed_led_id(idx), val)
      
      time.sleep(speed)

    self.playing_animation = False

  def power_on_led(self, led, color):
    self.pixels[led] = color
    self.pixels.show()

  def power_on_leds(self, leds_arr, color):
    for led in leds_arr:
      self.power_on_led(led, color)
