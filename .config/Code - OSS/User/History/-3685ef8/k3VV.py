

def count_separators(sentence: str):
    separator = " -_"
    res = 0
    for s in sentence:
        if s in separator:
            res += 1
    return res


count_separators("I am a sentence")