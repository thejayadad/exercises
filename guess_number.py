import random #built in python module 

target_number = random.randint(1,10) 
print(target_number)
guess_count = 0
game_one = True

count = 0
while count < 3:
    user_guess = input("Pick a number between 1 & 10 ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    if user_guess == target_number:
        print("You got it!")
        break
    elif user_guess > target_number:
        print("Guess to High!")
        count += 1
    elif user_guess < target_number:
        print("Guess to Low")
        count += 1
    if count == 3:
        print("U LOOSE!!!!!")
