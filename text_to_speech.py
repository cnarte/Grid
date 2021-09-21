from re import sub
import subprocess
from gtts import gTTS

mytext = "Welcome to flipkart!"

language = 'en'

myObj = gTTS(text=mytext, lang=language)

myObj.save("tempAudio/welcome.mp3")

subprocess.call(['mpg321', "tempAudio/welcome.mp3", '--play-and-exit']) # mpg321 / vlc
