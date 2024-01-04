book = input()
number_of_books = 0
while True:
    other_books = input()
    if other_books == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {number_of_books} books.")
        break
    elif book == other_books:
        print(f"You checked {number_of_books} books and found it.")
        break
    else:
        number_of_books += 1