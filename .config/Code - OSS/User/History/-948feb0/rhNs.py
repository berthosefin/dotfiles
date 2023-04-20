

def can_pay(price, percentage, amount):
    final_price = price - (40 * price)/100
    return final_price <= amount


print(can_pay(1000, 50, 500))
print(can_pay(1000, 50, 499))
print(can_pay(100, 25, -1000))
print(can_pay(0, 43, 0))