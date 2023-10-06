target_profit = int(input())
current_profit = 0
is_target_reached = False
while True:
    type_of_service = input()
    if type_of_service == "closed":
        break
    if type_of_service == "haircut":
        type_of_cut = input()
        if type_of_cut == "mens":
            current_profit += 15
        elif type_of_cut == "ladies":
            current_profit += 20
        elif type_of_cut == "kids":
            current_profit += 10
    elif type_of_service == "color":
        type_of_color = input()
        if type_of_color == "touch up":
            current_profit += 20
        elif type_of_color == "full color":
            current_profit += 30
    if current_profit >= target_profit:
        is_target_reached = True
        break
if is_target_reached:
    print(f"You have reached your target for the day!")
else:
    diff = abs(current_profit - target_profit)
    print(f"Target not reached! You need {diff}lv. more.")

print(f"Earned money: {current_profit}lv.")
