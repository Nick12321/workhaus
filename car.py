class Highway:

    def __init__(self, name):
        self.name = name
        self.eastbound = []
        self.westbound = []

    def addEastBoundCar(self, car):
        self.eastBound.append(car)

    def getEastBoundSpeedOfCarAtSpot(self, carSpot):
        return self.eastBound[carspot].getSpeed()

    def addWestBoundCar(self, car):
        self.westBound.append(car)

    def getWestBoundSpeedOfCarAtSpot(self, carSpot):
        return self.westBound[carSpot].getSpeed()

    def printCars(self, cars):
        for car in cars:
            car.printCarInfo()

    def printHighwayData(self):
        print("East Bound")
        self.printCars(self.eastBound)
        print("==============")
        print("West Bound")
        self.printCars(self.westBound)
