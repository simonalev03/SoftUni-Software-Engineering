users_dictionary = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        force_side, user = command.split(" | ")
        is_user_part_of_force = False
        for value in users_dictionary.values():
            if user in value:
                is_user_part_of_force = True
                break
        if not is_user_part_of_force:
            if force_side not in users_dictionary.keys():
                users_dictionary[force_side] = []
            users_dictionary[force_side].append(user)

    elif "->" in command:
        user, force_side = command.split(" -> ")
        for value in users_dictionary.values():
            if user in value:
                value.remove(user)
                break
        if force_side not in users_dictionary.keys():
            users_dictionary[force_side] = []
        users_dictionary[force_side].append(user)
        print(f"{user} joins the {force_side} side!")
    command = input()

for force_side, force_users in users_dictionary.items():
    if len(force_users) > 0:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for current_user in force_users:
            print(f"! {current_user}")
