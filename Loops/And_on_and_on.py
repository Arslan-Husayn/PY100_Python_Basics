

while True:
    print("and on")
    break


#testing a while loop for a number guessing game

import random

secret_number = random.randint(1,7)

while True:
    guess = int(input("Guess between 1 and 7: "))

    if guess == secret_number:
        print("You got that shit! 🎉")
        break
    else:
        "Nope, do it again sucka"