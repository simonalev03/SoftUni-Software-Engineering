number = int(input())

for rows in range(number):
    for columns in range(rows):
        print("*", end="")
    print()
for rows in range(number):
    for columns in range(rows, number):
        print("*", end="")
    print()


