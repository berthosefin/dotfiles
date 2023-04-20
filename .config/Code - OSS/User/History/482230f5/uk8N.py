

game = ("Rock", "Paper", "Scissor")
def roshambo(char1, char2):
    if char1 in game or char2 in game:
        pass
    else:
        raise ValueError("Error: Invalid move")