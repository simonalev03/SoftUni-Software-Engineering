budget = float(input())
number_of_statists = int(input())
price_clothing_per_statist = float(input())

decor = budget * 10 / 100
if number_of_statists > 150:
    price_clothing_per_statist = price_clothing_per_statist * 90 / 100
expenses = decor + (price_clothing_per_statist * number_of_statists)
diff = abs(expenses - budget)
if expenses > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")