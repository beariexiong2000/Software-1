number_box = []
number = input("Enter a number: ")

while number != "":
    number = float(number)
    number_box.append(number)
    number = input("Enter a number: ")
    
number_box.sort(reverse=True)

print("The greatest numbers in descending order:")

for number in number_box[:5]:
    print(number)
