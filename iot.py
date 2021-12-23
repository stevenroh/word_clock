from constants import COMMANDS
import os
import board
import neopixel

INVALID_TASK = "Invalid task"
LEDS_PIN = board.D18
NUM_PIXELS = 110
BRIGHTNESS = 1
ORDER = neopixel.RGB

class IOTUtils():
  def __init__(self):
    self.pixels = neopixel.NeoPixel(
      LEDS_PIN, NUM_PIXELS, brightness=BRIGHTNESS, auto_write=False, pixel_order=ORDER
    )

  def execute_if_valid(self, task):
    command = COMMANDS.get(task, INVALID_TASK)

    if command is not INVALID_TASK:
        os.system(command)
        return True

    return False

  def power_on_led(self, led):
    self.pixels[led] = (255, 0, 0)
    self.pixels.show()