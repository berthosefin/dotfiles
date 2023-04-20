from sys import argv

game = ("Rock", "Paper", "Scissor")
def roshambo():
    if char1 in game or char2 in game:
        pass
    else:
        raise ValueError("Error: Invalid move")