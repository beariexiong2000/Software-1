import random

# ----------------- 1. 生成 3 位密码 (每位 0-9) -----------------
code_3digit = ""  # 先准备一个空盒子（空字符串）用来装密码

# 只要密码的长度小于 3，就一直重复执行循环 body 里的代码
while len(code_3digit) < 3:
    num = random.randint(0, 9)  # 随机生成一个 0 到 9 的数字
    code_3digit += str(num)     # 把数字转成字符，拼接到密码字符串末尾 “+=” 可以用来拼接字符串 

# ----------------- 2. 生成 4 位密码 (每位 1-6) -----------------
code_4digit = ""  # 准备第二个空盒子

# 只要密码的长度小于 4，就继续循环
while len(code_4digit) < 4:
    num = random.randint(1, 6)  # 随机生成一个 1 到 6 的数字
    code_4digit += str(num)     # 拼接到密码末尾

# ----------------- 3. 输出最终结果 -----------------
print("3位密码:", code_3digit)
print("4位密码:", code_4digit)

 #   方法2 if 循环版  #
 import random

# ----------------- 1. 生成 3 位密码 (每位 0-9) -----------------
code_3digit = ""
while len(code_3digit) < 3:
    num = random.randint(0, 9)
    # 用 if 进行校验（虽然 randint 已限制范围，这里用来展示 logic）
    if 0 <= num <= 9:
        code_3digit += str(num)

# ----------------- 2. 生成 4 位密码 (每位 1-6) -----------------
code_4digit = ""
while len(code_4digit) < 4:
    num = random.randint(0, 9)  # 故意生成 0-9 范围的数字
    
    # 用 if 条件检查：只有当数字在 1 到 6 之间时，才拼进密码里
    if 1 <= num <= 6:
        code_4digit += str(num)
    # 如果生成的数字是 0、7、8、9，if 不成立，就会被自动扔掉，循环继续

print("3位密码:", code_3digit)
print("4位密码:", code_4digit)