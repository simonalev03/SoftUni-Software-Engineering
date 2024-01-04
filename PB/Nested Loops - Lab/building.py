floors_number = int(input())
rooms_number = int(input())

for floor in range(floors_number, 0, -1):
    for room in range(rooms_number):
        if floor == floors_number:
            print(f"L{floor}{room} ", end= "")
        elif floor % 2 == 0:
            print(f"O{floor}{room} ", end= "")
        else:
            print(f"A{floor}{room} ", end= "")
    print()
