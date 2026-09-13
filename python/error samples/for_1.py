# import random + random.randint???
# sum() VS append()???

import random

number = int(input("How many dice to roll: "))

finished_number = 0

sum_dice = []

while finished_number < number:

    sum_dice = sum(sum_dice)
    finished_number += 1

print(f"Sum of the dice: {sum_dice}")


#正确的使用for

import random

dice_list = []
dice_num = int(input("How many dice to roll: "))

for counter in range(dice_num):
    dice_roll = random.randint(1, 6)
    dice_list.append(dice_roll)

sum_dice = sum(dice_list)

print(f"Sum of the dice: {sum_dice}")