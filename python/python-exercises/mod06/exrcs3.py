# 被几个数整除，不超过2个即质数

number = int(input("Enter an integer: "))

count = 0 # 记录"从2到number-1之间，有多少个数能整除
i = 2  #2是起点，判断质数要排除1和它本身。

while i < number:
    if number % i == 0:
        count = count + 1
    i = i + 1

if count == 0 and number >= 2:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")







number = int(input("Enter an integer: "))

if number < 2:
    print(f"{number} is not a prime number.")
else:
    prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            prime = False
            break

    if prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

