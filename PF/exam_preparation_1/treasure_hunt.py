shopping_list = input().split("!")
command_as_str = input()

while command_as_str != "Go Shopping!":
    command = command_as_str.split()
    if command[0] == "Urgent":
        if command[1] not in shopping_list:
            shopping_list.insert(0, command[1])
    elif command[0] == "Unnecessary":
        if command[1] in shopping_list:
            shopping_list.remove(command[1])
    elif command[0] == "Correct":
        if command[1] in shopping_list:
            item_index = shopping_list.index(command[1])
            shopping_list[item_index] = command[2]
    elif command[0] == "Rearrange":
        if command[1] in shopping_list:
            item_index = shopping_list.index(command[1])
            shopping_list.append(shopping_list.pop(item_index))

    command_as_str = input()
print(*shopping_list, sep=", ")
