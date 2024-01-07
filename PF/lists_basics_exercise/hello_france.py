items_and_values = input().split("|")
budget = float(input())
train_ticket = 150
budget_after_selling_items = 0
profit = 0
new_item_prices = []
for item_value in items_and_values:
    item = item_value.split("->")
    item_type = item[0]
    item_price = float(item[1])
    if item_type == "Clothes":
        if item_price <= 50 and budget >= item_price:
            budget -= item_price
            clothes_price = item_price * 1.4
            profit += clothes_price - item_price
            budget_after_selling_items += clothes_price
            new_item_prices.append(clothes_price)
    elif item_type == "Shoes":
        if item_price <= 35 and budget >= item_price:
            budget -= item_price
            shoe_price = item_price * 1.4
            profit += shoe_price - item_price
            budget_after_selling_items += shoe_price
            new_item_prices.append(shoe_price)
    elif item_type == "Accessories" and budget >= item_price:
        if item_price <= 20.50:
            budget -= item_price
            accessory_price = item_price * 1.4
            profit += accessory_price - item_price
            budget_after_selling_items += accessory_price
            new_item_prices.append(accessory_price)
for new_price in new_item_prices:
    print(f"{new_price:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
budget_after_selling_items += budget
if budget_after_selling_items >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
