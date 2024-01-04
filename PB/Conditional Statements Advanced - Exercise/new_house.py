# Read user input
flower_type = input()
quantity_flowers = int(input())
budget = int(input())

# Logic
rose = 5
dahlia = 3.80
tulip = 2.80
narcissus = 3
gladiolus = 2.5
flower_price = 0

if flower_type == "Roses" and quantity_flowers > 80:
    flower_price = (rose * quantity_flowers) * 0.9
elif flower_type == "Roses" and quantity_flowers <= 80:
    flower_price = (rose * quantity_flowers)

if flower_type == "Dahlias" and quantity_flowers > 90:
    flower_price = (dahlia * quantity_flowers) * 0.85
elif flower_type == "Dahlias" and quantity_flowers <= 90:
    flower_price = (dahlia * quantity_flowers)

if flower_type == "Tulips" and quantity_flowers > 80:
    flower_price = (tulip * quantity_flowers) * 0.85
elif flower_type == "Tulips" and quantity_flowers <= 80:
    flower_price = (tulip * quantity_flowers)


if flower_type == "Narcissus" and quantity_flowers < 120:
    flower_price = (narcissus * quantity_flowers) * 1.15
elif flower_type == "Narcissus" and quantity_flowers >= 120:
    flower_price = (narcissus * quantity_flowers)

if flower_type == "Gladiolus" and quantity_flowers < 80:
    flower_price = (gladiolus * quantity_flowers) * 1.2
elif flower_type == "Gladiolus" and quantity_flowers >= 80:
    flower_price = (gladiolus * quantity_flowers)
left_sum = abs(budget - flower_price)
# Print output

if budget >= flower_price:
    print(f"Hey, you have a great garden with {quantity_flowers} {flower_type} and {left_sum:.2f} leva left.")
else:
    print(f"Not enough money, you need {left_sum:.2f} leva more.")