age = int(input())
laundry_price = float(input())
toy_price = int(input())
money_received = 0
toys_received = 0
current_birthday_money = 0
for i in range(1, age + 1):
    if i % 2 == 0:
        current_birthday_money += 10
        money_received += current_birthday_money - 1

    else:
        toys_received += 1
money_from_toys = toys_received * toy_price
saved_money = money_from_toys + money_received
difference = abs(laundry_price - saved_money)
if saved_money >= laundry_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")