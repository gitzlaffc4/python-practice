# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

def exercise_13():
    #prompt user
    num = int(input("How many numbers in a fibonacci sequence would you like to generate? : "))
    #start counting at 1
    count = 1
    #create blank list so empty list is returned if num == 0
    fib = []
    if num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while count < (num - 1):
            fib.append(fib[count - 1] + fib[count] )
            count += 1
    print(fib)
    return fib

exercise_13()




