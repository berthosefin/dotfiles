from sys import argv

game = ("rock", "paper", "scissor")
if argv[1] in game and argv[2] in game:
    pass
else:
    raise ValueError("Error: Invalid move")