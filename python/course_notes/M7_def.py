# 如果函数每次做的事情完全固定，不需要外部输入 → 不需要参数
def roll_dice():
    number = random.randint(1, 6)   # 固定是1到6，每次调用都一样
    return number

result = roll_dice()   # 调用时括号里不用传东西



# 如果函数要处理的数据，每次调用可能不一样 → 要带参数 
def roll_dice(sides):
    number = random.randint(1, sides)   # sides 每次可能不同（6面？21面？）
    return number

result = roll_dice(6)    # 传入6，摇6面骰
result = roll_dice(21)   # 传入21，摇21面骰




# 怎样调用带参数的函数

def addition(x,y):
    add = x + y 
    return add

x = int(input("Enter x: "))
y = int(input("Enter y: "))

while x > 0 and y > 0: 
    add = addition(x,y)  
    print(add)
    x = int(input("Enter x: "))   # 重新输入，更新x
    y = int(input("Enter y: "))   # 重新输入，更新y


# （）里的参数可以是个列表
def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

number_list = [1, 2, 3, 4, 5]
result = sum_of_list(number_list)
print(f"The sum of the numbers in the list is: {result}")