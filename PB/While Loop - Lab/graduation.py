# Read user input
name = input()
fails = 0
year = 1
average_grade = 0
# Logic
while True:
    grade = float(input())
    if grade < 4:
        fails += 1
        if fails > 1:
            print(f"{name} has been excluded at {year} grade")
            break
    else:
        year += 1
        average_grade += grade / 12
    if year > 12:
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break

# Print output