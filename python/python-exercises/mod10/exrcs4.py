class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed =  maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    
    def accelerate(self, change):
        if 0 <= self.current_speed + change <= self.maximum_speed:
            self.current_speed = self.current_speed + change
        elif self.current_speed + change < 0:
            self.current_speed = 0
        else:
            self.current_speed = self.maximum_speed
   
    def drive(self, hours):
        self.travelled_distance = self.travelled_distance + hours * self.current_speed

import random
def race(cars):
    longest_distance = 0
    while longest_distance < 10000:
        for car in cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

            if car.travelled_distance > longest_distance:
                longest_distance = car.travelled_distance

    return cars

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
    
    def hour_passes(self):
        import random
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)
        
    def print_status(self):
        for car in self.cars:
            print(car.license_plate, car.maximum_speed, car.current_speed, car.travelled_distance)
    
    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True

        return False