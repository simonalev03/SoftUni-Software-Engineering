all_courses = {}

command = input()
while command != "end":
    course, person = command.split(" : ")
    if course not in all_courses:
        all_courses[course] = [person]
    else:
        all_courses[course].append(person)
    command = input()

for course, people in all_courses.items():
    print(f"{course}: {len(people)}")
    for person in people:
        print(f"-- {person}")
        