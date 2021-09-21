''' commands to run :- 1. rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
                    2. rasa run actions
                    3. python voicebot.py
'''
import requests

sender = input("What is your name?\n")

bot_message = ""
while bot_message != "Bye":
    message = input("What's your message?\n")

    print("Sending message now...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": sender, "message": message})

    print("Bot says, ",end=" ")
    for i in r.json():
        bot_message = i['text']
        print(bot_message)