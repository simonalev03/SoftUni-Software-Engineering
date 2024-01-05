lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
broken_helmet = 0
broken_sword = 0
broken_shield = 0
broken_armor = 0
if 0 <= helmet_price <= 1000 and \
        0 <= sword_price <= 1000 \
        and 0 <= shield_price <= 1000 \
        and 0 <= armor_price <= 1000 \
        and 0 <= lost_fights <= 1000:
    for lost_fight in range(1, lost_fights + 1):
        if lost_fight % 2 == 0:
            broken_helmet += 1
        if lost_fight % 3 == 0:
            broken_sword += 1
            if lost_fight % 2 == 0:
                broken_shield += 1
                if broken_shield % 2 == 0:
                    broken_armor += 1
expenses = (broken_helmet * helmet_price) + \
           (broken_sword * sword_price) + \
           (broken_shield * shield_price) + \
           (broken_armor * armor_price)
print(f"Gladiator expenses: {expenses:.2f} aureus")
