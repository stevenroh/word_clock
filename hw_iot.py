"Utils to communicate with Hardware"

import threading
import os
import board
import neopixel
import time

from numpy import ndarray

from clock import Clock

from constants import COMMANDS, UPDATE_TIME_SECONDS, NUM_PIXELS, BRIGHTNESS
from animations import colors
from animations import *

from utils import get_fixed_led_id

INVALID_TASK = "Invalid task"

LEDS_PIN = board.D18
ORDER = neopixel.GRB

class HWIOTUtils():
    "Utils to communicate with Hardware"

    def __init__(self):
        self.playing_animation = False
        self.last_content = None

        self.pixels = neopixel.NeoPixel(
            LEDS_PIN, NUM_PIXELS, brightness=BRIGHTNESS, auto_write=False, pixel_order=ORDER
        )

        self.power_off_all()

        for i in range(NUM_PIXELS):
            self.power_on_led(i, colors.WHITE)
            time.sleep(0.01)
        
        threading.Timer(UPDATE_TIME_SECONDS, self.update_hw).start()

    def update_hw(self): 
        "Update hardware state"
   
        if not self.playing_animation:
            print("Update HW")
            words = Clock().get_words()
    
            if self.last_content != words:
                self.last_content = words
                print("Update needed")
        
                leds_on = Clock().get_leds_for_words(words)

                self.power_off_all()
                self.power_on_leds(leds_on, colors.WHITE)
            else:
                print("No update needed")

        threading.Timer(UPDATE_TIME_SECONDS, self.update_hw).start()

    def power_off_all(self):
        "Power off all leds"
        self.pixels.fill(colors.OFF)
        self.pixels.show()

    def execute_if_valid(self, task):
        "Execute a comand if valid"

        command = COMMANDS.get(task, INVALID_TASK)

        if command is not INVALID_TASK:
            os.system(command)
            return True

        return False

    def set_animation_playing(self, status):
        "Return if animation is currently playing"

        self.playing_animation = status

    def set_animation(self, animation, speed):
        "Set the animation (and speed) to be played"

        self.playing_animation = True
        self.last_content = None
        animation_length = len(animation)

        for step in range(animation_length):        
            leds = [item for sublist in animation[step] for item in sublist]

            for idx, val in enumerate(leds):
                self.power_on_led(get_fixed_led_id(idx), val, update=False)
            
            self.pixels.show()
            time.sleep(speed)

            if self.playing_animation is False:
                return

        self.playing_animation = False

    def power_on_led(self, led, color, update=True):
        "Power on single led with a specific color"

        if(isinstance(color, ndarray)):
            print(color.shape)
            self.pixels[led] = (color[0], color[1], color[2])
        else:
            self.pixels[led] = color

        if update:
            self.pixels.show()

    def power_on_leds(self, leds_arr, color):
        "Power on leds with a specific color"

        for led in leds_arr:
            self.power_on_led(led, color)
