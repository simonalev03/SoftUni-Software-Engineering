number_of_lines = int(input())
tank_capacity = 255
total_liters_filled = 0
for water in range(number_of_lines):
    added_water = int(input())
    if tank_capacity - added_water < 0:
        print("Insufficient capacity!")
        continue
    tank_capacity -= added_water
    total_liters_filled += added_water
print(total_liters_filled)



