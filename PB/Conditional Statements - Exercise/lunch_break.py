from math import ceil

#Read user input
show_name = input()
duration_episode = int(input())
duration_break = int(input())
#Logic
break_time = duration_break * (1/8)
chill_time = duration_break * (1/4)
free_time = duration_break - (break_time + chill_time)
duration_break = ceil(abs(free_time - duration_episode))
#Print output
if free_time >= duration_episode:
    print(f"You have enough time to watch {show_name} and left with {duration_break} minutes free time.")
else:
    print(f"You don't have enough time to watch {show_name}, you need {duration_break} more minutes.")