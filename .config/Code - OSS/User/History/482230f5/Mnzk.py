

game = ("Rock", "Paper", "Scissor")
def roshambo(char1, char2):
    if not char1 or char2 not in game:
        pass
    else:
        raise ValueError("Error: Invalid move")