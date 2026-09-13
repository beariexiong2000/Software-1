import random

dice_list = []
dice_num = int(input("How many dice to roll: "))

for a in range(dice_num):
    dice_roll = random.randint(1, 6)
    dice_list.append(dice_roll)

sum_dice = sum(dice_list)

print(f"Sum of the dice: {sum_dice}")