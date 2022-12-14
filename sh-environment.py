from sense_hat import SenseHat

sense = SenseHat()

sense.set_rotation(180)

# Sets teh color variables
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Gets the environmental readings and rounds them acordingly
pressure = round(sense.get_pressure(), 1)
print(pressure, 'mb')

temperature = round(sense.get_temperature(), 1)
print(temperature, 'ºC')
temp2 = round(sense.get_temperature_from_pressure(), 1)
print(temp2, 'ºC')

humidity = round(sense.get_humidity(), 0)
print(humidity, "%")
humidity_msg = "Humidity: " + str(humidity) + ' %'


# Formats the message to display
pressure_msg = "Pressure: " + str(pressure) + ("mb")

pressure_colour = white
if pressure > 1027:
    pressure_colour = blue
if pressure < 979:
    pressure_colour = red

# Clears the sense screen
sense.clear()

# Displays the pressure in the LED Matrix
sense.show_message("Pressure: ")
sense.show_message(str(pressure), text_colour=pressure_colour)
sense.show_message("mb")

bg = black
if humidity < 30:
    bg = red
if humidity > 60:
    bg = blue

sense.show_message(humidity_msg, back_colour=bg)

# Clears the sense screen
sense.clear()
