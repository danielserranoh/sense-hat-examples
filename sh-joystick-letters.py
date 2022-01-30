#!/usr/bin/python

from sense_hat import SenseHat
sense = SenseHat()


while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            print(event.action)
            if event.direction == "up":
                sense.show_letter("U", text_colour=(
                    255, 0, 0), back_colour=(60, 0, 0))
            elif event.direction == "down":
                sense.show_letter("D", text_colour=(
                    255, 0, 255), back_colour=(60, 0, 60))
            elif event.direction == "left":
                sense.show_letter("L", text_colour=(
                    0, 255, 0), back_colour=(0, 60, 0))
            elif event.direction == "right":
                sense.show_letter("R", text_colour=(
                    0, 0, 255), back_colour=(0, 0, 60))
            elif event.direction == "middle":
                sense.show_letter("M", text_colour=(
                    0, 0, 0), back_colour=(60, 60, 60))
