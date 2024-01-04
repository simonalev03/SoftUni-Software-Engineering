#Read user input
food = input()
type_food = ""
#Logic
if food == "banana" or food == "apple" or food == "kiwi" or food == "cherry" or food == "lemon" or food == "grapes":
    type_food = "fruit"
elif food == "tomato" or food == "cucumber" or food == "pepper" or food == "carrot":
    type_food = "vegetable"
else:
    type_food = "unknown"
#Print output
print(type_food)