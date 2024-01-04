sum_saved = 0
is_enough = False
while True:
    sum_saved = 0
    destination = input()
    if destination == "End":
        break
    minimum_sum = float(input())
    while True:
        money_saved = float(input())
        sum_saved += money_saved
        if sum_saved >= minimum_sum:
            is_enough = True
            if is_enough:
                print(f"Going to {destination}!")
                break

