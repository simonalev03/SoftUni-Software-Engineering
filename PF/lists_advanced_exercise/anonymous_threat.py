strings = input().split()
command = input().split()
while command[0] != "3:1":
    command = input().split()

    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        
    elif command[0] == "divide":
        number_index = int(command[1])
        partitions = int(command[2])
