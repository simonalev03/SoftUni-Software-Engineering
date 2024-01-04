# Read user input


# Logic
goal_steps = 10000
total_steps = 0
while total_steps < goal_steps:
    command = input()
    if command == "Going home":
        last_steps = int(input())
        total_steps += last_steps
        break
    steps_walked = int(command)
    total_steps += steps_walked
diff = abs(goal_steps - total_steps)


# Print output
if total_steps >= goal_steps:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")