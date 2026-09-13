# 判断是否为质数，最重要的是找出逻辑分支————循环何时停止

# while -if-else版
user_input = int(input("Enter an integer: "))

i = 2
is_prime = True

if user_input <= 1:
    is_prime = False

while i * i <= user_input:
    if user_input % i == 0:
        is_prime = False
        break

    i += 1

if is_prime:
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")


# for 版
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