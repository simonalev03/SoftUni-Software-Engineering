countries = input().split(", ")
capitals = input().split(", ")
country_capital = {countries[index]: capitals[index] for index in range(len(countries))}
for country, capital in country_capital.items():
    print(f"{country} -> {capital}")