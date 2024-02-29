total_days = int(input())
plunder_per_day = int(input())
expected_end_plunder = int(input())
total_plunder = 0
for current_day in range(1, total_days + 1):
    total_plunder += plunder_per_day
    if current_day % 3 == 0:
        total_plunder += plunder_per_day * 0.5
    if current_day % 5 == 0:
        total_plunder -= total_plunder * 0.3

percentage = (total_plunder / expected_end_plunder) * 100
if total_plunder >= expected_end_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {percentage:.2f}% of the plunder.")


