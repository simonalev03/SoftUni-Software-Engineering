#Read user input
day = input()
user_output = ""
#Logic

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    user_output = "Working day"
elif day == "Saturday" or day == "Sunday":
    user_output = "Weekend"
else:
    user_output = "Error"
#Print output
print(user_output)