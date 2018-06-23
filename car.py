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

class Car:

    def __init__(self, colour, model, make):
        self.colour = colour
        self.model = model
        self.make = make
        self.speed = 0

    def setSpeed(self, newSpeed, speedUnit):
        if speedUnit == "mph":
            self.speed = self.convertMphToKmph(newSpeed)
        else:
            self.speed = newSpeed

    def getSpeed(self):
        return self.speed

    def convertMphToKmph(self, speedInMph):
        return int(round(speedInMph * 1.60934))

    def printCarInfo(self):
        print("Colour: " + self.colour + \
        ", Model: " + self.model + \
        ", Make: " + self.make + \
        ", Speed: " + str(self.getSpeed()) + "Km/h")

car1 = Car("Blue", "Rav4", "Toyota")
car2 = Car("White", "Model X", "Tesla")
car3 = Car("Red", "Corolla", "Toyota")
car4 = Car("Silver", "Accord", "Honda")
car5 = Car("Black", "Fusion", "Ford")

car1.setSpeed(100, "kmph")
car2.setSpeed(50, "mph")
car3.setSpeed(105, "kmph")
car4.setSpeed(60, "mph")
car5.setSpeed(110, "kmph")

highway = Highway("401")
highway.addEastBoundCar(car1)
highway.addEastBoundCar(car2)
highway.addEastBoundCar(car3)
highway.addWestBoundCar(car4)
highway.addWestBoundCar(car5)
