from sense_hat import SenseHat
sense = SenseHat()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)

sense.clear()
sense.set_pixel(2, 2, blue)
sense.set_pixel(4, 2, blue)
sense.set_pixel(3, 4, (100, 0, 0))
sense.set_pixel(1, 5, red)
sense.set_pixel(2, 6, red)
sense.set_pixel(3, 6, red)
sense.set_pixel(4, 6, red)
sense.set_pixel(5, 5, red)
