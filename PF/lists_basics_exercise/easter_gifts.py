gifts = input().split()
command = input().split()

while command[0] != "No" and command[1] != "Money":
    if command[0] == "OutOfStock":
        item = command[1]
        for gift in gifts:
            if gift == item:
                gift_to_replace = gifts.index(gift)
                gifts[gift_to_replace] = "None"
    elif command[0] == "Required":
        item = command[1]
        if 0 < int(command[2]) < len(gifts):
            gifts[int(command[2])] = item
    elif command[0] == "JustInCase":
        item = command[1]
        gifts[-1] = item
    command = input().split()
for gift in gifts:
    if gift != "None":
        print(gift, end=" ")
