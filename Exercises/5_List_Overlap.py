# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
import random
#imports
def exercise_5():

    a = generate_list()
    b = generate_list()
    c = []

    for element_a in a:
        if element_a in b and element_a not in c:
            c.append(element_a)
    print(c)

def generate_list():
    length = random.randint(0, 100)

    a = [random.randint(1, 20) for _ in range(length)]

    return a

exercise_5()
