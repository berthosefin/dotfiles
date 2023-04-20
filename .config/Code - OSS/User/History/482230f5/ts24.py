from sys import argv

game = ("rock", "paper", "scissor")
if 2 < len(argv) < 2:
    if argv[1] in game and argv[2] in game:
        pass
    else:
        raise ValueError("Error: Invalid move")
else:
    raise ValueError("Error: You must enter exactly 2 arguments.")