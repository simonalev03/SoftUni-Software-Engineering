usernames = {}
programming_languages = {}

while True:
    command = input()
    if "-" not in command:
        break

    info = command.split("-")
    if len(info) == 3:
        username, language, points = info[0], info[1], info[2]
        if username not in usernames.keys():
            usernames[username] = []
        usernames[username].append(int(points))
        for current_points in usernames[username]:
            if len(usernames[username]) > 1:
                points_to_remove = min(usernames[username])
                usernames[username].remove(points_to_remove)
        if language not in programming_languages.keys():
            programming_languages[language] = []
        programming_languages[language].append(points)

    elif len(info) == 2:
        username, status = info[0], info[1]
        for current_username in usernames.keys():
            if username == current_username:
                usernames.pop(current_username)
                break

print("Results:")
for username, points in usernames.items():
    print(f"{username} | {sum(points)}")

print("Submissions:")
for language, submissions in programming_languages.items():
    print(f"{language} - {len(submissions)}")