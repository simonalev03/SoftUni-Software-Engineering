number_of_messages = int(input())

message = ""
for message_number in range(number_of_messages):
    message_type = int(input())
    if message_type == 88:
        message = "Hello"
    elif message_type == 86:
        message = "How are you?"
    elif message_type < 88:
        message = "GREAT!"
    else:
        message = "Bye."
    print(message)