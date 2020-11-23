import unittest
from SW import ParkingLot
from SW import ParkingSpot


lot1spots = [1, 1, 1] # a parking lot with 3 floors each with one spot
lot1spots2 = [3, 3, 3]

lot2spots = [0, 1, 1] # a parking lot with first floor full and others with one spot
lot2spots2 = [2, 3, 3]
lot2spots3 = [3, 2, 3]
lot3spots = [0, 1, 1]
lot4spots = [0, 1, 1]
lot5spots = [0, 0, 1]



class TestCars(unittest.TestCase):
    
    def test_spotTaken(self): #1 car takes a spot on floor 1 in lot 1
        lot1 = ParkingLot(1, lot1spots)
        spot1 = ParkingSpot(1, 1, 1, False)
        spot1.state = True # Spot is taken here
        spots = lot1.spotTaken(spot1)

        self.assertEqual(spots, 0)


    def test_spotTaken2(self): #1 car takes a spot on floor 1 in a bigger sized lot 1
        lot1 = ParkingLot(1, lot1spots2)
        spot1 = ParkingSpot(1, 1, 1, False)
        spot1.state = True # Spot is taken here
        spots = lot1.spotTaken(spot1)

        self.assertEqual(spots, 2)

    def test_spotTaken3(self): #1 car takes a spot on floor 2 in lot 1
        lot1 = ParkingLot(1, lot1spots)
        spot1 = ParkingSpot(1, 2, 1, False)
        spot1.state = True # Spot is taken here
        spots = lot1.spotTaken(spot1)

        self.assertEqual(spots, 0)  

    def test_spotTaken4(self): #2 cars take up spots in lot 1
        lot1 = ParkingLot(1, lot1spots)
        spot1 = ParkingSpot(1, 1, 1, False)
        spot2 = ParkingSpot(1, 2, 1, False)
        spot1.state = True # Spot1 is taken here
        spot2.state = True # Spot2 is taken here
        spots1 = lot1.spotTaken(spot1)
        spots2 = lot1.spotTaken(spot2)

        self.assertEqual(spots1, spots2)        

    def test_spotTaken5(self): #2 cars take up spots in lot 1 and lot 2
        lot1 = ParkingLot(1, lot1spots)
        lot2 = ParkingLot(2, lot1spots)
        spot1 = ParkingSpot(1, 1, 1, False)
        spot2 = ParkingSpot(1, 1, 1, False)
        spot1.state = True # Spot1 is taken here
        spot2.state = True # Spot2 is taken here
        spots1 = lot1.spotTaken(spot1)
        spots2 = lot2.spotTaken(spot2)

        self.assertEqual(spots1, spots2)       

    def test_spotOpened(self): # 1 car vacates a spot on floor 1
        lot2 = ParkingLot(1, lot2spots)
        spot1 = ParkingSpot(1, 1, 1, True)
        spot1.state = False # Spot is vacated here
        spots = lot2.spotOpened(spot1)

        self.assertEqual(spots, 1)

    def test_spotOpened2(self): # 1 car vacates a spot on floor 1 of bigger parking lot
        lot2 = ParkingLot(1, lot2spots2)
        spot1 = ParkingSpot(1, 1, 1, True)
        spot1.state = False # Spot is vacated here
        spots = lot2.spotOpened(spot1)

        self.assertEqual(spots, 3)

    def test_spotOpened3(self): # 1 car vacates a spot on floor 2 of bigger parking lot
        lot2 = ParkingLot(1, lot2spots3)
        spot1 = ParkingSpot(1, 2, 1, True)
        spot1.state = False # Spot is vacated here
        spots = lot2.spotOpened(spot1)

        self.assertEqual(spots, 3)    

    def test_spotOpened4(self): # 2 cars vacate 2 spots on two floors of same lot
        lot2 = ParkingLot(1, lot5spots)
        spot1 = ParkingSpot(1, 1, 1, True)
        spot2 = ParkingSpot(1, 2, 1, True)
        spot1.state = False # Spot is vacated here
        spot2.state - False # Spot is vacated here
        spots1 = lot2.spotOpened(spot1)
        spots2 = lot2.spotOpened(spot2)

        self.assertEqual(spots1, spots2)

    def test_spotOpened5(self): # 2 vars vacate 2 spots in two separate lots
        lot1 = ParkingLot(1, lot3spots)
        lot2 = ParkingLot(2, lot4spots)
        spot1 = ParkingSpot(1, 1, 1, True)
        spot2 = ParkingSpot(2, 1, 1, True)
        spot1.state = False # Spot is vacated here
        spot2.state - False # Spot is vacated here
        spots1 = lot1.spotOpened(spot1)
        spots2 = lot2.spotOpened(spot2)

        self.assertEqual(spots1, spots2)

if __name__ == '__main__':
    unittest.main()
