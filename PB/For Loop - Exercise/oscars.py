# Read user input
actor_name = input()
academy_points = float(input())
number_jury = int(input())
all_points = 0
current_points = 0
are_enough = False
# Logic
for i in range(number_jury):
    jury_name = input()
    jury_points = float(input())
    bonus_points = (jury_points * len(jury_name)) / 2
    current_points += bonus_points
    all_points = current_points + academy_points
    if all_points > 1250.5:
        are_enough = True
        break
difference = abs(all_points - 1250.5)
# Print output
if are_enough:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {all_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")