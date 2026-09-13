name = set()
user_input = input("Enter a name: ")

while user_input != "":

    if user_input in name:
        print("Existing name")
        user_input = input("Enter a name: ")
    else:
        print("New name")
        name.add(user_input)
        user_input = input("Enter a name: ")
for i in name:
    print(i)

