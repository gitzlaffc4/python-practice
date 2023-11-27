# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
def excercise_2():
    num_a = int(input("Pick a number : "))
    num_b = int(input("Pick another number : "))

    if num_a % num_b == 0:
        print (str(num_a) + " is divisible by " + str(num_b) + ".")
    elif num_a % 2 == 0:
        print(str(num_a) + " is not divisible by " + str(num_b) + ", but is even")
    else:
        print(str(num_a) + " is not divisible by " + str(num_b) + ", but is odd")
    print("")

    excercise_2()

excercise_2()
