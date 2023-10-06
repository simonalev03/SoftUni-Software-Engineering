film_name = input()
hall_type = input()
number_of_tickets_sold = int(input())
film_profit = 0
if hall_type == "normal":
    if film_name == "A Star Is Born":
        film_profit = number_of_tickets_sold * 7.50
    elif film_name == "Bohemian Rhapsody":
        film_profit = number_of_tickets_sold * 7.35
    elif film_name == "Green Book":
        film_profit = number_of_tickets_sold * 8.15
    else:
        film_profit = number_of_tickets_sold * 8.75
elif hall_type == "luxury":
    if film_name == "A Star Is Born":
        film_profit = number_of_tickets_sold * 10.50
    elif film_name == "Bohemian Rhapsody":
        film_profit = number_of_tickets_sold * 9.45
    elif film_name == "Green Book":
        film_profit = number_of_tickets_sold * 10.25
    else:
        film_profit = number_of_tickets_sold * 11.55
else:
    if film_name == "A Star Is Born":
        film_profit = number_of_tickets_sold * 13.50
    elif film_name == "Bohemian Rhapsody":
        film_profit = number_of_tickets_sold * 12.75
    elif film_name == "Green Book":
        film_profit = number_of_tickets_sold * 13.25
    else:
        film_profit = number_of_tickets_sold * 13.95

print(f"{film_name} -> {film_profit:.2f} lv.")

