#Read user input
day = input()
ticket_price = 0
#Logic
if day == "Monday" or day == "Tuesday" or day == "Friday":
    ticket_price = 12
elif day == "Wednesday" or day == "Thursday":
    ticket_price = 14
elif day == "Saturday" or day == "Sunday":
    ticket_price = 16
#Print output
print(ticket_price)