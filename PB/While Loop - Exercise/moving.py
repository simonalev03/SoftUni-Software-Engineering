# Read user input
width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())
total_free_space = width_free_space * length_free_space * height_free_space
number_of_boxes = 0
is_house_full = False
are_boxes_moved = False
# Logic

while True:
    user_input = input()
    if user_input == "Done":
        are_boxes_moved = True
        break
    boxes_moved = int(user_input)
    number_of_boxes += boxes_moved
    if number_of_boxes >= total_free_space:
        is_house_full = True
        break
difference = abs(total_free_space - number_of_boxes)
# Print output
if are_boxes_moved:
    print(f"{difference} Cubic meters left.")
else:
    print(f"No more free space! You need {difference} Cubic meters more.")
