#!/usr/bin/python
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
pink = (255, 0, 255)
black = (0, 0, 0)


a = black
r = red
heart_pixels = [
    a, a, a, a, a, a, a, a,
    a, r, r, a, a, r, r, a,
    r, a, a, r, r, a, a, r,
    r, a, a, a, a, a, a, r,
    a, r, a, a, a, a, r, a,
    a, a, r, a, a, r, a, a,
    a, a, a, r, r, a, a, a,
    a, a, a, a, a, a, a, a
]
full_heart_pixels = [
    a, a, a, a, a, a, a, a,
    a, r, r, a, a, r, r, a,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    a, r, r, r, r, r, r, a,
    a, a, r, r, r, r, a, a,
    a, a, a, r, r, a, a, a,
    a, a, a, a, a, a, a, a
]
# Display these colours on the LED matrix
sense.set_pixels(heart_pixels)
sleep(2)
sense.show_message("Akane", scroll_speed=0.1,
                   text_colour=pink, back_colour=white)

for x in range(5):
    sense.set_pixels(heart_pixels)
    sleep(0.5)
    sense.set_pixels(full_heart_pixels)
    sleep(0.5)
