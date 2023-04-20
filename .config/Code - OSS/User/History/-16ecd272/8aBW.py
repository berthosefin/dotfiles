

def clamp(vmin, val, vmax):
    if val < vmin:
        res = vmin
    elif val > vmax:
        res = vmax
    else:
        res = vmax
    return res


print(clamp(5, 3, 10))
print(clamp(5, 7, 10))
print(clamp(5, 15, 10))