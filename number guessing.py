#number guessing game
import random
hidden = random.randrange(1,201)
while True :
    user_input = input("Please Enter your guess[x]:")
    print(user_input)
    
    if user_input == 'x':
        print("sad to see you leaving early")
        exit()
    guess = int(user_input)
    if guess == hidden:
        print("hit")
        break
    if guess<hidden:
        print("your guess is too low")
    else :
        print("your guess is too high")