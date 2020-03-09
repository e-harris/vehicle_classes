class vehicle_class():
    def __init__(self, passengers, cargo):
        self.passengers = passengers
        self.cargo = cargo

    def move(self):
        return "Go forward"

    def stop(self):
        return "Stop"
