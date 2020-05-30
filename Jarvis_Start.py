import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import cv2

print("initialising jarvis")

MASTER="Sir"

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

#wishing command
def wishMe():
    hour=int(datetime.datetime.now().hour)
    print(hour)

    if  hour>0 and hour < 12:
        speak("Good morning"+MASTER)


    elif hour >=12 and hour <18:
        speak("Good Afternoon"+MASTER)
    else:
        speak("Good Evening"+MASTER)
    speak("how may i help you")

#taking command
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language ='en-in')
        print(query)

    except Exception as e:
        print("Sorry please can you repeat again")
        query=None
    return query

wishMe()

#input
query= takeCommand()

#wikipedia
if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query=query.replace("wikipedia","")
    results=wikipedia.summary(query,sentences=3)
    print(results)
    speak(results)

#Search engines
elif 'google' in query.lower():
    speak('Opening Google...')
    speak('What do you want to search')
    query_google=takeCommand()
    print(query_google)
    new=query_google.replace('','+')
    url="https://www.google.com/search?source=hp&ei=NdBTXs-4DceG4-EP1o2umA0&q="+new+"&oq="+new+"&gs_l=psy-ab.3.0.0l10.728770.730510..732615...0.0..0.227.1422.0j5j3......0....1..gws-wiz.....6..0i362i308i154i357j0i131.PEWMaSRAodU"
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url, new=2)

elif 'bing server' in query.lower():
    speak('Opening bing...')
    speak('What do you want to search')
    query_bing=takeCommand()
    print(query_bing)
    new=query_bing.replace('','+')       
    url="https://www.bing.com/search?q="+new+"&form=QBLH&sp=-1&pq="+new+"&sc=8-4&qs=n&sk=&cvid=9B7A47BA6F86486EA0B7911FEB590930"
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    #webbrowser.get(chrome_path).open("bing.com")
    webbrowser.get(chrome_path).open(url, new=2)    

elif 'yahoo' in query.lower():
    speak('Opening yahoo...')
    speak('What do you want to search')
    query_yahoo=takeCommand()
    print(query_yahoo)
    new=query_yahoo.replace('','+')       
    url="https://in.search.yahoo.com/search?p="+new+"&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8"
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    #webbrowser.get(chrome_path).open("yahoo.com")
    webbrowser.get(chrome_path).open(url, new=2)
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

#youtube
elif 'youtube' in query.lower():
    import youTube

#music online and offline
elif 'play music' in query.lower():
    speak("online music or offline music")
    query_music=takeCommand()
    if 'online' in query_music.lower():
        chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open("https://www.youtube.com/watch?v=92J9p0VplTo&list=PL9bw4S5ePsEHwKpj0RkGOr2Is2uxvP0OD",new=2)
    elif 'offline' in query_music.lower():
        song_dir="G:\\Music"
        songs=os.listdir("G:/Music")
        os.startfile(os.path.join(song_dir, songs[7]))

#news
elif 'news' in query.lower():
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    speak("Showing today's news")
    speak('choose your language. English. Hindi. bengali. other languages. say Again if you want to hear again the list')
    n=takeCommand()
    while n=='again' or n=='Again':
        if 'again' in n.lower():
            speak('choose your language. English. hindi. bengali. other languages. Say Again if you want to hear again the list')
            n=takeCommand()
    if 'english' in n.lower():
        webbrowser.get(chrome_path).open("https://timesofindia.indiatimes.com/",new=2)
    elif 'hindi' in n.lower():
        webbrowser.get(chrome_path).open("https://aajtak.intoday.in/",new=2)
    elif 'bengali' in n.lower():
        webbrowser.get(chrome_path).open("https://www.ndtv.com/bengali",new=2)
    else:
        speak('Speak out the language in which you want to read news')
        lang=takeCommand()
        webbrowser.get(chrome_path).open("https://www.ndtv.com/"+lang, new=2)

#Shopping
elif 'shopping' in query.lower():
    import shopping

#playstore
elif 'playstore' or 'play store' in query.lower():
    import playstore  

#Turn on camera
elif 'camera' in query.lower():
    import camera
# Next targets... Working on it
#Editting app

#1-Click photos
#2-Record Videos
#Security(Face lock)
#Analysing an image
#Turn on wifi, hotspot, bluetooth
#enter directory to search a file in the laptop
#Connecting with any phone and accessing it
#Calling using the connected phone
