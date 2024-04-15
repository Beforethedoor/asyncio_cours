from collections import deque

messages = deque([1, 2, 3, 4, 5])


def process_message(msg):
    pass


while messages:
    if messages:
        message = messages.pop()
        process_message(message)
