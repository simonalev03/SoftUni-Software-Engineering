pirate_ship_status = [int(current_part) for current_part in input().split(">")]
warship_status = [int(current_warship_part) for current_warship_part in input().split(">")]
ship_section_max_health = int(input())
command = input().split()
is_game_over = False
while command[0] != "Retire":
    if command[0] == "Fire":
        if 0 <= int(command[1]) < len(warship_status):
            warship_status[(int(command[1]))] -= int(command[2])
            if warship_status[(int(command[1]))] <= 0:
                print("You won! The enemy ship has sunken.")
                is_game_over = True
                break

    elif command[0] == "Defend":
        if 0 <= int(command[1]) <= int(command[2]) < len(pirate_ship_status):
            for current_part in range(int(command[1]), int(command[2]) + 1):
                pirate_ship_status[current_part] -= int(command[3])
                if pirate_ship_status[current_part] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    is_game_over = True
                    break
            if is_game_over:
                break

    elif command[0] == "Repair":
        if 0 <= int(command[1]) < len(pirate_ship_status):
            pirate_ship_status[(int(command[1]))] += int(command[2])
            if pirate_ship_status[(int(command[1]))] > ship_section_max_health:
                pirate_ship_status[(int(command[1]))] = ship_section_max_health
    elif command[0] == "Status":
        repair_section_counter = 0
        for current_part in pirate_ship_status:
            if current_part < ship_section_max_health * 0.2:
                repair_section_counter += 1
        print(f"{repair_section_counter} sections need repair.")
    command = input().split()

if not is_game_over:
    pirate_ship_sum = sum(pirate_ship_status)
    warship_sum = sum(warship_status)
    print(f"Pirate ship status: {pirate_ship_sum}\nWarship status: {warship_sum}")
