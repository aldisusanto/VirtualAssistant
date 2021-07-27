import sys

import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import smtplib
import pywhatkit as kit

engine = pyttsx3.init('sapi5')


# voices = engine.getProperty()


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("listening....")
            audio = r.listen(source)
            print("recognition")
            voice = r.recognize_google(audio, language='id')
            voice = voice.lower()
            print(f"your said : {voice}")

    except Exception as e:
        return takecommand()
    return voice


def intro():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("good morning sir !!")
    elif 12 < hour < 18:
        speak("good afternoon sir !!")
    elif 18 < hour < 24:
        speak("good evening sir !!")

    speak("Im your assistant. I can help you in many things")
    speak("you can try by saying send whatsapp")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email', 'your password')
    server.sendmail('your email', to, content)
    server.close()

def message_email():
    speak("what is your message?")
    content = takecommand().lower()
    sendEmail(to, content)
    speak(f"Email has been sent to {to}")


def message_whatsapp(phone_no):
    speak("what is your message?")
    message = takecommand().lower()
    webbrowser.open('https://web.whatsapp.com/send?phone=' + phone_no + '&text=' + message)


intro()
while True:
    query = takecommand()
    if 'open download' in query:
        speak("opening")
        path = "C:\\Users\\HP\\Downloads"
        os.startfile(path)

    elif 'open document' in query:
        speak("opening")
        path = "C:\\Users\\HP\\Documents"
        os.startfile(path)

    elif 'open pycharm' in query:
        speak("launching")
        path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1\\bin\\pycharm64.exe"
        os.startfile(path)

    elif 'open visual code' in query:
        speak("launching")
        path = "C:\\Microsoft VS Code\\Code.exe"
        os.startfile(path)

    elif 'open facebook' in query:
        speak("opening")
        webbrowser.open("www.facebook.com")

    elif 'send email' in query:
        try:
            speak("Do you want send email too?")
            if takecommand().lower() == 'me':
                to = 'aldisusanto648@gmail.com'
                message_email()
            elif takecommand().lower() == 'father':
                to = 'andilewa0205@gmail.com'
                message_email()
            elif takecommand().lower() == 'sister':
                to = 'ainunananda3@gmail.com'
                message_email()
            else:
                speak("operation not success")
        except Exception as e:
            print(e)
            speak("Email not send")

    elif 'send whatsapp' in query:
        try:
            speak("Do you want send message too??")
            if takecommand().lower() == 'sister':
                phone_no = '+6281242105737'
                message_whatsapp(phone_no)

            elif takecommand().lower() == 'father':
                phone_no = '+6285230197505'
                message_whatsapp(phone_no)

            else:
                speak("operation not success")
        except:
            speak("Message not send")

    elif 'music on youtube' in query:
        speak("what do you want play ?")
        music = takecommand().lower()
        speak("opening")
        kit.playonyt(music)

    elif 'search google' in query:
        speak("what do you want to find?")
        search = takecommand().lower()
        speak("searching")
        webbrowser.open("https://www.google.com/search?q=" + search)

    elif 'search location' in query:
        speak("what you want to find on the map?")
        maps = takecommand().lower()
        speak("opening")
        webbrowser.open("https://www.google.co.id/maps/place/" + maps)

    elif 'play music' in query:
        speak("playing")
        music_dir = "C:\\Users\\HP\\Music\\playlist"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'no thanks' in query:
        speak("thanks for using me, have a good day")
        sys.exit()

    else:
        speak("please say again")
