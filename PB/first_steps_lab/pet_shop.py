one_package_dog_food = 2.50
one_package_cat_food = 4

number_of_dog_packages = int(input())
number_of_cat_packages = int(input())

price = (number_of_dog_packages * one_package_dog_food) + (number_of_cat_packages * one_package_cat_food)
result = f"{price} lv."

print(result)