 ① Create the starting value
value = ...

# ② Start repeating
while condition_using(value):

    # ③ Process the CURRENT value
    if ...:
        ...

    if ...:
        ...

    # ④ Change the value used in the while condition
    value = ...

# ⑤ Do something after the loop ends
# if/while/for，后接4个缩进
# while 负责“继续”，if 负责“判断”
# 循环里必须再次有个 input(.....)