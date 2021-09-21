import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(sample_rate=44100) as source:
    print('Speak something: ')
    audio = r.listen(source, 0, 5)

    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
    except:
        print('Sorry could not recognize your voice')
