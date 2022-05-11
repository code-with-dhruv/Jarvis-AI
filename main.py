import datetime
import imp
from logging import exception
import webbrowser
import wikipedia
import pyttsx3
import  speech_recognition as sr
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishme():
    hour = int( datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("Im a AI bot Created by Dhruv")
    
def query():
  q=input('type your text to be converted to voice:')
  return speak(q)
  



def takecommand():
    '''
     microphone input is taken into consideration (voice recognition)
     uses user input and types the words heard in the console
     made for future integration cmds like wikipedia, playmusic etc
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("...Listening")
        r.pause_threshold = 1
        audio=r.listen(source)
        
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in') 
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)

        print("Can you repeat ?, didnt get you")
        return "None"
    return query




if __name__ == "__main__":
    wishme()
    

    query()
    while True:

        query1=takecommand().lower()
        #logic for Wiki

        if 'wikipedia' in query1:
            speak('searching Wikipedia')
            query1=query1.replace("wikipedia","")
            results=wikipedia.summary(query1,sentances=3)
            speak('According to Wikipedia')
            speak (results)
            print(results)
        
        # elif 'open Youtube' in query1:
        #     webbrowser.open("youtube.com")

        elif 'open stack' or 'openstack' in query1:
            webbrowser.open("stackoverflow.com")
        elif 'open git' or 'opengit' in query1:
            webbrowser.open("github.com")
        elif 'open google' in query1:
            webbrowser.open("google.com")
        
        elif 'the time' in query1:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The  time is {strTime}")






