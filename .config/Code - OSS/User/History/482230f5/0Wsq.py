from sys import argv

game = ("Rock", "Paper", "Scissor")
def roshambo():
    if argv[1] in game or argv[2] in game:
        pass
    else:
        raise ValueError("Error: Invalid move")