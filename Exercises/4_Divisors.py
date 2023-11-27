#https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
def exercise_4():
    num_a = int(input("Pick and number, any number : "))
    a = range(2, num_a)
    for element in a:
        if num_a % element == 0:
            print(str(element))
    go_again()

def go_again():
    a = input("Would you like to go again? (Y/n) : ")

    if a in ('Y','y','yes'):
        exercise_4()

exercise_4()