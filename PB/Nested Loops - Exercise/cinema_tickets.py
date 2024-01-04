student_ticket = 0
standard_ticket = 0
kid_ticket = 0
movie_name = input()
while movie_name != "Finish":
    free_space = int(input())
    sold_seats = 0
    for free_ticket in range(free_space):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_ticket += 1
        elif ticket_type == "standard":
            standard_ticket += 1
        elif ticket_type == "kid":
            kid_ticket += 1
        sold_seats += 1
    percent_full_hall = sold_seats / free_space * 100
    print(f"{movie_name} - {percent_full_hall:.2f}% full.")
    movie_name = input()
total_tickets_sold = student_ticket + standard_ticket + kid_ticket
student_ticket_percent = student_ticket / total_tickets_sold * 100
standard_ticket_percent = standard_ticket / total_tickets_sold * 100
kid_ticket_percent = kid_ticket / total_tickets_sold * 100

print(f"Total tickets: {total_tickets_sold}")
print(f"{student_ticket_percent:.2f}% student tickets.")
print(f"{standard_ticket_percent:.2f}% standard tickets.")
print(f"{kid_ticket_percent:.2f}% kids tickets.")


