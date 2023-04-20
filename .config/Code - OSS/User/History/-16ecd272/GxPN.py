

def clamp(vmin, val, vmax):
    if val < vmin:
        res = vmin
    elif val > vmax:
        res = vmax
    else:
        res = vmax
    return res


clamp(5, 3, 10)