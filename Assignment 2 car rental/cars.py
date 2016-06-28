# Define a class for my car

class Car(object):
    # implement the car object.
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        self.engineSize = ''

    def getColour(self):
        return self.__colour

    def getMake(self):
        return self.__make

    def getMileage(self):
        return self.__mileage

    def setColour(self, colour):
        self.__colour = colour

    def setMake(self, make):
        self.__make = make

    def setMileage(self, mileage):
        self.__mileage = mileage

    def paint(self, colour):
        self.__colour = colour
        return self.__colour

    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage

class ElectricCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value

class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__fuelType = "Petrol"

    def getFuelType(self):
        return self.__fuelType
        
class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__fuelType = "Diesel"

    def getFuelType(self):
        return self.__fuelType
        
class HybridCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__fuelType = "Petrol"
        self.__numberFuelCells = 1

    def getFuelType(self):
        return self.__fuelType
        
    def setFuelType(self, value):
        self.__fuelType = value
        
    def getNumberFuelCells(self):
        return self.__numberFuelCells
    
    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value

