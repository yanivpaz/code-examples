
#!/usr/bin/python
import boto3
import time
import subprocess 
from datetime import  datetime
import json

sqs = boto3.resource ('sqs')
queue = sqs.get_queue_by_name(QueueName='YanivSQS')

while True:
    for message in queue.receive_message (MessageAttributeNames=['Author']):
        author_text = ''
        if message.message_attribute is not None:
            author_name = message.message_attributes.get('Author').get('StringValues')
            if author_name:

