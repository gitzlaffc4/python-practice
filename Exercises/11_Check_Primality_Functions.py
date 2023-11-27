# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
import sys


def exercise_11():
    num_a = int(input("Pick and number, any number : "))
    a = range(2, num_a)
    is_prime = True
    for element in a:
        if num_a % element == 0:
            is_prime = False
    if is_prime:
        print("The number " + str(num_a) + " is prime")
    else:
        print("The number " + str(num_a) + " is NOT prime")
    go_again()

def go_again():
    a = input("\nWould you like to go again? (Y/n) : ")

    if a.casefold() in ('y','yes'):
        exercise_11()
    else:
        sys.exit()

exercise_11()