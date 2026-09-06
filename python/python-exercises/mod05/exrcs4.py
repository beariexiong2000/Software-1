import random
cmp_num = random.randint(1,10)
guess = int(input("Guess a number (1-10): "))
while guess != cmp_num:
    
    if guess > cmp_num:
        print("Too high")
    if guess < cmp_num:
        print("Too low")
    guess = int(input("Guess a number (1-10): "))
    
print("Correct")