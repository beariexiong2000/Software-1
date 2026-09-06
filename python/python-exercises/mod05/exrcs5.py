username = "python"
password = "rules"
un_input = input("Enter username: ")
pw_input = input("Enter password: ")

attemps = 0

while (un_input != username or pw_input != password) and attemps < 4:
    attemps += 1
    print ("Incorrect username or password. Please try again.")
    un_input = str(input("Enter username: "))
    pw_input = str(input("Enter password: "))
if un_input == username and pw_input == password and attemps < 6:
    print("Welcome")
else:
    print("Access denied")