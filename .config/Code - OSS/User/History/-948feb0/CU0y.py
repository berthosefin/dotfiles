

def can_pay(price, percentage, amount):
    final_price = price - (40 * price)/100
    return final_price < amount


print(can_pay(1000, 40, 599))
print(can_pay(1000, 40, 601))