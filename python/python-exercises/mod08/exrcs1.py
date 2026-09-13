def get_seasons(number):
    winter, spring, summer, autumn = (12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)
    seasons = {"winter": winter, "spring": spring, "summer": summer, "autumn": autumn}

    for a,b in seasons.items():
        if number in b:
            return a
    

user_input = int(input("Enter the number of a month (1-12): "))
print(f"You entered {user_input}")

out_season = get_seasons(user_input)

if user_input in range(1,13):
    print(f"The season is {out_season}")
else:
    print("Please return a valid number!")



