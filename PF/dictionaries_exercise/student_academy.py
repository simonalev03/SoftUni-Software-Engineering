student_grades = {}

students_count = int(input())
for current_student in range(students_count):
    student_name = input()
    student_grade = float(input())
    if student_name in student_grades:
        student_grades[student_name].append(student_grade)
    else:
        student_grades[student_name] = [student_grade]
student_with_above_avg_grades = {}
for student_name, grades in student_grades.items():
    average_grade = sum(grades) / len(grades)
    student_grades[student_name] = average_grade
    if student_grades[student_name] >= 4.50:
        student_with_above_avg_grades[student_name] = average_grade

for student_name, avg_grade in student_with_above_avg_grades.items():
    print(f"{student_name} -> {avg_grade:.2f}")

del student_grades
