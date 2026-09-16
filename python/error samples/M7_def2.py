import math
def calculate_unit_price (x,y):
    price = x / ((y / 200) ** 2 * math.pi)
    return price

unit_price = price # 多余的

y1 = float(input("Enter the diameter of the first pizza (cm): "))
x1 = float(input("Enter the price of the first pizza (euros): "))
y2 = float(input("Enter the diameter of the second pizza (cm): "))
x2 = float(input("Enter the price of the second pizza (euros): "))

priceA = calculate_unit_price (x1,y1)
priceB = calculate_unit_price (x2,y2)

print(f"Unit price of the first pizza: {priceA} euros/m²")   # 保留小数
print(f"Unit price of the second pizza: {priceB} euros/m²")   # 保留小数

if priceA < priceB:
    print("The first pizza provides better value for money.")
elif priceA == priceB:
    print("Two pizzas provide same value for money.")
else:
    print("The second pizza provides better value for money.")