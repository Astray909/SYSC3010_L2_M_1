import RPi.GPIO as IO
import time

IO.setwarnings(False) #ignore warnings
IO.setmode (IO.BCM) #to address pins as ints

IO.setup(18,IO.IN) #GPIO 18 -> IR sensor as input

while 1:
    print(IO.input(18))
    time.sleep(5)
    