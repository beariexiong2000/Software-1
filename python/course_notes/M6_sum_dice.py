# 初级版本不用 for
import random

number = int(input("How many dice to roll: "))

finished_number = 0
dice_list = []

while finished_number < number:
    dice = random.randint(1, 6)
    dice_list.append(dice)
    finished_number += 1

sum_dice = sum(dice_list)

print(f"Sum of the dice: {sum_dice}")

# for + range

import random
# 导入 random 模块，让我们可以生成随机数


dice_list = []
# 创建一个空列表，用来保存每一次掷骰子的结果


dice_num = int(input("How many dice to roll: "))
# 让用户输入要掷多少个骰子
# input() 得到的是字符串，所以用 int() 转换成整数


for counter in range(dice_num):
    # 重复 dice_num 次
    # counter 会依次得到 0, 1, 2, ... dice_num - 1

    dice_roll = random.randint(1, 6)
    # 随机生成一个 1 到 6 之间的整数
    # 相当于掷一次骰子

    dice_list.append(dice_roll)
    # 把这一次掷骰子的结果加入 dice_list


sum_dice = sum(dice_list)
# 把 dice_list 里面所有骰子的数字加起来


print(f"Sum of the dice: {sum_dice}")
# 输出所有骰子的总和