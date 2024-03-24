phonebook = {}

while True:
    info = input().split("-")
    if len(info) < 2:
        break
    name = info[0]
    phone_number = info[1]
    phonebook[name] = phone_number

searched_people = int(*info)
for current_person in range(searched_people):
    person = input()
    if person in phonebook.keys():
        print(f"{person} -> {phonebook[person]}")
    else:
        print(f"Contact {person} does not exist.")
