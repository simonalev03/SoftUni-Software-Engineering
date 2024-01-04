# Read user input
unsatisfying_grades = int(input())
bad_mark = 0
sum_grade = 0
problems = 0
last_problem_solved = ""
is_failed = False
question = input()
# Logic
while question != "Enough":
    grade = int(input())
    if grade <= 4:
        bad_mark += 1
        if bad_mark >= unsatisfying_grades:
            is_failed = True
            break
    problems += 1
    sum_grade += grade
    last_problem_solved = question
    question = input()
if is_failed:
    print(f"You need a break, {bad_mark} poor grades.")
else:
    sum_grade /= problems
    print(f"Average score: {sum_grade:.2f}")
    print(f"Number of problems: {problems}")
    print(f"Last problem: {last_problem_solved}")



# Print output




