import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import cv2

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

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

def incLength():
    speak('How much do you want to change the length')
    length=takeCommand()
    resized=cv2.resize(img,((float(img.shape[1]/1)),(float(img.shape[0]*length))))
    cv2.imshow("photos",resized)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

def decLength():
    speak('How much do you want to change the length')
    length=takeCommand()
    resized=cv2.resize(img,((float(img.shape[1]/1)),(float(img.shape[0]/length))))
    cv2.imshow("photos",resized)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

def incBreadth():
    speak('How much do you want to change the length')
    breadth=takeCommand()
    resized=cv2.resize(img,((float(img.shape[1]*breadth)),(float(img.shape[0]))))
    cv2.imshow("photos",resized)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()


def decBreadth():
    speak('How much do you want to change the length')
    breadth=takeCommand()
    resized=cv2.resize(img,((float(img.shape[1]/breadth)),(float(img.shape[0]))))
    cv2.imshow("College photos",resized)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
