# 大楼管理多台电梯和楼层 多语法组成程序

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
    # 创建一栋 Building 时，需要提供：1. 最低楼层2. 最高楼层3. 电梯数量
    def __init__(self, bottom_floor, top_floor, numbers_of_elevators):

        # 把最低楼层保存为 Building 自己的 property
        self.bottom_floor = bottom_floor
        # 把最高楼层保存为 Building 自己的 property
        self.top_floor = top_floor
        # 创建一个空 list，准备存放 Elevator objects
        self.elevators = []

        # 重复“创建电梯”这么多次。 例如 numbers_of_elevators = 3，就重复3次
        for i in range(numbers_of_elevators):
            # 创建一台新的 Elevator object， bottom_floor 和 top_floor 是前面收到要求的参数
            elevator = Elevator(bottom_floor, top_floor)

            # 把刚创建的这台 elevator 放进 elevators list
            self.elevators.append(elevator)

# 什么时候用self. self, 取决于这个东西是否“长期属于这个 object” → 是，self.xxx
# 反之，只是这个 method 运行过程中临时使用 → xxx

# 让“指定的一台电梯”去“指定的楼层”
# # elevator_number = 选择哪台电梯（list index） destination_floor = 要去几楼
    def run_elevator(self, elevator_number, destination_floor):

        # 从 elevators list 中，根据 index 取出一台电梯
        # 例如 elevator_number = 1
        # 就是 self.elevators[1]
        elevator = self.elevators[elevator_number]

        # 让刚刚选出来的那台 elevator
        # 调用它自己的 go_to_floor() method
        elevator.go_to_floor(destination_floor)


# 火警：让所有电梯都回到最低楼层
    def fire_alarm(self):

        # 从 elevators list 中一台一台取出 elevator
        for elevator in self.elevators:

            # 当前取出来的这台电梯回到底楼
            # self.bottom_floor 是这栋 Building 的最低楼层
            elevator.go_to_floor(self.bottom_floor)