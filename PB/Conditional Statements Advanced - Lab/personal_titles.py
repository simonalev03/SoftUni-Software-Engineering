#Read user input
age = float(input())
gender = input()
title = ""
#Logic
if age >= 16 and gender == "m":
    title = "Mr."
elif age < 16 and gender == "m":
    title = "Master"
elif age >= 16 and gender == "f":
    title = "Ms."
elif age < 16 and gender == "f":
    title = "Miss"
#Print output
print(title)