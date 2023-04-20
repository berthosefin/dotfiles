

def final_pattern(lst, h, w):
    if h > 0 and w > 0:
        for l in lst:
            if l == "full":
                [print("*" * w) for i in range(h)]
            elif l == "empty":
                if h > 2:
                    print("*" * w)
                    for i in range(h-2):
                        if w < 2:
                            print("*")
                        else:
                            print("*" + " " * (w-2) + "*")
                    print("*" * w)
                else:
                    [print("*" * w) for i in range(h)]
            elif l == "diagonal":
                if h == w:
                    if h > 2:
                        print("*" * w)
                        for i in range(h-2):
                            if w < 2:
                                print("*")
                            else:
                                diagonal = "d" * w
                                print(diagonal)
                        print("*" * w)
                    else:
                        [print("*" * w) for i in range(h)]
            elif l == "concentric":
                print("concentric")
                # if h == w:
                #     if h > 2:
                #         print("*" * w)
                #         for i in range(h-2):
                #             if w < 2:
                #                 print("*")
                #             else:
                #                 diagonal = "d" * w
                #                 print(diagonal)
                #         print("*" * w)
                #     else:
                #         [print("*" * w) for i in range(h)]
    else:
        print()


final_pattern(["empty", "concentric", "full", "empty", "diagonal"], 3, 10)
