# Read user input
from math import ceil

number_of_people = int(input())
entry_price = float(input())
price_per_lounge = float(input())
price_per_umbrella = float(input())
# Logic
entry_price_for_all_people = number_of_people * entry_price
number_of_umbrellas = ceil(number_of_people * 75 / 100)
number_of_lounges = ceil(number_of_people * 50 / 100)
final_umbrella_price = number_of_umbrellas * price_per_umbrella
final_lounge_price = number_of_lounges * price_per_lounge
final_sum = entry_price_for_all_people + final_umbrella_price + final_lounge_price


# Print output
print(f"{final_sum:.2f} lv.")