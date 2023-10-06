number_of_people = int(input())
season = input()
excursion_price = 0
if number_of_people <= 5:
    if season == "spring":
       excursion_price = number_of_people * 50
    elif season == "summer":
        excursion_price = (number_of_people * 48.5) * 0.85
    elif season == "autumn":
        excursion_price = number_of_people * 60
    elif season == "winter":
        excursion_price = (number_of_people * 86) * 1.08
else:
    if season == "spring":
        excursion_price = number_of_people * 48
    elif season == "summer":
        excursion_price = (number_of_people * 45) * 0.85

    elif season == "autumn":
        excursion_price = number_of_people * 49.5
    elif season == "winter":
        excursion_price = (number_of_people * 85) * 1.08

print(f"{excursion_price:.2f} leva.")