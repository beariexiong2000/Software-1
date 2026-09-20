# Main Menu and User Navigation
# User records, age check, enter game or end game


print("Please enter your name and age.") 
def age_check():
    username = input("Enter your name: ")
    userage = int(input("Enter your age: "))
    if userage < 12:
        print("Sorry, this game is not suitable for minors under 12 years old.")
    else:
        print(f"Hello {username}, welcome to the world of Journey to the West!")

age_check()
    
choice = ""
    
while choice != "lopeta":
    print("\nPlease select an option: ")
    print("1. New Game")
    print("2. Load Game")
    print("3. Game Records")
    print("lopeta")

    choice = input("Enter your choice: ")
    journey_diary = []
    if choice == "1":
        trust_score = 0
        team = [] 
        import game_logic 

    elif choice == "2":
        print("Loading the Historical Records...")

    elif choice == "3":
        def game_records():
            print("1. Write about today's journey")
            print("2. View your journey's diary")
            game_record_choice = input("Enter your choice: ")

            if record_choice == "1":
                text = input("Write about today's journey: ")
                journey_diary.append(text)
                print("Your text has been added.")

            elif record_choice == "2":
                print("This is your journey's diary:")
                print(journey_diary)

            elif record_choice == "3":
                print("Returning to Main Menu.")
            else:
                print("Invalid choice! Please try again.")

        game_records()    
    elif choice == "lopeta":
        print("Goodbye! Thank you for playing.")
        
    else:
        print("Invalid choice! Please try again.")

