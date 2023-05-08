from car import Car

class UberVan(Car):
    typecar = []
    seats = [] 

    def __init__(self, License, Driver, typecar, seats):
        super.__init__(License,Driver)
        self.typecar = typecar
        self.seats = seats
