#https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
def exercise_3():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    smaller = int(input("Find numbers less than : "))

    for element in a:
        if element < smaller:
            b.append(element)
    print(b)

exercise_3()