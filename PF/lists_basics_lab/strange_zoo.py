animal = []
head = input()
body = input()
tail = input()
animal.append(head)
animal.append(body)
animal.append(tail)
animal[0], animal[2] = animal[2], animal[0]
print(animal)