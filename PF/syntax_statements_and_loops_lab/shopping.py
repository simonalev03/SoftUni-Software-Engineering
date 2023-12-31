budget = int(input())
while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    expense = int(command)
    budget -= expense
    if budget < 0:
        print("You went in overdraft!")
        break



