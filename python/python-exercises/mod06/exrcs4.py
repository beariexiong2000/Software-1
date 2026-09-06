city_list = []

for i in range(5):
    city = input("Enter the name of a city: ")
    city_list.append(city)

print()
print()
print("The cities you entered:")

for city in city_list:
    print(city)