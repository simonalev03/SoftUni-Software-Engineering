# Read user input

price_of_holiday = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())
# Logic

sum_toys = puzzles + dolls + teddy_bears + minions + trucks
price_puzzle = 2.60
price_doll = 3
price_teddy_bear = 4.10
price_minion = 8.20
price_truck = 2
price_toys = (puzzles * price_puzzle) + (dolls * price_doll) + (teddy_bears * price_teddy_bear) +\
             (minions * price_minion) + (trucks * price_truck)
if sum_toys >= 50:
    price_toys *= 0.75
price_toys *= 0.9
left_money = abs(price_toys - price_of_holiday)
# Print output

if price_toys >= price_of_holiday:
    print(f"Yes! {left_money:.2f} lv left.")
else:
    print(f"Not enough money! {left_money:.2f} lv needed.")
