employees_happiness = [int(happiness) for happiness in input().split()]
happiness_improvement_factor = int(input())
new_employees_happiness = []
for employee in employees_happiness:
    new_employees_happiness.append(employee * happiness_improvement_factor)
avg_happiness = sum(new_employees_happiness) // len(employees_happiness)
happiness_score = 0
for employee in new_employees_happiness:
    if employee > avg_happiness:
        happiness_score += 1
if happiness_score < len(new_employees_happiness) // 2:
    print(f"Score: {happiness_score}/{len(new_employees_happiness)}. Employees are not happy!")
else:
    print(f"Score: {happiness_score}/{len(new_employees_happiness)}. Employees are happy!")
