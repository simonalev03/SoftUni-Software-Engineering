quantity_of_decorations = int(input())
days_left_to_christmas = int(input())
money_spend = 0
christmas_spirit = 0
ornament_set_price = 2
ornament_set_spirit = 5
skirt_price = 5
skirt_spirit = 3
garland_price = 3
garland_spirit = 10
lights_price = 15
lights_spirit = 17
for day in range(1, days_left_to_christmas + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        money_spend += quantity_of_decorations * ornament_set_price
        christmas_spirit += ornament_set_spirit
    if day % 3 == 0:
        money_spend += quantity_of_decorations * (skirt_price + garland_price)
        christmas_spirit += skirt_spirit + garland_spirit
        if day % 5 == 0:
            christmas_spirit += 30
    if day % 5 == 0:
        money_spend += quantity_of_decorations * lights_price
        christmas_spirit += lights_spirit
    if day % 10 == 0:
        christmas_spirit -= 20
        money_spend += skirt_price + garland_price + lights_price
if days_left_to_christmas % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {money_spend}")
print(f"Total spirit: {christmas_spirit}")