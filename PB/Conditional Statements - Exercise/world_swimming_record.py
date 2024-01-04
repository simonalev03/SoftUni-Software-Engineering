from math import floor
# Read user input
record_seconds = float(input())
distance_meters = float(input())
time_for_1_meter_swim_seconds = float(input())
# Logic

distance = distance_meters * time_for_1_meter_swim_seconds
friction = floor(distance_meters / 15) * 12.5
total_time = distance + friction
remaining_seconds = abs(record_seconds - total_time)
# Print output

if total_time < record_seconds:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {remaining_seconds:.2f} seconds slower.")

