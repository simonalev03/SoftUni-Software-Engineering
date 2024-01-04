number = int(input())
day_of_week = ""
if number == 1:
    day_of_week = "Monday"
elif number == 2:
    day_of_week = "Tuesday"
elif number == 3:
    day_of_week = "Wednesday"
elif number == 4:
    day_of_week = "Thursday"
elif number == 5:
    day_of_week = "Friday"
elif number == 6:
    day_of_week = "Saturday"
elif number == 7:
    day_of_week = "Sunday"
else:
    day_of_week = "Error"
#Print output
print(day_of_week)