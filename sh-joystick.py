from sense_hat import SenseHat
sense = SenseHat()


while True:
    for event in sense.stick.get_events():
        # Prints the response of event.direction and event.action
        # for each event in the joystic
        print("Direction: " + event.direction +
              " & " + "Action: " + event.action)
