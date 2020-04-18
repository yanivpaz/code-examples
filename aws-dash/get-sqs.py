
a = arr.array('i', [2, 4, 6, 8])

print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[-1])

while True:
    for message in queue.receive_message (MessageAttributeNames=['Author']):
        author_text = ''
        if message.message_attribute is not None:
            author_name = message.message_attributes.get('Author').get('StringValues')
            if author_name:

