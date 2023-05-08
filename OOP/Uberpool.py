from car import Car

class Uberpool(Car):
    brand = str
    model = str 

    def __init__(self, License, Driver, brand, model):
        super.__init__(License,Driver)
        self.brand = brand
        self.model = model

