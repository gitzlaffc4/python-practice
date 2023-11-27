#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#Remember the rules:
# - Rock beats scissors
# - Scissors beats paper
# - Paper beats rock

def ask(n):
    ask_again = True
    selection = ""
    while ask_again:
        selection = input("Player " + str(n) + ", Rock, Paper, or Scissors? : ").casefold()
        if selection in ['rock','r','paper','p','scissors','s']:
            ask_again = False
        else:
            print("Your entry is invalid, please try again")
    return selection

def rps():
    player1 = ask(1)
    player2 = ask(2)
    print("Player 1 picked " + player1)
    print("Player 2 picked " + player2)
    a = [player1,player2]
    if player1 == player2:
        print("It's a Tie!!!")
    elif player1 == 'rock':
        if player2 == 'scissors':
            print("Rocks breaks Scissors, Player 1 Wins")
        else:
            print("Paper covers rock, Player 2 Wins")
    elif player1 == 'paper':
        if player2 == 'scissors':
            print("Scisscors cuts paper , Player 2 Wins")
        else:
            print("Paper covers rock, Player 1 Wins")
    elif player1 == 'scissors':
        if player2 == 'rock':
            print("Rocks breaks Scissors , Player 2 Wins")
        else:
            print("Scissors cut paper, Player 1 Wins")
    print("")
    play_again = input("Would you like to play again? Y/n : ").casefold()
    if play_again in ['yes','y']:
        rps()
    else:
        print("goodbye")
        return

rps()