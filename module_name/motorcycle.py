from .factory import Factory

class Motorcycle(Factory):
    def __init__(self, model_name, fuel_type):
        self._number_of_wheels = 2
        self._model_name = model_name
        self._fuel_type = fuel_type
        Motorcycle.motorcycle_count += 1

    def create_vehicle(self):
        pass

    def change_model_name(self, model_name):
        self._model_name = model_name

    def change_fuel_type(self, fuel_type):
        if fuel_type in ['electric', 'petrol', 'diesel']:
            self._fuel_type = fuel_type
        else:
            raise ValueError("Invalid fuel type")

    @classmethod
    def print_motorcycle_count(cls):
        print(f"Total motorcycles created: {cls.motorcycle_count}")

    def __str__(self):
        return (f"Motorcycle(Model Name: {self._model_name}, Fuel Type: {self._fuel_type}, "
                f"Number of Wheels: {self._number_of_wheels})")
