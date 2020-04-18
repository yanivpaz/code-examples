
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
                author_text = ' ({0})'.format(author_name)
        else:
          print ('message from IOT : {0}'.format (message.body))
          data = json.loads(message.body)
          if data["serialNumber"] == "GG"
             data["username"] = "yaniv"
          clickType = data["clickType"]
          if clickType == "SINGLE"
            print ("Recedived SINGLE");
            message.delete()
            data["cmp"] = "XXX"
          elif clickType == "DOUBLE"
            print ("Recedived SINGLE");
            message.delete()
            data["cmp"] = "YYY"
            subprocess.call ("run_command",shell=True)
          elif clickType == "LONG"
            print ("Recedived SINGLE");
            message.delete()
            data["cmp"] = "YYY"
            subprocess.call ("run_command",shell=True)
    time.sleep (2)
