group_size = int(input())
total_days = int(input())
coins = 0
if 1 <= group_size <= 100 and 1 <= total_days <= 100:
    for day in range(1, total_days + 1):
        if day % 10 == 0:
            group_size -= 2
        if day % 15 == 0:
            group_size += 5
        coins += 50 - (group_size * 2)
        if day % 3 == 0:
            coins -= (group_size * 3)
        if day % 5 == 0:
            coins += (group_size * 20)
            if day % 3 == 0:
                coins -= (group_size * 2)
shared_coins = int(coins / group_size)
print(f"{group_size} companions received {shared_coins} coins each.")

