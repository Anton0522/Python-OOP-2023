from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self,fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self,amount):
        pass


class Car(Vehicle):
    def drive(self,distance):
        consumption = (self.fuel_consumption + 0.9) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self,amount):
        self.fuel_quantity += amount


class Truck(Vehicle):
    def drive(self, distance):
        consumption = (self.fuel_consumption + 1.6) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, amount):
        self.fuel_quantity += amount * 0.95
