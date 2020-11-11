import RPi.GPIO as IO
import time
import array as arr
from parkingLot import ParkingLot
from parkingSpot import ParkingSpot
import parkingSpot

IO.setwarnings(False) #ignore warnings
IO.setmode (IO.BCM) #to address pins as ints

lot1spots = [1, 1, 1] #create a parking lot with 3 floors each with one spot
lot1 = ParkingLot(1, lot1spots)

#Creating a parking spot that is initialized to be empty
spot1 = ParkingSpot(1, 1, 1, False, 18)

spot1 = IO.setup(spot1.GPIOnum,IO.IN) #GPIO 18 -> IR sensor as input

while 1:
    if(IO.input(spot1.GPIOnum)==True): #car is far away
        print("No car detected")
        if(spot1.state == True)
            lot1.FloorSpots[spot1.FloorID - 1] = lot1.FloorSpots[spot1.FloorID - 1] + 1
        spot1.state = False
        print(lot1.FloorSpots[spot1.FloorID - 1])
        print(spot1.state)

    if(IO.input(spot1.GPIOnum)==False): #car is close
        print("Car detected")
        if(spot1.state == False)
            lot1.FloorSpots[spot1.FloorID - 1] = lot1.FloorSpots[spot1.FloorID - 1] - 1
        spot1.state = True
        print(lot1.FloorSpots[spot1.FloorID - 1])
        print(spot1.state)

    time.sleep(5)    