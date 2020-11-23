import time

class ParkingLot:
    
    def __init__(self, LotID, FloorSpots):
        self.LotID = LotID
        self.FloorSpots = FloorSpots

    def spotTaken(self, ParkingSpot):
        self.FloorSpots[ParkingSpot.FloorID - 1] -= 1
        return self.FloorSpots[ParkingSpot.FloorID - 1]

    def spotOpened(self, ParkingSpot):
        self.FloorSpots[ParkingSpot.FloorID - 1] += 1
        return self.FloorSpots[ParkingSpot.FloorID - 1]

class ParkingSpot:

    def __init__(self, LotID, FloorID, SpotID, state):
        self.LotID = LotID
        self.FloorID = FloorID
        self.SpotID = SpotID
        self.state = state







