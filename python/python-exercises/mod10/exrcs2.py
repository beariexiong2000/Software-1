class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print(self.current_floor)
    def floor_down(self):
        self.current_floor -= 1
        print(self.current_floor)  
        
    def go_to_floor(self, number):
        while self.current_floor < number:
            self.floor_up()

        while self.current_floor > number:
            self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, numbers_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        for i in range(numbers_of_elevators):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, destination_floor):
        elevator = self.elevators[elevator_number]
        elevator.go_to_floor(destination_floor)
    