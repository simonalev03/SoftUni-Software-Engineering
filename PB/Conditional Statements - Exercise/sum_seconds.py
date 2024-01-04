from math import floor
#Read user input
time_first = int(input())
time_second = int(input())
time_third = int(input())
#Logic
sum_seconds = (time_first + time_second + time_third)
minutes = sum_seconds // 60
seconds = sum_seconds % 60
floor(minutes)

if seconds < 10:
    print(f"{minutes}:{seconds:02d}")
else:
    print(f"{minutes}:{seconds}")
#Print output