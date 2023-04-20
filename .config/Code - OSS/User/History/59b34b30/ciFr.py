

def only_digits(sentence):
    if sentence.isdigit():
        res = True
    else:
        res = False
    return res


print(only_digits("555656"))