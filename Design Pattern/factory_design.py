'''
The Factory design pattern in Python is a creational pattern that provides an interface or a function 
for creating objects without explicitly specifying their concrete classes

When to Use the Factory Pattern
Decoupling code: When the client code needs to be independent of the exact classes of objects it creates.
Handling complex creation logic: When the process of creating an object is complex or involves conditional logic (e.g., based on input data or configuration).
Supporting multiple product types: When an application needs to support various related objects that share a common interface, and new types may be added in the future without modifying existing client code (adhering to the Open/Closed Principle).
Centralizing object creation: To have a single point of control for object instantiation, which simplifies maintenance and testing. 
'''

from abc import ABC, abstractmethod

# 1. Product Interface (Abstract Class in Python)
class Vehicle(ABC):
    @abstractmethod
    def print_vehicle(self):
        pass

# 2. Concrete Products
class Car(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def print_vehicle(self):
        print(f"Creating a Car: {self.brand} {self.model}")

class Bike(Vehicle):
    def __init__(self, brand, bike_type):
        self.brand = brand
        self.bike_type = bike_type

    def print_vehicle(self):
        print(f"Creating a Bike: {self.brand} {self.bike_type}")

# 3. Factory Method/Class
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type, **kwargs):
        if vehicle_type == 'Car':
            return Car(kwargs['brand'], kwargs['model'])
        elif vehicle_type == 'Bike':
            return Bike(kwargs['brand'], kwargs['bike_type'])
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")

# 4. Client Code
if __name__ == "__main__":
    car = VehicleFactory.create_vehicle('Car', brand='Toyota', model='Corolla')
    bike = VehicleFactory.create_vehicle('Bike', brand='Yamaha', bike_type='Sport')

    car.print_vehicle()
    bike.print_vehicle()
