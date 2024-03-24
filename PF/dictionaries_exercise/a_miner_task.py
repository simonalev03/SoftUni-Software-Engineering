resources_quantity = {}

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())

    if resource not in resources_quantity:
        resources_quantity[resource] = 0
    resources_quantity[resource] += quantity

for resource, quantity in resources_quantity.items():
    print(f"{resource} -> {quantity}")
