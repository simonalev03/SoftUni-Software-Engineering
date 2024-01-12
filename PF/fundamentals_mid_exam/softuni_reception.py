first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())
hourly_accepted_requests = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
time_needed = students_count // hourly_accepted_requests
if students_count % hourly_accepted_requests != 0:
    time_needed += 1

for current_hour in range(1, time_needed + 1):
    students_count -= hourly_accepted_requests
    if current_hour % 3 == 0 and students_count != 0:
        time_needed += 1
print(f"Time needed: {time_needed}h.")
