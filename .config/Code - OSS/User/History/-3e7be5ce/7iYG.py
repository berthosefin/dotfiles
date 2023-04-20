

# def empty_rectangle(h, w):
#     if h > 0 and w > 0:
#         print("*" * w)
#         for i in range(h-2):
#             if w < 2:
#                 print("*")
#             else:
#                 print("*" + " " * (w-2) + "*")
#         print("*" * w)
#     else:
#         print()


def empty_rectangle(h, w):
    [print("*" * w) for i in range(h) if h & w > 0]
    if h > 0 and w > 0:
        print("*" * w)
        for i in range(h-2):
            if w < 2:
                print("*")
            else:
                print("*" + " " * (w-2) + "*")
        print("*" * w)
    else:
        print()


empty_rectangle(3, 5)
print()
empty_rectangle(2, 5)
print()
empty_rectangle(3, 1)
print()
empty_rectangle(3, 3)