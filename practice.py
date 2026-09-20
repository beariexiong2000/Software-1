print("Please enter your name and age.") 
def age_check():
    username = input("Enter your name: ")
    userage = int(input("Enter your age: "))
    if userage < 12:
        print("Sorry, this game is not suitable for minors under 12 years old.")
    else:
        print(f"Hello {username}, welcome to the world of Journey to the West!")

age_check()