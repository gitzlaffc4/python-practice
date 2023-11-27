# https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
def excercise_7():
    #predefined list
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    #create new list of only evens
    b = [i for i in a if i % 2 == 0]
    #print list
    print(b)
excercise_7()