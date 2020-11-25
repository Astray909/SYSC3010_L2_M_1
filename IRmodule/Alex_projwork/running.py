import RPi.GPIO as IO
import time
from Parking import ParkingLot
from Parking import ParkingSpot
from TS import thingspeak_post

key = "UPJ636UNXXEE2IIG"

def spotIO(ParkingSpot):
    IO.setup(ParkingSpot.GPIOnum,IO.IN)

def detectCar(ParkingSpot, ParkingLot): #General function to detect and update cars in parking spots
    if(IO.input(ParkingSpot.GPIOnum) == True):
        if(ParkingSpot.state == True):
            ParkingLot.FloorSpots[ParkingSpot.FloorID - 1] = ParkingLot.FloorSpots[ParkingSpot.FloorID - 1] + 1
            ParkingSpot.state = False
            thingspeak_post(ParkingLot.LotID, ParkingSpot.FloorID, ParkingLot.FloorSpots[ParkingSpot.FloorID - 1], ParkingSpot.SpotID, ParkingSpot.state, "UPJ636UNXXEE2IIG")    


    if(IO.input(ParkingSpot.GPIOnum) == False):
        if(ParkingSpot.state == False):
            ParkingLot.FloorSpots[ParkingSpot.self.FloorID - 1] = ParkingLot.FloorSpots[ParkingSpot.FloorID - 1] - 1
            ParkingSpot.state = True    
            thingspeak_post(ParkingLot.LotID, ParkingSpot.FloorID, ParkingLot.FloorSpots[ParkingSpot.FloorID - 1], ParkingSpot.SpotID, ParkingSpot.state, "UPJ636UNXXEE2IIG")

# IO init

IO.setwarnings(False) #ignore warnings
IO.setmode(IO.BCM) #to address pins as ints
spotList = []

# Instantiate spots here

spot1 = ParkingSpot(1, 1, 1, False, 18)
spotList.append(spot1)

# Init LotSpots here

lot1spots = [3, 3, 3]

# Instantiate lots

lot1 = ParkingLot(1, lot1spots)

# Connect spots as inputs

while(len(spotList) > 0):
    spotIO(spotList.pop())

# polling the spots    

while(1):

    # detectCar funcs with the spots
    detectCar(spot1, lot1)

    time.sleep(5) # update every 5 s
    