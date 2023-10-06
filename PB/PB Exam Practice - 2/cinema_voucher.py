voucher_price = int(input())
number_of_purchases = 0
number_of_tickets = 0
first_number = 0
second_number = 0
ticket_price = 0
purchase_price = 0

while True:
    purchase = input()
    if purchase == "End":
        break
    if len(purchase) > 8:
        number_of_tickets += 1
        first_number = ord(purchase[0])
        second_number = ord(purchase[1])
        ticket_price += first_number + second_number
        voucher_price -= ticket_price
        if voucher_price <= 0:
            break
    else:
        number_of_purchases += 1
        purchase_price += ord(purchase[0])
        ticket_price -= purchase_price
        if ticket_price <= 0:
            break
print(number_of_tickets)
print(number_of_purchases)