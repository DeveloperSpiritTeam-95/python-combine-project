# Project Title: Guess The Number

import random

target = random.randint(1,100)

while True:
    print(target)
    userChoice = input("Guess the target Value or Quit(Q):")
    if(userChoice == "Quite" or userChoice == "quite"):
        break
    else:
        userChoice = int(userChoice)
        if(target == userChoice):
            print("You win the Game. Congratulation.")
            break
        elif(userChoice < target):
            print("your number was too small. Take a Bigger Guess.")
        else:
            print("your number was too large. Take a Smaller Guess.")
         
print("=====GAME OVER=====")