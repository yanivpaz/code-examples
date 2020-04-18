#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:42:09 2019

@author: jayja
@source: https://towardsdatascience.com/build-your-first-chatbot-using-python-nltk-5d07b027e727
"""

from nltk.chat.util import Chat, reflections

#print(reflections)

pairs = [
            [
                r"my name is (.*)",
                ["Hello %1, how are you today?",]
            ],
            [
                r"what is your name?",
                ["My name is ChatBot and I will help you verify the Turing test today",]
            ],
            [
                r"how are you?",
                ["I was doing good until now\nJust kidding am still doing great, how are you doing?",]
            ],
            [
                r"sorry (.*)",
                ["What are you apologizing for?", "It's all right, I am very forgiving",]
            ],
            [   
                r"i'm (.*) doing good",
                ["That's great to hear", "^_^",]
            ],
            [
                r"hi|hey|hello (.*)",
                ["Hello", "Hey there",]
            ],
            [
                r"(.*) age?",
                ["I was created on the 1st of September, 2019\nas a beta project",]
            ],
            [
                r"quit",
                ["Signing out, see you soon ^_^"]
            ],
        ]
            

def chatbot():
    '''Chat is the class that contains all the logic to be used by the chatbot,
    reflections is a predefined dictionary containing a set of input values and it's corresponding output values
    '''
    print("Booting up\nHey I am a simple ChatBot made without ML, only using NLTK library. Please type in English language what you want to ask me. Type quit to leave")
    chat = Chat(pairs, reflections)
    #trigger the convo
    chat.converse()

if __name__ == "__main__":
    chatbot()