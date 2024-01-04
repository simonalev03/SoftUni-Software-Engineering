# Read user input
days = int(input())
room = input()
review = input()
# Logic
nights = days - 1
apartment_price = 25
president_apartment_price = 35
room_for_one_person_price = 18
price = 0
if room == "apartment":
    if days < 10:
        price = (apartment_price * nights) * 0.7
    elif days > 10  and days <= 15:
        price = (apartment_price * nights) * 0.65
    else:
        price = (apartment_price * nights) * 0.5
elif room == "president apartment":
    if days < 10:
        price = (president_apartment_price * nights) * 0.9
    elif days > 10 and days <= 15:
        price = (president_apartment_price * nights) * 0.85
    else:
        price = (president_apartment_price * nights) * 0.8
else:
    price = room_for_one_person_price * nights
if review == "positive":
    price *= 1.25
else:
    price *= 0.9
print(f"{price:.2f}")
# Print output
