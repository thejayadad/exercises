import random #built in python module 

target_number = random.randint(1,10) #get random number between 1-10
print(target_number)

count = 0 #Variable just keep count of turns

while count < 3:
    user_guess = input("Pick a number between 1 & 10 ")
    if user_guess.isdigit(): #built in method to see if all text are digits
        user_guess = int(user_guess) #int method to convert string to integer
    if user_guess == target_number: #compare guess to target
        print("You got it!")
        break
    elif user_guess > target_number: #if guess is greater than target
        print("Guess to High!")
        count += 1 # increase count by one
    elif user_guess < target_number: #if guess is less than target
        print("Guess to Low")
        count += 1 
    if count == 3: #if we get 3 counts
        print("U LOOSE!!!!!")
