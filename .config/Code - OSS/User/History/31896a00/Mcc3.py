

# def full_rectangle(h, w):
#     if h | w > 0:
#         for i in range(h):
#             print("*" * w)
#     else:
#         print()


def full_rectangle(h, w):
    [print("*" * w) if h | w > 0 else print() for i in range(h)]


full_rectangle(3, 5)
full_rectangle(3, -5)