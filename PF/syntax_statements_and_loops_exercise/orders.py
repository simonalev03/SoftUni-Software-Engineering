number_of_orders = int(input())
total_order_price = 0
for order in range(number_of_orders):
    order_price = 0
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if not (0.01 <= price_per_capsule <= 100.00):
        continue
    elif not (1 <= days <= 31):
        continue
    elif not (1 <= capsules_per_day <= 2000):
        continue
    else:
        order_price = price_per_capsule * capsules_per_day * days
    if order_price != 0:
        print(f"The price for the coffee is: ${order_price:.2f}")
    else:
        continue
    total_order_price += order_price
print(f"Total: ${total_order_price:.2f}")