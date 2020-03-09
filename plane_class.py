from vehicle_class import *


class plane(vehicle_class):

    def __init__(self, passengers, cargo, altitude, crew, engines):
        super().__init__(passengers, cargo)
        self.altitude = altitude
        self.crew = crew
        self.eninges = engines

    def takeoff(self):
        return "The plane is now airborne"

    def land(self):
        return "We have landed"
