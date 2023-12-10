import random

#First we will define our basic 3 moves that are Rock, Paper and Scissors
moves = ('rock','paper','scissors')
play_game = True

while play_game:
    player1 = None
    Computer = random.choice(moves)
    
    while player1 not in moves:
        player1 = input("Enter your move (rock,paper,scissors):")

    #Taking player input and printing the selected moves by Player and Computer
    print("Player's Move: {}".format(player1))
    print("Computer's Move: {}".format(Computer))
    
    #Checking the win and lose conditions for Player
    if player1 == Computer:
        print("It's a Tie!!")
    elif player1 == 'rock' and Computer == 'scissors':
        print("Player1 wins!!!!")
    elif player1 == 'paper' and Computer == 'rock':
        print("Player1 wins!!!!")
    elif player1 == 'scissors' and Computer == 'paper':
        print("Player1 wins!!!!")
    else:
        print("Computer Wins ")
    #Taking input to play the game again
    if not input("Do you want to play Again? (y/n)").lower() == 'y':
        play_game = False

print("Thanks for playing!!")
