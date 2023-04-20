from sys import argv

game = ("rock", "paper", "scissor")
if len(argv) == 3:
    if argv[1] in game and argv[2] in game:
        if argv[1] == argv[2]:
            print("Draw")
        elif argv[1] == 'rock' and argv[2] == 'paper':
            print("Paper wins.")
    else:
        raise ValueError("Error: Invalid move")
else:
    raise ValueError("Error: You must enter exactly 2 arguments.")