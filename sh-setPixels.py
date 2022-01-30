from sense_hat import SenseHat
from time import sleep

# declares the senseHat object
sense = SenseHat()
# Sets the orientation of the LED matrix
# 0 = hdmi downwards, 90 = SD downwards
sense.set_rotation(90)

# Define some colours
B = (102, 51, 0)
b = (0, 0, 255)
S = (205, 133, 63)
W = (255, 255, 255)
k = (0, 0, 0)
g = (0, 255, 0)

# Set up where each colour will display
creeper_pixels = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, k, k, g, g, k, k, g,
    g, k, k, g, g, k, k, g,
    g, g, g, k, k, g, g, g,
    g, g, k, k, k, k, g, g,
    g, g, k, k, k, k, g, g,
    g, g, k, g, g, k, g, g
]

# Display these colours on the LED matrix
sense.set_pixels(creeper_pixels)
sleep(2)
# Set up where each colour will display
steve_pixels = [
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, S, S, S, S, S, S, B,
    S, S, S, S, S, S, S, S,
    S, W, b, S, S, b, W, S,
    S, S, S, B, B, S, S, S,
    S, S, B, S, S, B, S, S,
    S, S, B, B, B, B, S, S
]

# Display these colours on the LED matrix
sense.set_pixels(steve_pixels)
sleep(2)

# Clears the LED Matrix
sense.clear()
