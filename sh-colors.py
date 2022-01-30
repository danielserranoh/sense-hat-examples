from sense_hat import SenseHat
sense = SenseHat()

r = 255
g = 255
b = 255

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
pink = (255, 0, 255)


sense.show_message("Akane", scroll_speed=0.1,
                   text_colour=pink, back_colour=white)
sense.clear(blue)
