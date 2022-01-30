from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
num = randint(0, 10)

red = (255, 0, 0)
pink = (255, 0, 255)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
green = (0, 255, 0)
white = (255, 255, 255)
grey = (80, 80, 80)
dark_grey = (40, 40, 40)


name = "Akane"

# for i = 1 to name.length

# Generate a random colour


def pick_random_colour():
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)
    return (random_red, random_green, random_blue)


sense.show_letter("J", text_colour=pick_random_colour(),
                  back_colour=red)
sleep(0.6)
sense.show_letter("a", text_colour=pick_random_colour(),
                  back_colour=white)
sleep(0.6)
sense.show_letter("i", text_colour=pick_random_colour(),
                  back_colour=red)
sleep(0.6)
sense.show_letter("m", text_colour=pick_random_colour(),
                  back_colour=white)
sleep(0.6)
sense.show_letter("e", text_colour=pick_random_colour(),
                  back_colour=red)
sleep(0.6)
sense.show_letter(".", text_colour=pick_random_colour(),
                  back_colour=pick_random_colour())
sleep(1)
sense.clear()
