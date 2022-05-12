from fbchat import Client
from fbchat.models import *
import configparser
import time


class MessageHandler:
    def __init__(self, recipient, text, hour, minute):
        self.recipient = recipient
        self.text = text
        self.hour = hour
        self.minute = minute
        self.delivered = False


config = configparser.ConfigParser()

config.read('config.ini')

# Prob not the best idea to plain-text this
user = config['DEFAULT']['Username']
password = config['DEFAULT']['Password']

client = Client(user, password)

print("Own id: {}".format(client.uid))

threads = client.fetchThreadList()




# Message func

def SendMessage(recipientName, message):
    for thread in threads:
        if thread.name == recipientName:
            client.send(Message(text=message), thread_id=thread.uid, thread_type=ThreadType.USER)
            print("Message sent to {}".format(recipientName))
            


GoodMorning = MessageHandler("Your Name Here", "Good Morning!", 8, 00)

Messages = [GoodMorning]

while(True):

    CurrentTime = time.localtime()

    for message in Messages:
        if message.delivered == False:
            if message.hour == CurrentTime.tm_hour and message.minute == CurrentTime.tm_min:
                SendMessage(message.recipient, message.text)
                message.delivered = True
                print("Message delivered")
