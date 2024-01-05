number_of_balls = int(input())
highest_value = 0
best_ball_weight = 0
best_ball_time_to_make = 0
best_ball_quality = 0
if 0 <= number_of_balls <= 100:
    for snowball in range(1, number_of_balls + 1):
        current_value = 0
        snowball_weight = int(input())
        time_to_make = int(input())
        snowball_quality = int(input())
        if 0 <= snowball_weight <= 1000 and \
                1 <= time_to_make <= 500 and \
                0 <= snowball_quality <= 100:
            current_value = int(snowball_weight / time_to_make) ** snowball_quality
            if current_value > highest_value:
                highest_value = current_value
                best_ball_weight = snowball_weight
                best_ball_time_to_make = time_to_make
                best_ball_quality = snowball_quality
print(f"{best_ball_weight} : {best_ball_time_to_make} = {highest_value} ({best_ball_quality})")


