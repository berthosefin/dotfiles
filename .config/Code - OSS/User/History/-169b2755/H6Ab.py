from random import random


def moody_function():
    val = random()
    if val < 0.2:
        raise ValueError("Nop")
    elif val < 0.4:
        raise RuntimeError("Still nop")
    else:
        return "Hmm, ok"