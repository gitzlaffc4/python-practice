# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
def exercise_6():
    #get word from input
    word = input("give me a word : ")
    #reverse the word
    rev = word[::-1]
    #compare word to reverserd word using casefold to ignore case
    if word.casefold() == rev.casefold():
        #if the same, let them know
        print(word + " is a Palindrome!")
    else:
        #if not the same, let them know
        print(word + " is NOT a Palindrome!")
exercise_6()