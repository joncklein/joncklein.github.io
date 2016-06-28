import unittest

from cars import *

"""
red_car = Car()
print 'Colour ' + red_car.getColour()

red_car.paint('red')
print 'Colour ' + red_car.getColour()


print 'Engine Size ' + red_car.engineSize
red_car.engineSize = '3.9'
print 'Engine Size ' + red_car.engineSize
"""

# test the car functionality
class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()

    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())

    def test_car_make(self):
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())

    def test_car_colour(self):
        self.assertEqual('', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())
        
class TestElectricCar(unittest.TestCase):
    
    def setUp(self):
        self.electriccar = ElectricCar()
        
    def test_fuel_cells(self):
        self.assertEqual(1, self.electriccar.getNumberFuelCells())
        self.electriccar.setNumberFuelCells(4)
        self.assertEqual(4, self.electriccar.getNumberFuelCells())

class TestPetrolCar(unittest.TestCase):

    def setUp(self):
        self.petrolcar = PetrolCar()
        
    def test_fuel_type(self):
        self.assertEqual('Petrol', self.petrolcar.getFuelType())

class TestDieselCar(unittest.TestCase):

    def setUp(self):
        self.dieselcar = DieselCar()
        
    def test_fuel_type(self):
        self.assertEqual('Diesel', self.dieselcar.getFuelType())
        
class TestHybridCar(unittest.TestCase):

    def setUp(self):
        self.hybridcar = HybridCar()
        
    def test_fuel_type(self):
        self.assertEqual('Petrol', self.hybridcar.getFuelType())
        self.hybridcar.setFuelType('Diesel')
        self.assertEqual('Diesel', self.hybridcar.getFuelType())
        
    def test_fuel_cells(self):
        self.assertEqual(1, self.hybridcar.getNumberFuelCells())
        self.hybridcar.setNumberFuelCells(4)
        self.assertEqual(4, self.hybridcar.getNumberFuelCells()



if __name__ == '__main__':
    unittest.main()
