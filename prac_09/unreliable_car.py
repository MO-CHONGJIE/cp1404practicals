from car import Car
from random import randint

class UnreliableCar(Car):
    """Represent a Car object."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

