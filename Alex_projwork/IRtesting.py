import RPi.GPIO as IO
import time
import array as arr
from parkingLot import ParkingLot
from parkingSpot import ParkingSpot
import parkingSpot

IO.setwarnings(False) #ignore warnings
IO.setmode (IO.BCM) #to address pins as ints

lot1 = ParkingLot()
lot1.LotID = 1
lot1.FloorSpots = [1, 1, 1] #create a 

#Creating a parking spot that is initialized to be empty
spot1 = ParkingSpot()
spot1.LotID = 1
spot1.FloorID = 1
spot1.SpotID = 1
spot1.state = False #unoccupied

spot1 = IO.setup(18,IO.IN) #GPIO insertnum -> IR sensor as input

while 1:
    if(IO.input(18)==True): #car is far away
        print("No car detected")

    if(IO.input(18)==False): #car is close
        print("Car detected")

    time.sleep(5)    