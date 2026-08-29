# 1 Fixed amount of repetitions
rounds = int(input("How many greetings: "))  # 1. 获取总次数
finished_rounds = 0                           # 2. 计数器清零

while finished_rounds < rounds:               # 3. 判断是否达到目标次数
    print("Good morning")                     # 4. 执行任务
    finished_rounds = finished_rounds + 1     # 5. 计数器加 1


# 2 User "Stops" the Loop

command = input("Enter command: ")  # 1. 第一次获取输入

while command != "stop":            # 2. 条件检查
    print("Executing command: " + command) # 3. 循环体：执行命令
    command = input("Enter command: ")     # 4. 循环体：再次获取输入

print("Execution stopped.")        # 5. 循环结束后的收尾代码


# 3 BREAK 语句示例

command = input("Enter command: ")  # 1. 第一次获取输入

while command != "stop":            # 2. 正常循环条件：只要不是 "stop" 就继续
    if command == "MAYDAY":         # 3. 紧急检查：如果输入的是 "MAYDAY"
        break                       # 4. 强制打断！立刻跳出 while 循环
    
    print("Executing command: " + command) # 5. 打印执行信息
    command = input("Enter command: ")     # 6. 重新获取下一个输入

print("Execution stopped.")        # 7. 循环结束后的收尾代码


# 4 模拟筛子

import random                               # 1. 导入随机数工具包

dice1 = dice2 = rolls = 0                   # 2. 变量初始化（全部设为 0）

while (dice1 != 6 or dice2 != 6):           # 3. 循环条件：只要没摇出双 6 就继续
    dice1 = random.randint(1,6)             # 4. 摇第一颗骰子（产生 1~6 的随机整数）
    dice2 = random.randint(1,6)             # 5. 摇第二颗骰子（产生 1~6 的随机整数）
    rolls = rolls + 1                       # 6. 计数器加 1（记录摇的次数）

print(f"Rolled {rolls:d} times.")           # 7. 打印最终统计次数