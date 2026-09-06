user_input = input("Enter a number (or press Enter to quit): ")
if user_input != "":
    min_num = float(user_input)
    max_num = float(user_input)
    # ask for next number
    user_input = input("Enter a number (or press Enter to quit): ")
    while user_input != "":
         # Convert the text input into a number, as "user_input" is a string text that cannot be compared, and "number" is more readible. 
         number = float(user_input)
         if number < min_num:
            min_num = number
         if number > max_num:
            max_num = number
         user_input = input("Enter a number (or press Enter to quit): ")
    print(f"Smallest number: {min_num}") 
    print(f"Largest number: {max_num}")   