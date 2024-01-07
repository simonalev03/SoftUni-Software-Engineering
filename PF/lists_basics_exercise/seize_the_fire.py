levels_of_fire = input().split("#")
water = int(input())
total_fire = 0
effort = 0
extinguished_cells = ["Cells:"]
for current_fire in levels_of_fire:
    fire = current_fire.split(" = ")
    fire_threat = fire[0]
    fire_value = int(fire[1])
    if fire_threat == "High" and 81 <= fire_value <= 125 and water - fire_value >= 0:
        water -= fire_value
        effort += fire_value * 0.25
        total_fire += fire_value
        extinguished_cells.append(" - " + str(fire_value))
    elif fire_threat == "Medium" and 51 <= fire_value <= 80 and water - fire_value >= 0:
        water -= fire_value
        effort += fire_value * 0.25
        total_fire += fire_value
        extinguished_cells.append(" - " + str(fire_value))
    elif fire_threat == "Low" and 1 <= fire_value <= 50 and water - fire_value >= 0:
        water -= fire_value
        effort += fire_value * 0.25
        total_fire += fire_value
        extinguished_cells.append(" - " + str(fire_value))
print(*extinguished_cells, sep="\n")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
