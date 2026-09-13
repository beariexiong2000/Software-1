# Main Menu and User Navigation
# User records, age check, enter game or end game

print("Please enter your name and age.") 
username = input("Enter your name: ")
userage = int(input("Enter your age: "))

if userage < 12:
    print("Sorry, this game is not suitable for minors under 12 years old.")
else: 
    print(f"Hello {username}, welcome to the world of Journey to the West!")
    
    choice = ""
    
    
    while choice != "lopeta":
        print("\nPlease select an option: ")
        print("1. New Game")
        print("2. Load Game")
        print("lopeta")

        choice = input("Enter your choice: ")

        if choice == "1":
            trust_score = 0
            team = [] 
            import game_logic 

        elif choice == "2":
            print("Loading the Historical Records...")

        elif choice == "lopeta":
            print("Goodbye! Thank you for playing.")

        else:
            print("Invalid choice! Please try again.")

