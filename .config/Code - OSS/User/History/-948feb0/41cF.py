

def can_pay(price, percentage, amount):
    final_price = price - (40 * price)/100
    if final_price < amount:
        res = True
    else:
        res = False
    return res


print(can_pay(1000, 40, 5000))