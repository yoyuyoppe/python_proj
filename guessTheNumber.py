# The game of guessing numbers
import random

def guessTheNumber():
    """
    Provides 6 attempts to guess the number
    """
    for n in range(1, 7):
        guess = int(input("You option: "))

        if (guess > NUMBER):
            print("This number is greater than planned")
        elif (guess < NUMBER):    
            print("This number is less than planned")
        else:
            break

    if guess == NUMBER:
        print("Right! The number of attempts: "+str(n))
    else:
        print("The correct number: "+str(NUMBER))

NUMBER = random.randint(1, 13)
print('Guess a number from 1 to 13')
guessTheNumber()
