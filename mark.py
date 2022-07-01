import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from datetime import date


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good morning!")
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        print("Good Afternoon!")
        speak("Good Afternoon!")

    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("I am Mark, Sir. How may I assist you?")
    speak("I am Mark, Sir. How may I assist you")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Analysing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: {}\n".format(query))

    except Exception:
        print("Say that again please...")
        return "None"
    return query


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('virtualassistantmark@gmail.com', '@alfred12')
    server.sendmail('virtualassistantmark@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wish()
    while True:

        query = takeCommand().lower()

        if 'hello' in query:
            print("Hello Sir. How are you today?")
            speak("Hello Sir. How are you today?")

        elif 'who are you' in query:
            print(
                "I am Mark, Sir. I am just a dignified virtual butler at your service.")
            speak(
                "I am Mark, Sir. I am just a dignified virtual butler at your service.")

        elif 'what can you do' in query:
            print("I can send emails, open websites , search videos on youtube , surf google, predict date and time and provide news headlines from the Times Of India")
            speak("I can send emails, open websites , search videos on youtube , surf google, predict date and time and provide news headlines from the Times Of India")

        elif 'who made you' in query:
            print("I am built by Vishnu.")
            speak("I am built by Vishnu.")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'search youtube' in query:
            speak("What should I search for, Sir?")
            req = takeCommand()
            webbrowser.open(
                "https://www.youtube.com/results?search_query={}".format(req))

        elif 'search google' in query:
            speak("What should I search for, Sir?")
            search = takeCommand()
            webbrowser.open(
                "https://www.google.com/search?q={}".format(search))

        elif 'open website' in query:
            speak("Which website should i open, Sir?")
            site = takeCommand()
            if site != 'none':
                webbrowser.open("https://www.{}.com/".format(site))
            else:
                speak("Website not found")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("Sir, the time is {}".format(strTime))
            speak("Sir, the time is {}".format(strTime))

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Who is this email going to ?")
                mail = input("Who is this email going to ?: ")
                to = "{}@gmail.com".format(mail)
                sendemail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email.")

        elif 'joke' in query:
            print("I went to a street where the houses were numbered 8k, 16k, 32k, 64k, 128k, 256k and 512k. It was a trip down Memory Lane.")
            speak("I went to a street where the houses were numbered 8k, 16k, 32k, 64k, 128k, 256k and 512k. It was a trip down Memory Lane. Ha, Ha, Ha ")

        elif 'date' in query:
            today = date.today()
            print("The date is {}".format(today))
            speak("The date is {}".format(today))

        elif 'code' in query:
            codePath = r"C:\Users\vishn\AppData\Local\Programs\Microsoft VS Code"
            os.startfile(codePath)

        if 'leave' in query:
            print("Goodbye Sir. Have a nice day.")
            speak("Goodbye Sir. Have a nice day.")
            break
