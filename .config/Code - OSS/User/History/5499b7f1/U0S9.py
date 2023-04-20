from seven_wonders import seven_wonders


def get_odd_wonders(lst: list):
    for i in range(len(lst)):
        for l in lst:
            if i%2==0:
                print(l[i])


print(get_odd_wonders(seven_wonders()))
print(get_odd_wonders(["salad", "tomato", "onion"]))