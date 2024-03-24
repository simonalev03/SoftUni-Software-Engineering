orders = {}
items_price = {}
command = input()
while command != "buy":
    product_info = command.split()
    product_name = product_info[0]
    product_price = float(product_info[1])
    product_quantity = int(product_info[2])
    items_price[product_name] = product_price
    if product_name in orders.keys():
        orders[product_name] += product_quantity
        if items_price[product_name] != product_price:
            items_price[product_name] = product_price
    else:
        orders[product_name] = product_quantity
    command = input()
for quantity in orders.keys():
    orders[quantity] *= items_price[quantity]

for product_name, product_price in orders.items():
    print(f"{product_name} -> {product_price:.2f}")
