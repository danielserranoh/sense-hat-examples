from sense_hat import SenseHat

sense = SenseHat()

# inicializa variables de color
r = (255, 0, 0)
k = (0, 0, 0)
# Set up where each colour will display
warning_screen = [
    r, r, r, r, r, r, r, r,
    r, r, k, r, r, r, r, r,
    r, k, k, r, r, r, r, r,
    k, k, k, k, k, k, k, k,
    k, k, k, k, k, k, k, k,
    r, k, k, r, r, r, r, r,
    r, r, k, r, r, r, r, r,
    r, r, r, r, r, r, r, r
]

#Setup Warning Limit
warning_g = 0.5

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = round(x, 1)
    y = round(y, 1)
    z = round(z, 1)

    # Prints to screen
    print("x={0}, y={1}, z={2}".format(x, y, z))

    if abs(x) > warning_g or abs(y) > warning_g or abs(z) > warning_g:
        sense.set_pixels(warning_screen)
        # Update the rotation of the display depending on which way up the Sense HAT is
        if x == -1:
            sense.set_rotation(180)
        elif y == 1:
            sense.set_rotation(90)
        elif y == -1:
            sense.set_rotation(270)
        else:
            sense.set_rotation(0)
    else:
        sense.clear()
