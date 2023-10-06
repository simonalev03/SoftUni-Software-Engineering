number_of_pages = int(input())
pages_read_per_hour = int(input())
number_of_days = int(input())

amount_of_hours = (number_of_pages // pages_read_per_hour) // number_of_days

print(amount_of_hours)