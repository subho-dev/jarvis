import cv2
import numpy as np
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


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

speak('Video recording, picture click or web cam')
cam=takeCommand()
#0 for 1st webcam 1 for 2nd
cap=cv2.VideoCapture(0)
sve=cv2.VideoWriter_fourcc(*'XVID')

out=cv2.VideoWriter('output.avi',sve, 20.0, (640,480))
#must be 640,480 otherwise will not be supported

if 'video' or 'recording' in cam.lower():
    while True:
        ret, frame=cap.read()    
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('color Camera',frame)
        cv2.imshow('gray frame',gray)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
elif 'picture' or 'photo' or 'click' or 'capture' in cam.lower():
    while True:
        ret, frame=cap.read()    
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('color Camera',frame)
        cv2.imshow('gray frame',gray)
        speak('press     c        to capture')
        if cv2.waitKey(1) & 0xFF==ord('c'):
            out.write(frame)
            break
elif 'webcam' in cam.lower():
    while True:
        ret, frame=cap.read()    
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('color Camera',frame)
        cv2.imshow('gray frame',gray)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
cap.release()
out.release()
cv2.destroyAllWindows
