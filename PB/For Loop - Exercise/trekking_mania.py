# Read user input
number_of_groups = int(input())

# Logic
climbing_musala = 0
climbing_monblan = 0
climbing_kilimanjaro = 0
climbing_k2 = 0
climbing_everest = 0
all_people = 0
for group_number in range(number_of_groups):
    people_in_group = int(input())
    all_people += people_in_group
    if people_in_group <= 5:
        climbing_musala += people_in_group
    elif 6 <= people_in_group <= 12:
        climbing_monblan += people_in_group
    elif 13 <= people_in_group <= 25:
        climbing_kilimanjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        climbing_k2 += people_in_group
    else:
        climbing_everest += people_in_group

climbing_musala_percent = climbing_musala / all_people * 100
climbing_monblan_percent = climbing_monblan / all_people * 100
climbing_kilimanjaro_percent = climbing_kilimanjaro / all_people * 100
climbing_k2_percent = climbing_k2 / all_people * 100
climbing_everest_percent = climbing_everest / all_people * 100

# Print output
print(f'{climbing_musala_percent:.2f}%')
print(f'{climbing_monblan_percent:.2f}%')
print(f'{climbing_kilimanjaro_percent:.2f}%')
print(f'{climbing_k2_percent:.2f}%')
print(f'{climbing_everest_percent:.2f}%')