to_do_tasks = []
while True:
    task = input()
    if task == "End":
        break
    to_do_tasks.append(task)
    #split_tasks = task.split("-")
sorted_todos = sorted(to_do_tasks, key=lambda x: int(x.split("-")[0]))
print([todo.split("-")[1] for todo in sorted_todos])