
import googlesearch
import pyttsx3
import speech_recognition as sr
import wikipedia
from googlesearch import search
import webbrowser
import os

import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning Badsa")
    elif hour>=12 and hour<18:
        speak("good afternoon Badsa")
    else:
        speak("good evening Badsa")        


def takeCommand():
     #it take microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  
    
    except Exception as e:
        #print(e)
        print("Say it again please...")
        return "None"
   
    return query    


if __name__=="__main__" :
    wishMe()
    speak("Hi I am jervis, speed 1 terahertz, memory 1 zigabyte  , how can i help you Badsa")
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According ti wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
             webbrowser.open("google.com")
        
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'E:\\music\\favourite'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H,%M,%S")
            speak(f"sir, the time is {strTime}")   

        elif 'open code' in query:
            codePath = "C:\\Users\\mars\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)     

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")   
            
        elif 'who' in query:
            speak('Searching ...')
            query = query.replace("who", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to google") 
            print(results)
            speak(results)

        elif 'katy perry' in query:
            results = googlesearch.search('Katy Perry')
            print(results)
        

        elif 'youtube' in query:
            webbrowser.open("Youtube.com")


        elif 'map' in query:
            webbrowser.open("maps.google.com")

        elif 'what is' in query:
            speak('searching...')
            query = query.replace("what is", "")
            results = search(query)
            speak("According to google")
            print(results)
        
            
        
        elif 'how to' in query:
            speak('searching...')
            query = query.replace("how to", "")
            results = googlesearch.search(query)
            speak("According to google")
            print(results)
        elif 'instagram' in query:
            webbrowser.open("instagram.com")