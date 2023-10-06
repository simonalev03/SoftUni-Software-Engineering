amount_of_chicken = int(input())
amount_of_fish = int(input())
amount_of_vegetarian = int(input())

chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
delivery = 2.50

order = (amount_of_chicken * chicken_menu) + (amount_of_fish * fish_menu) + (amount_of_vegetarian * vegetarian_menu)
desert = order - (order * (80 / 100))

sum = order + desert + delivery

print((round(sum, 2)))