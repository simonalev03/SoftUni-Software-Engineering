elements = input().split()
moves = 0

while True:
    moves += 1
    command = input().split()
    if command[0] == "end":
        print("Sorry you lose :(")
        print(*elements)
        break
    elif command[0] == command[1] or (int(command[0]) >= len(elements) or int(command[1]) >= len(elements)) or \
            int(command[0]) < 0 or int(command[1]) < 0:
        middle_of_the_elements = len(elements) // 2
        elements.insert(middle_of_the_elements, f"-{moves}a")
        elements.insert(middle_of_the_elements + 1, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif elements[int(command[0])] == elements[int(command[1])]:
        found_first_element = elements[int(command[0])]
        found_second_element = elements[int(command[1])]
        found_first_element_index = elements.index(found_first_element)
        elements.pop(found_first_element_index)
        found_second_element_index = elements.index(found_second_element)
        elements.pop(found_second_element_index)
        print(f"Congrats! You have found matching elements - {found_first_element}!")
    elif elements[int(command[0])] != elements[int(command[1])]:
        print("Try again!")
    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break
