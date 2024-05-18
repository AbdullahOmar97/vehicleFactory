import unittest
from module_name.car import Car
from module_name.motorcycle import Motorcycle

class TestVehicleFactory(unittest.TestCase):
    def test_create_car(self):
        car = Car("Model S", "electric", "red", 4)
        self.assertEqual(car._model_name, "Model S")
        self.assertEqual(car._fuel_type, "electric")
        self.assertEqual(car._color, "red")
        self.assertEqual(car._number_of_doors, 4)

    def test_create_motorcycle(self):
        motorcycle = Motorcycle("Model X", "petrol")
        self.assertEqual(motorcycle._model_name, "Model X")
        self.assertEqual(motorcycle._fuel_type, "petrol")

    def test_change_car_attributes(self):
        car = Car("Model S", "electric", "red", 4)
        car.change_model_name("Model 3")
        car.change_fuel_type("diesel")
        car.change_color("blue")
        car.change_number_of_doors(2)
        self.assertEqual(car._model_name, "Model 3")
        self.assertEqual(car._fuel_type, "diesel")
        self.assertEqual(car._color, "blue")
        self.assertEqual(car._number_of_doors, 2)

    def test_change_motorcycle_attributes(self):
        motorcycle = Motorcycle("Model X", "petrol")
        motorcycle.change_model_name("Model Y")
        motorcycle.change_fuel_type("electric")
        self.assertEqual(motorcycle._model_name, "Model Y")
        self.assertEqual(motorcycle._fuel_type, "electric")

if __name__ == '__main__':
    unittest.main()
