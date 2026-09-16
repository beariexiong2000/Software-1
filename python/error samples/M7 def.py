def sum_of_list(number):     #  1 参数名可以随便取
    total = 0
    for i in number_list:   #  1  但函数内部应该只使用参数名    
        total += i
    return total


result = sum_of_list(number_list)   # 顺序搞反了： 定义变量 VS 调用函数
number_list = [1, 2, 3, 4, 5]      # 先定义变量（左边）


print(f"The sum of the numbers in the list is: {result}")