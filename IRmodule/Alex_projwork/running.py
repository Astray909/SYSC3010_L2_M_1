import RPi.GPIO as IO
import time
from Parking import ParkingLot
from Parking import ParkingSpot
from TS import thingspeak_post

key = "UPJ636UNXXEE2IIG"

def spotIO(ParkingSpot):
    IO.setup(ParkingSpot.GPIOnum,IO.IN)

def detectCar(ParkingSpot, ParkingLot): #General function to detect and update cars in parking spots
    if(IO.input(ParkingSpot.GPIOnum) == True and ParkingSpot.state == True):
        #if(ParkingSpot.state == True):
        ParkingLot.spotOpened(ParkingSpot)
        #ParkingLot.FloorSpots[ParkingSpot.FloorID - 1] = ParkingLot.FloorSpots[ParkingSpot.FloorID - 1] + 1
        ParkingSpot.state = False
        thingspeak_post(ParkingLot.LotID, ParkingSpot.FloorID, ParkingLot.FloorSpots[ParkingSpot.FloorID - 1], ParkingSpot.SpotID, ParkingSpot.state, key)    


    elif(IO.input(ParkingSpot.GPIOnum) == False and ParkingSpot.state == False):
        #if(ParkingSpot.state == False):
        ParkingLot.spotTaken(ParkingSpot)
        #ParkingLot.FloorSpots[ParkingSpot.FloorID - 1] = ParkingLot.FloorSpots[ParkingSpot.FloorID - 1] - 1
        ParkingSpot.state = True    
        thingspeak_post(ParkingLot.LotID, ParkingSpot.FloorID, ParkingLot.FloorSpots[ParkingSpot.FloorID - 1], ParkingSpot.SpotID, ParkingSpot.state, key)

# IO init

IO.setwarnings(False) #ignore warnings
IO.setmode(IO.BCM) #to address pins as ints
spotList = []

# Instantiate spots here

spot1 = ParkingSpot(1, 1, 1, False, 18)
spotList.append(spot1)

spot2 = ParkingSpot(1, 1, 2, False, 23)
spotList.append(spot2)

spot3 = ParkingSpot(1, 2, 1, False, 24)
spotList.append(spot3)

spot4 = ParkingSpot(1, 2, 2, False, 4)
spotList.append(spot4)

# Init LotSpots here

lot1spots = [2, 2]

# Instantiate lots

lot1 = ParkingLot(1, lot1spots)

# Connect spots as inputs

while(len(spotList) > 0):
    spotIO(spotList.pop())

# Displaying lotspots initially

#lot1 spots
thingspeak_post(lot1.LotID, 1, lot1.FloorSpots[0], 0, False, key)
time.sleep(1)
thingspeak_post(lot1.LotID, 2, lot1.FloorSpots[1], 0, False, key)
time.sleep(1)

# polling the spots    

while(1):

    # detectCar funcs with the spots
    detectCar(spot1, lot1)

    time.sleep(1) # update every 1 s

    detectCar(spot2, lot1)

    time.sleep(1) # update every 1 s

    detectCar(spot3, lot1)

    time.sleep(1) # update every 1 s

    detectCar(spot4, lot1)

    time.sleep(1) # update every 1 s
    