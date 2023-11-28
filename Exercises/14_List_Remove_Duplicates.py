# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

## base exercise 14
def dup_loop(alist):
    no_dups = []
    for i in alist:
        if i not in no_dups:
            no_dups.append(i)
    return no_dups
def dup_set(alist):
    no_dups = list(set(alist))
    return no_dups

## redo exercise 5

# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
import random
#imports
def exercise_5():

    a = generate_list()
    b = generate_list()
    c = set(a + b)

    print(list(c))

def generate_list():
    length = random.randint(0, 20)
    a = [random.randint(1, 100) for _ in range(length)]
    return a
exercise_5()
