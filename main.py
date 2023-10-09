import random

import pyttsx3
import speech_recognition as sr
import datetime
import os
from requests import get
import wikipedia
import webbrowser
import pywhatkit as pkit
import smtplib
import openai
from api import apikey


chatStr = ""
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)
# engine.setProperty('rate',150)

# converts text to speech
def speak(audio):
    print("  ")
    print(f":{audio}")
    print("  ")

    engine.say(audio)
    engine.runAndWait()
# Convert text to speech

def Takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio,language='en-in')
        print(f"Your command: {query}\n")

    except Exception as e:
        # speak("SORRY SIR, Please say that again..")
        return "none"


    return query

# to greet
def wish():
    hour =int(datetime.datetime.now().hour)

    if hour>=0 & hour<=12:
        speak("GOOD MORNING")

    elif  hour>=12 & hour<=18:
        speak("GOOD AFTERNOON")

    else:
        speak("GOOD EVENING")
    speak("I am jarvis sir. HOW CAN I HELP YOU TODAY?")

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('lakshitkhandelwal2002@gmail.com','@Lakshit151202')
    server.sendmail('lakshitkhandelwal2002@gmail.com',to,content)
    server.close()

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Lakshit: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]



def TaskExecution():

    wish()


    while True:
        query = Takecommand().lower()

        # LOGIC BUILDING STARTS NOW

        if "open notepad" in query:
            npath="C:\\WINDOWS\\system32\\notepad.exe"
            speak("Yes,opening notepad sir")
            os.startfile(npath)

        elif "close notepad" in query:

            speak("closing notepad sir")
            os.system("taskkill /f /im notepad.exe")

        elif "play anime" in query:
            apath= "E:\Anime\edit"
            vid=os.listdir(apath)
            rd = random.choice(vid)
            os.startfile(os.path.join(apath, rd))


        elif "open cmd" in query:
            speak("opening cmd sir. ")
            os.system("start cmd")

        elif "open security camera" in query:
            import urllib.request
            import cv2
            import numpy as np
            import time
            URL="http://192.168.235.199:8080/shot.jpg"
            while True:
                img_arr=np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                img=cv2.imdecode(img_arr,-1)
                cv2.imshow('IPWebcam',img)
                q=cv2.waitKey(1)
                if q == ord("q"):
                    break
            cv2.destroyAllWindows()


        # elif "play music" in query:
        #     speak("Sure sir, now playing your favourite music ")
        #     music_dir = "D:\\music"
        #     songs=os.listdir(music_dir)
        #     rd=random.choice(songs)
        #     os.startfile(os.path.join(music_dir,rd))

        elif "shutdown" in query:
            speak("GOOD BYE SIR, Have a nice day!.")
            speak("Shutting down system in ")
            speak('3')
            speak('2')
            speak('1')
            os.close()
            break


        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"your IP adress is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(result)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open codechef" in query:
            webbrowser.open('https://www.codechef.com/users/degeneratorx')

        elif "open google" in query:
            speak('okay Sir, what do you want to search on google?')
            q2=Takecommand().lower()
            webbrowser.open(f"{q2}")

        elif "play song " in query:
            speak('okay Sir, what do you wanna listen today?')
            q3 = Takecommand().lower()
            pkit.playonyt(f"{q3}")

        elif "send sms" in query:
            speak("what should i say,sir?")
            msg=Takecommand()
            # importing twilio
            from twilio.rest import Client

            # Your Account Sid and Auth Token from twilio.com / console
            account_sid = 'AC9a631d2f826ff332a0f1252aa1a76c6e'
            auth_token = '30b33053babadbc83ac1eb844e28e8d8'

            client = Client(account_sid, auth_token)

            message = client.messages.create(
                from_='+13342181751',
                body=msg,
                to='+916377722611'
            )

            print(message.sid)

        elif "make a call" in query:
            from twilio.rest import Client

            # Your Account Sid and Auth Token from twilio.com / console
            account_sid = 'AC9a631d2f826ff332a0f1252aa1a76c6e'
            auth_token = '30b33053babadbc83ac1eb844e28e8d8'

            client = Client(account_sid, auth_token)

            message = client.calls.create(
                from_='+13342181751',
                twiml='<Response><Say> Hello Jarvis calling this side. Hope you are doing well..</Say><Response>',
                to='+916377722611'
            )
            print(message.sid)


        # elif "email to ravi" in query:
        #     try:
        #         speak("what should i say? ")
        #         content=Takecommand().lower()
        #         to= "bt22cse149@iiitn.ac.in"
        #         sendEmail(to,content)
        #         speak("Email is successfully sent to Ravi ")
        #
        #     except Exception as e:
        #         print(e)
        #         speak("sorry sir ,an unidentified error has occured")
        else:
            print("Chatting...")
            chat(query)
# TaskExecution()