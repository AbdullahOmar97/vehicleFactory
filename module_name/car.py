from .factory import Factory

class Car(Factory):
    def __init__(self, model_name, fuel_type, color, number_of_doors):
        self._number_of_wheels = 4
        self._model_name = model_name
        self._fuel_type = fuel_type
        self._color = color
        self._number_of_doors = number_of_doors
        Car.car_count += 1

    def create_vehicle(self):
        pass

    def change_model_name(self, model_name):
        self._model_name = model_name

    def change_fuel_type(self, fuel_type):
        if fuel_type in ['electric', 'petrol', 'diesel']:
            self._fuel_type = fuel_type
        else:
            raise ValueError("Invalid fuel type")

    def change_color(self, color):
        self._color = color

    def change_number_of_doors(self, number_of_doors):
        if number_of_doors in [2, 4]:
            self._number_of_doors = number_of_doors
        else:
            raise ValueError("Invalid number of doors")

    @classmethod
    def print_car_count(cls):
        print(f"Total cars created: {cls.car_count}")

    def __str__(self):
        return (f"Car(Model Name: {self._model_name}, Fuel Type: {self._fuel_type}, "
                f"Color: {self._color}, Number of Doors: {self._number_of_doors}, "
                f"Number of Wheels: {self._number_of_wheels})")
