#https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
def exercise_1():
    name = input("What is your name? : ")
    age = int(input("How old are you? : "))
    how_many = int(input("How many times should I introduce you? :"))
    turn_100 = 2023 + (100 - age)

    n = 0
    while n < how_many:
        print("Hello " + name + ", you will turn 100 years old in " + str(turn_100) + ".")
        print("")
        n += 1
    exercise_1()
exercise_1()