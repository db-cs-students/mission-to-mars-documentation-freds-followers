# Mission-to-Mars-Documentation
## Name Of Team Sensor Payload - M.O.R.G.E.
What Does M.O.R.G.E stand for? - Mechanical Organic Rotating Giroscopic Entity
![Screenshot of Data](Datascreenshot.png)
![Images of M.O.R.G.E.](MORGEfront.jpg)
![Images of M.O.R.G.E.](MORGEback.jpg)
![Images of M.O.R.G.E.](MORGEmicroside.jpg)
![Images of M.O.R.G.E.](MORGEconnectionside.jpg)
![Images of M.O.R.G.E.](MORGEmicro_out.jpg)
Reciver Code:
```python
radio.set_group(99)
def on_received_value(name, value):
    serial.write_value(name, value)
radio.on_received_value(on_received_value)
```
