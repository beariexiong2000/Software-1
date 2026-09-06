# Main Menu and User Navigation
# User records, age check, enter game

print("Please select an option: ")
print("1. New Game and User Registration")
print("2. Load Game")
print("3. Exit")

choice = input("Enter your choice 1, 2 or 3: ")
if choice == "1":
   print("Please enter your name and age.") 
   username = input("Enter your name: ")
   userage = int(input("Enter your age: "))
   if userage < 12:
     print("Sorry, this game is not suitable for minors under 12 years old.")
   else: 
     print (f"Hello {username}, welcome to the world of Journey to the West!")
     trust_score = 0
     team = []  
     import game_logic     

elif choice == "2":
    print("Loading the Historical Records")
elif choice == "3":
    print("Goodbye! Thank you for playing.")
else:
    print("Invalid choice! Please choose from 1, 2, 3.")

