import random

wins = 0
loss = 0

random_num = random.randint(0,2)
print(random_num)

user_request = input("Please enter your guess 0)Rock... 1)Paper... 2)Scissors ")
request = int(user_request)
if request == '2':
    