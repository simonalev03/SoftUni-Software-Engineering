year = int(input())
year += 1
while True:
    year_string = str(year)
    if len(set(year_string)) == len(year_string):
        print(year)
        break
    year += 1
