# -------------------------------------------------------------------
# 单位换算————用f来自动四舍五入& "\n"无缝换行
# -------------------------------------------------------------------

# 1. 接收用户输入并转换为浮点数（float）
# 提示词末尾的 \n 确保输入时界面整洁
talents = float(input("Enter talents:\n"))
pounds = float(input("Enter pounds:\n"))
lots = float(input("Enter lots:\n"))

# 2. 换算总重量（单位：克 grams）
# 换算标准：1 talent = 20 pounds, 1 pound = 32 lots, 1 lot = 13.3 grams
total_grams = talents * 20 * 32 * 13.3 + pounds * 32 * 13.3 + lots * 13.3

# 3. 拆分千克（kg）与余下的克（g）
# // 是整除运算符，只取整数部分；int() 转换确保结果为整数千克
kilograms = int(total_grams // 1000)

# % 是取模（求余数）运算符，取出不足 1000 克的剩余克数
remaining_grams = total_grams % 1000

# 4. 格式化输出结果（重点分析：f-string 拼接 + 换行 + 自动格式化保留小数）
# 
# 详细解析：
#  - 字符串开头的 f 表示这是一个 f-string（格式化字符串），允许在字符串内部用 {} 直接嵌入变量。
#  - \n : 换行符（Line Break）。系统评测要求 "modern units:" 后面必须换行，\n 的作用就是强行切到下一行。
#  - {kilograms} : 直接把整除得到的整数千克插入该位置。
#  - {remaining_grams:.2f} : 自动约数/格式化控制。
#      * ':' 代表对后面的变量开启格式化设定。
#      * '.2f' 意思是保留 2 位小数的浮点数（Float）。
#      * 优势：它会自动补充末尾的 0（比如 512.0 会自动显示为 512.00，425.6 会补全为 425.60），完美匹配评测系统的精确对比！
print(f"The weight in modern units:\n{kilograms} kilograms and {remaining_grams:.2f} grams.")