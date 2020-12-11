radio.set_group(99)
def on_forever():
    radio.send_value("x", input.acceleration(Dimension.X))
    radio.send_value("y", input.acceleration(Dimension.Y))
    radio.send_value("z", input.acceleration(Dimension.Z))
    pause(50)
basic.forever(on_forever)
