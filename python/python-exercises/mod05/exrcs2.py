length1 = float(input("Enter length in inches (negative value to quit): "))
while length1 >= 0:
    length2 = length1 / 0.3937
    print(f"{length1} inches is {length2:.2f} centimeters")
    length1 = float(input("Enter length in inches (negative value to quit): "))
print("Program ended.")