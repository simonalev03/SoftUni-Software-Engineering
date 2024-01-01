number_of_messages = int(input())

message = ""
for message_number in range(number_of_messages):
    chat_code = int(input())
    if chat_code == 88:
        message = "Hello"
    elif chat_code == 86:
        message = "How are you?"
    elif chat_code < 88:
        message = "GREAT!"
    else:
        message = "Bye."
    print(message)