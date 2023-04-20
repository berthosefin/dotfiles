

def full_rectangle(h, w):
    if h > 0 and w > 0:
        for i in range(h):
            print("*" * w)
    else:
        print()

full_rectangle(3, 5)
full_rectangle(3, -55)