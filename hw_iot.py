import threading
import os
import board
import neopixel
import time
from clock import Clock
from constants import COMMANDS
from animations import colors

INVALID_TASK = "Invalid task"
LEDS_PIN = board.D18
NUM_PIXELS = 110
BRIGHTNESS = 1
ORDER = neopixel.GRB

class HWIOTUtils():
  def __init__(self):
    self.pixels = neopixel.NeoPixel(
      LEDS_PIN, NUM_PIXELS, brightness=BRIGHTNESS, auto_write=False, pixel_order=ORDER
    )

    self.power_off_all()

    for i in range(NUM_PIXELS):
      self.power_on_led(i, colors.WHITE)
      time.sleep(0.01)
    
    threading.Timer(5.0, self.update_hw).start()

  def update_hw(self):
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

  def power_on_led(self, led, color):
    self.pixels[led] = color
    self.pixels.show()

  def power_on_leds(self, leds_arr, color):
    for led in leds_arr:
      self.power_on_led(led, color)
