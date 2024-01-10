def loading_bar(some_number: int):
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    number_divider = some_number // 10
    return f"{some_number}% [{'%' * number_divider}{'.' * (10 - number_divider)}]\nStill loading..."


number = int(input())
print(loading_bar(number))
