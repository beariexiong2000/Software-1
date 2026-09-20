class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed =  maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
   
newcar = Car("ABC-123", 142)

print(f"License plate: {newcar.license_plate}")
print(f"Maximum speed: {newcar.maximum_speed} km/h")
print(f"Current speed: {newcar.current_speed} km/h")
print(f"Travelled distance: {newcar.travelled_distance} km")