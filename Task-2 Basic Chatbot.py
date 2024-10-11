import nltk
import random
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello there!", "Hi!", "Hey! What's up?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thanks!", "Pretty good, how about you?", "Can't complain!"]
    ],
    [
        r"what's your name?",
        ["My self Chatbot.", "I'm Chatbot, nice to meet you.", "Chatbot."]
    ],
    [
        r"what can you do?",
        ["I can chat with you!", "We can talk about anything you like.", "I'm still learning, but I'm a pretty good listener."]
    ],
    [
        r"what about you?",
        ["I'm a computer program, so I don't have a personal life."]
    ],
    [
        r"bye|goodbye|see you",
        ["See ya!", "Take care!", "Later!"]
    ],
    [
        r"(.*)",
        ["Tell me more about that.", "Interesting!", "I'm listening."]
    ],
]

def chatbot():
    print("Hey! Let's chat. Type 'bye' to say goodbye.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()