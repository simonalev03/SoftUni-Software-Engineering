# Read user input
month = input()
nights = int(input())
# Logic
studio = 0
apartment = 0
price_studio = 0
price_apartment = 0
if month == "May" or month == "October":
    studio = 50
    apartment = 65
    price_studio = nights * studio
    price_apartment = nights * apartment
    if 7 < nights <= 14:
        studio *= 0.95
        price_studio = nights * studio
    elif nights > 14:
        studio *= 0.7
        price_studio = nights * studio
        apartment *= 0.9
        price_apartment = nights * apartment
elif month == "June" or month == "September":
    studio = 75.2
    apartment = 68.7
    price_studio = nights * studio
    price_apartment = nights * apartment
    if nights > 14:
        studio *= 0.8
        price_studio = nights * studio
        apartment *= 0.9
        price_apartment = nights * apartment
else:
    studio = 76
    apartment = 77
    price_studio = nights * studio
    price_apartment = nights * apartment
    if nights > 14:
        apartment *= 0.9
        price_apartment = nights * apartment
# Print output
print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
