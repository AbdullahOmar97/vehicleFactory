from abc import ABC, abstractmethod

class Factory(ABC):
    car_count = 0
    motorcycle_count = 0

    @abstractmethod
    def create_vehicle(self):
        pass

    @classmethod
    def get_vehicle_count(cls):
        return cls.car_count, cls.motorcycle_count
