number_of_rooms = int(input())
free_chairs = 0
for room in range(1, number_of_rooms + 1):
    info_for_room = input().split()
    chairs = len(info_for_room[0])
    people = int(info_for_room[1])
    if chairs >= people:
        free_chairs += chairs - people
    else:
        needed_chairs_in_room = people - chairs
        free_chairs -= needed_chairs_in_room
        print(f"{needed_chairs_in_room} more chairs needed in room {room}")

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")