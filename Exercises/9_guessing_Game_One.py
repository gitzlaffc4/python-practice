# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random
import sys

#define program to guess the number
def exercise_9():
    #generate random number
    rand = random.randint(1, 9)
    #set first guess attempt counter
    guesses = 1
    correct = False
    #ask for input
    guess = input("\n Guess what number I am thinking of, 1 through 9: ")
    #while loop until user exits or guesses it right while keeping count of guesses
    while correct is False:
        if guess == 'exit':
            print("goodbye \n")
            sys.exit()
        elif int(guess) not in range(1, 10):
            print("You entered an incorrect number, lets try again \n")
            exercise_9()
        elif int(guess) == rand:
            if guesses == 1:
                print("Congrats you won!!! You got it right in 1 guess!\n")
            else:
                print("Congrats you won!!! You got it right in " + str(guesses) + " guesses!\n")
            return 1
        elif int(guess) < rand:
            guess = input("Too low... try again : ")
            guesses += 1
        elif int(guess) > rand:
            guess = input("Too high... try again :")
            guesses += 1

def guessing(value):
    #keep score
    score = 0
    #add scores
    score += value
    name = input("What is your name? : ")
    keep_playing = True
    while keep_playing:
        if score == 0:
            a = input("Hello " + name + ", Would you like to play a game? (Y/n) :")
            if a.casefold() in ['y','yes']:
                score += exercise_9()
            else:
                print("goodbye\n")
                return
        else:
            a = input("Hello " + name + ", your current score is " + str(score) + ". Would you like to keep playing? (Y/n) :")
            if a.casefold() in ['y','yes']:
                score += exercise_9()
            else:
                print("goodbye\n")
                return
guessing(0)