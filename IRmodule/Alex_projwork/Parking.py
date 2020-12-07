import time

# Class used to represent a parking lot
class ParkingLot:
    
    def __init__(self, LotID, FloorSpots):
        self.LotID = LotID
        self.FloorSpots = FloorSpots

    # Function for calculating floorspots if a spot is taken
    def spotTaken(self, ParkingSpot):
        if(self.LotID == ParkingSpot.LotID):
            self.FloorSpots[ParkingSpot.FloorID - 1] -= 1

    # Function for calculating floorspots if a spot is vacated
    def spotOpened(self, ParkingSpot):
        if(self.LotID == ParkingSpot.LotID):
            self.FloorSpots[ParkingSpot.FloorID - 1] += 1
            
# Class used to represnt a parking spot
class ParkingSpot:

    def __init__(self, LotID, FloorID, SpotID, state, GPIOnum):
        self.LotID = LotID
        self.FloorID = FloorID
        self.SpotID = SpotID
        self.state = state
        self.GPIOnum = GPIOnum






