number_of_students = int(input())
sum_grade = 0
failed_students = 0
poor_students = 0
avg_students = 0
excellent_students = 0
for student in range(number_of_students):
    grade = float(input())
    sum_grade += grade
    if 2 <= grade <= 2.99:
        failed_students += 1
    elif 3 <= grade <= 3.99:
        poor_students += 1
    elif 4 <= grade <= 4.99:
        avg_students += 1
    elif 5 <= grade:
        excellent_students += 1
avg_grade = sum_grade / number_of_students
failed_students_percent = failed_students / number_of_students * 100
poor_students_percent = poor_students / number_of_students * 100
avg_students_percent = avg_students / number_of_students * 100
excellent_students_percent = excellent_students / number_of_students * 100

print(f"Top students: {excellent_students_percent:.2f}%")
print(f"Between 4.00 and 4.99: {avg_students_percent:.2f}%")
print(f"Between 3.00 and 3.99: {poor_students_percent:.2f}%")
print(f"Fail: {failed_students_percent:.2f}%")
print(f"Average: {avg_grade:.2f}")


