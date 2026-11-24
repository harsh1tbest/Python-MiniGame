#we are going to genrate a randomm number and asks the user to guess it
import random
G=random.randint(1,10)
UI=-1
guess=0
while (UI!=G):
    UI=int(input("take a guess"))
    guess+=1
    if UI>G:
        print("guessed no is higher try guessing lower")
    elif UI<G:
        print("guessed no is lower try guessing higher")
    else:
        print("correct guess you won the game")
print(f"you guesses the correct no in {guess} guesses") 