list_of_numbers = [int(number) for number in input().split()]
while True:
    command = input().split()
    if command[0] == "end":
        break
    elif command[0] == "swap":
        list_of_numbers[int(command[1])], list_of_numbers[int(command[2])] \
            = list_of_numbers[int(command[2])], list_of_numbers[int(command[1])]
    elif command[0] == "multiply":
        list_of_numbers[int(command[1])] = list_of_numbers[int(command[1])] * list_of_numbers[int(command[2])]
    elif command[0] == "decrease":
            list_of_numbers = [number - 1 for number in list_of_numbers]

print(*list_of_numbers,sep=", ")
