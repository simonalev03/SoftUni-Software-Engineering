#Read user input
hour = int(input())
day = input()
#Logic
result = ""
if 10 <= hour <= 18 and (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday"\
    or day == "Friday"or day == "Saturday"):
    result = "open"
else:
    result = "closed"
#Print output
print(result)