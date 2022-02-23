#!/usr/bin/env python

import pygame
import time
from gpiozero import Button
import neopixel
import board

# Set buttons

button1 = Button(14)
button2 = Button(23)
button3 = Button(25) # Reset button

# Set buzzer sound

buzzer1audio = "buzzer.mp3"
buzzer2audio = "buzzer.mp3"

# Get music playback ready

pygame.mixer.init
pygame.mixer.music.set_volume(1.0)

# LED strips configuration:
LED_1_COUNT   = 5       # Number of LED pixels
LED_1_BRIGHTNESS = 128  # LED brightness
LED_1_PIN = board.D15   # Pin for this strip
LED_1_ORDER  = neopixel.GRB # order of LED colours. May also be RGB, GRBW, or RGBW

LED_2_COUNT   = 5       # Number of LED pixels
LED_2_BRIGHTNESS = 128  # LED brightness
LED_2_PIN = board.D24   # Pin for this strip
LED_2_ORDER  = neopixel.GRB # order of LED colours. May also be RGB, GRBW, or RGBW

# LED colours

box_on = (255,255,255)
box_answer = (0, 255, 0)
box_off = (0, 0, 0)

# Set strips

strip1 = neopixel.NeoPixel(LED_1_PIN, LED_1_COUNT, brightness = LED_1_BRIGHTNESS, auto_write=False, pixel_order = LED_1_ORDER)
strip2 = neopixel.NeoPixel(LED_2_PIN, LED_2_COUNT, brightness = LED_2_BRIGHTNESS, auto_write=False, pixel_order = LED_2_ORDER)

# Initalise the library (must be called once before 
# other functions)

strip1.begin()
strip2.begin()

# Function to control colour change

def buzz_in(active_strip):
    if active_strip == 1:
        pygame.mixer.music.load(buzzer1)
        pygame.mixer.music.play()
        for i in range (strip2.numPixels()):
            strip2.setPixelColor(i, box_off)
            strip2.show()
        for i in range(strip1.numPixels()):
            strip1.setPixelColor(i, box_answer)
            strip1.show()
            time.sleep(0.2)
        button3.wait_for_press()
        time.sleep(0.5)
        for i in range (strip1.numPixels()):
            strip1.setPixelColor(i, box_on)
            strip1.show()
        for i in range(strip2.numPixels()):
            strip2.setPixelColor(i, box_on)
            strip2.show()
    if active_strip == 2:
        pygame.mixer.music.load(buzzer2)
        pygame.mixer.music.play()
        for i in range (strip1.numPixels()):
            strip1.setPixelColor(i, box_off)
            strip1.show()
        for i in range(strip2.numPixels()):
            strip2.setPixelColor(i, box_answer)
            strip2.show()
            time.sleep(0.2)
        button3.wait_for_press()
        time.sleep(0.5)
        for i in range (strip1.numPixels()):
            strip1.setPixelColor(i, box_on)
            strip1.show()
        for i in range(strip2.numPixels()):
            strip2.setPixelColor(i, box_on)
            strip2.show()

for i in range (strip1.numPixels()):
    strip1.setPixelColor(i, box_on)
    strip1.show()
for i in range(strip2.numPixels()):
    strip2.setPixelColor(i, box_on)
    strip2.show()

# Main loop

while True:
    # Turn on the LEDs on the boxes
    
    button1.when_pressed = buzz_in(1)
    button2.when_pressed = buzz_in(2)