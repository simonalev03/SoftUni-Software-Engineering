#Read user input
animal = input()
animal_type = ""
#Logic
if animal == "dog":
    animal_type = "mammal"
elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    animal_type = "reptile"
else:
    animal_type = "unknown"
print(animal_type)
#Print output
