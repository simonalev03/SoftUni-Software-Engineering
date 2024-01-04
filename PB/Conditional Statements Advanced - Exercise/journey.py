#Read user input
budget = float(input())
season = input()
#Logic
place = ""
region = ""
if budget <= 100:
    region = "Bulgaria"
    if season == "summer":
        budget *= 0.3
        place = "Camp"
    elif season == "winter":
        budget *= 0.7
        place = "Hotel"
elif budget <= 1000:
    region = "Balkans"
    if season == "summer":
        budget *= 0.4
        place = "Camp"
    elif season == "winter":
        budget *= 0.8
        place = "Hotel"
else:
    region = "Europe"
    budget *= 0.9
    place = "Hotel"

#Print output
print(f"Somewhere in {region}")
print(f" {place} - {budget:.2f}")