current_year = int(input())
new_year = current_year + 1
while True:
    if len(set(str(new_year))) == len(str(current_year)):
        print(new_year)
        break
    new_year += 1