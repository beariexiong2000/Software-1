from player import Player

print("Please select an option: ")
print("1. New Game and User Registration")
print("2. Load Game")
print("3. Exit")

choice = input("Enter your choice 1, 2 or 3: ")

if choice == "1":
    print("Please enter your name and age.") 
    username = input("Enter your name: ")
    
    # 简单的防错：防止玩家把年龄输成字母导致报错
    try:
        userage = int(input("Enter your age: "))
    except ValueError:
        print("Invalid age! Please enter a valid number next time.")
        userage = 0

    if userage < 12:
        print("Sorry, this game is not suitable for minors under 12 years old.")
    else: 
        print(f"\nHello {username}, welcome to the world of Journey to the West!")
        # Create the Player 
        current_player = Player(username, userage)
        current_player.show_status()

elif choice == "2":
    print("Loading the Historical Records...")

elif choice == "3":
    print("Goodbye! Thank you for playing.")

else:
    print("Invalid choice! Please choose from 1, 2, 3.")