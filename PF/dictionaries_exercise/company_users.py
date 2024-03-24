command = input()
companies_workers = {}
while command != "End":
    company_name, employee_id = command.split(" -> ")
    if company_name in companies_workers:
        if employee_id not in companies_workers[company_name]:
            companies_workers[company_name].append(employee_id)
    else:
        companies_workers[company_name] = [employee_id]
    command = input()

for company, workers in companies_workers.items():
    print(f"{company}")
    for worker in workers:
        print(f"-- {worker}")
