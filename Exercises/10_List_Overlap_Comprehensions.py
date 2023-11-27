# https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

import random

def exercise_10():
    # provided lists
    a = generate_list()
    b = generate_list()
    # find overlap
    c = [i for i in a if i in b]
    result = []
    # remove duplciations
    for i in c:
        if i not in result:
            result.append(i)
    print("Random list A:")
    print(a)
    print("\nRandom list B:")
    print(b)
    print("\nOverlap in list A and B:")
    print(result)

def generate_list():
    length = random.randint(0, 100)
    a = [random.randint(1, 50) for _ in range(length)]
    return a

exercise_10()
