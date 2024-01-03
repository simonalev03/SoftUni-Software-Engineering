budget = float(input())
price_for_1_kg_flour = float(input())
number_of_loaves_bread = 0
colored_eggs = 0
price_for_1_pack_eggs = price_for_1_kg_flour * 0.75
price_for_1l_milk = price_for_1_kg_flour * 1.25
price_for_1_loaf = price_for_1_kg_flour + price_for_1_pack_eggs + (price_for_1l_milk / 4)
while True:
    if budget < price_for_1_loaf:
        break
    budget -= price_for_1_loaf
    number_of_loaves_bread += 1
    colored_eggs += 3
    if number_of_loaves_bread % 3 == 0:
        colored_eggs -= (number_of_loaves_bread - 2)
print(f"You made {number_of_loaves_bread} loaves of Easter bread!\
 Now you have {abs(colored_eggs)} eggs and {budget:.2f}BGN left.")
