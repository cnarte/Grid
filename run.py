''' command to run :- 1. rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
                    2. rasa run actions
                    3. python run.py
'''


import json
import requests
import speech_recognition as sr
import subprocess
from gtts import gTTS


bot_message = ""
message = ""


while bot_message != "Bye" or bot_message != "thanks":

    r = sr.Recognizer()
    with sr.Microphone(sample_rate=44100) as source:
        print("Speak Anything: ")
        audio = r.listen(source, 0, 5)

        try:
            message = r.recognize_google(audio)
            print("You said:", message)
        except:
            print("Sorry could not recognize your voice")
        
    if len(message) == 0:
        continue
    print("Sending message now...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

    print("Bot says: ")
    for i in r.json():
        bot_message = i['text']
        print(bot_message)

    myObj = gTTS(text=bot_message)
    myObj.save('tempAudio/test.mp3')
    print("saved")

    subprocess.call(['mpg321', 'tempAudio/test.mp3', '--play-and-exit'])


