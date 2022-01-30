from sense_hat import SenseHat

sense = SenseHat()

# inicializa variables de color
red = (255, 0, 0)

# Display the letter J
# sense.show_letter("J")


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

  # Update the rotation of the display depending on which way up the Sense HAT is
    if x == -1:
        sense.set_rotation(180)
    elif y == 1:
        sense.set_rotation(90)
    elif y == -1:
        sense.set_rotation(270)
    else:
        sense.set_rotation(0)

    if abs(x) > 1.0 or abs(y) > 1.0 or abs(z) > 1.0:
        sense.set_pixel(0, 0, red)
    else:
        sense.clear()
