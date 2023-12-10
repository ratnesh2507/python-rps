# Rock, Paper, Scissors Game

## Features and Functionality

This Python script implements a simple Rock, Paper, Scissors game where a player competes against the computer. The game continues until the player decides not to play again.

### Game Setup

- The game includes three basic moves: 'rock', 'paper', and 'scissors'.

- The `moves` tuple stores these three moves.

- The variable `play_game` is initially set to `True` to ensure the game starts.

### Game Loop

- The game is wrapped in a `while` loop (`while play_game:`) to allow continuous gameplay until the player decides to stop.

- In each iteration of the loop:
  - The computer randomly chooses a move from the `moves` tuple using `random.choice`.
  - The player is prompted to input their move, and the input is validated to ensure it is one of the allowed moves.

### Game Mechanics

- The selected moves by the player and the computer are displayed.

- The game checks the win and lose conditions for the player based on the selected moves:
  - If the player and computer choose the same move, it's a tie.
  - If the player's move beats the computer's move, the player wins.
  - If the player's move loses to the computer's move, the computer wins.

### Play Again

- After each round, the player is asked if they want to play again. If the player inputs 'y', the game continues; otherwise, `play_game` is set to `False`, and the loop exits.

### Running the Game

- To play the game, execute the script.

- Follow the on-screen instructions to input your move ('rock', 'paper', or 'scissors').

- The result of each round will be displayed, and you can choose to play again.

### Sample Usage

```python
while play_game:
    player1 = None
    Computer = random.choice(moves)
    
    while player1 not in moves:
        player1 = input("Enter your move (rock, paper, scissors):")

    # ... (game mechanics)

    if not input("Do you want to play Again? (y/n)").lower() == 'y':
        play_game = False

print("Thanks for playing!!")
