# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

def exercise_12(list):
    new_list = [list[0],list.pop()]
    print(new_list)
    return new_list

exercise_12([1,3,5,6,7,8])
