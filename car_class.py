from vehicle_class import *

# car class

# import my vehicle class

# define car class here and make it inherit from vehicle


#Characterists:
# brand
# horse_power
# max_speed

#methods :
# park
# honk


class car(vehicle_class):

    def __init__(self, passengers, cargo, brand, horse_power, max_speed):
        super().__init__(passengers, cargo)
        self.brand = brand
        self.horse_power = horse_power
        self.max_speed = max_speed

    def park(self):
        return "The car is parked"

    def honk(self):
        return "BEEP BEEP"
