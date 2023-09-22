import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import time

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

command = 'imstillhere'


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    global command
    try:
        with sr.Microphone() as source:
            command = 'imstillhere'
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command

while True:
    command = take_command()
    print(command)
    if 'cancel' in command:
        talk('cancelling request')
    elif 'imstillhere' in command:
        talk('hey im still here')
        time.sleep (1)
        talk('mind closing this programm?')
        time.sleep (3)
        talk ('ok i will close it for you')
        break
    elif 'crackhead' in command:
        talk('Hello Bro!! How May i Help you?')
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        break
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    else:
        talk('sorry, please repeat')
