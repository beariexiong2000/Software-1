# 为了检查参数是否“空白”，不可float(input)
# list的修改，append/sort等，无需储存为新变量，直接操作即可

user_input = float(input("Enter a number: "))

number_list = []

while user_input != "":
    number_list = number_list.append(user_input)

    user_input = float(input("Enter a number: "))

newlist = number_list.sort(reverse = True)

print(f"newlist(1,6)":.1f)