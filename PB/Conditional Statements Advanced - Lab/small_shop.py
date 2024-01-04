#Read user input
product = input()
town = input()
quantity = float(input())
total_price = 0

#Logic
coffee_price_sofia = 0.50
water_price_sofia = 0.80
beer_price_sofia = 1.20
sweets_price_sofia = 1.45
peanuts_price_sofia = 1.60
coffee_price_plovdiv = 0.40
water_price_plovdiv = 0.70
beer_price_plovdiv = 1.15
sweets_price_plovdiv = 1.30
peanuts_price_plovdiv = 1.50
coffee_price_varna = 0.45
water_price_varna = 0.70
beer_price_varna = 1.10
sweets_price_varna = 1.35
peanuts_price_varna = 1.55

if town == "Sofia":
    if product == "coffee":
        total_price = quantity * coffee_price_sofia
    elif product == "water":
        total_price = quantity * water_price_sofia
    elif product == "beer":
        total_price = quantity * beer_price_sofia
    elif product == "sweets":
        total_price = quantity * sweets_price_sofia
    elif product == "peanuts":
        total_price = quantity * peanuts_price_sofia

elif town == "Plovdiv":
    if product == "coffee":
        total_price = quantity * coffee_price_plovdiv
    elif product == "water":
        total_price = quantity * water_price_plovdiv
    elif product == "beer":
        total_price = quantity * beer_price_plovdiv
    elif product == "sweets":
        total_price = quantity * sweets_price_plovdiv
    elif product == "peanuts":
        total_price = quantity * peanuts_price_plovdiv
elif town == "Varna":
    if product == "coffee":
        total_price = quantity * coffee_price_varna
    elif product == "water":
        total_price = quantity * water_price_varna
    elif product == "beer":
        total_price = quantity * beer_price_varna
    elif product == "sweets":
        total_price = quantity * sweets_price_varna
    elif product == "peanuts":
        total_price = quantity * peanuts_price_varna
#Print output
print(total_price)