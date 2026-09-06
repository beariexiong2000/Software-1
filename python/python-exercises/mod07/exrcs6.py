import math

def calculate_unit_price(diameter_cm, price_euros):
    # Convert diameter from cm to radius in meters
    radius_m = (diameter_cm / 100) / 2
    # Calculate area in square meters (A = pi * r^2)
    area_m2 = math.pi * (radius_m ** 2)
    # Calculate unit price per square meter
    unit_price = price_euros / area_m2
    return unit_price

dia1 = float(input("Enter the diameter of the first pizza (cm): "))
price1 = float(input("Enter the price of the first pizza (euros): "))

dia2 = float(input("Enter the diameter of the second pizza (cm): "))
price2 = float(input("Enter the price of the second pizza (euros): "))

unit_price1 = calculate_unit_price(dia1, price1)
unit_price2 = calculate_unit_price(dia2, price2)

print(f"Unit price of the first pizza: {unit_price1:.2f} euros/m²")
print(f"Unit price of the second pizza: {unit_price2:.2f} euros/m²")

if unit_price1 < unit_price2:
    print("The first pizza provides better value for money.")
elif unit_price2 < unit_price1:
    print("The second pizza provides better value for money.")
else:
    print("Both pizzas offer the same value for money.")