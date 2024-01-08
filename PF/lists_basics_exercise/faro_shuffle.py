cards = input().split()
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    middle_of_deck = len(cards) // 2
    left_part = cards[:middle_of_deck]
    right_part = cards[middle_of_deck:]
    deck_after_shuffle = []
    for card_index in range(len(left_part)):
        deck_after_shuffle.append(left_part[card_index])
        deck_after_shuffle.append(right_part[card_index])
    cards = deck_after_shuffle
print(cards)
