number_of_people = int(input())
elevator_capacity = int(input())
courses = int(number_of_people / elevator_capacity)
left = number_of_people % elevator_capacity
if left % elevator_capacity != 0:
    courses += 1
print(courses)



