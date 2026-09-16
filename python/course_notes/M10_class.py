class ClassName:
# 未确定时，用"pass" 占位
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def method(self, parameter):
        # do something
        pass


object1 = ClassName(value1, value2)

object1.method(parameter)