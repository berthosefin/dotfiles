

def only_digits(sentence):
    return isinstance(sentence, (int, float))


print(only_digits("666"))
print(only_digits("N6656"))