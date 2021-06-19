import face_recognition
import cv2
import os
import pyttsx3
import numpy as n
from datetime import datetime
path='images'
i=[]
c=[]
q=[]
my=os.listdir(path)
print(my)
for c1 in my:
    im=cv2.imread(f'{path}/{c1}')
    i.append(im)
    c.append(os.path.splitext(c1)[0])
def speak(text):
   e=pyttsx3.init()
   e.say(text)
   e.runAndWait()
speak("hi")
def attendance(n2):
    with open('attendance','r+') as f:
        lis=f.readlines()
        newlist=[]
        for  i in lis:
            entry=i.split(',')
            newlist.append(entry[0])
        if n2 not in newlist:
            print(newlist)
            speak(n2 + "attendance has been recorded")
            no=datetime.now()
            ds=no.strftime('%H:%M:%S')
            f.write(f'\n{n2},{ds}')
        else:
            speak("Your attendance has already been recorded")
def encode(i):
    encode1=[]
    for v in i:
       v= cv2.cvtColor(v, cv2.COLOR_BGR2RGB)
       h = face_recognition.face_encodings(v)[0]
       encode1.append(h)
    return encode1
ee=encode(i)
print(len(ee))
cap=cv2.VideoCapture(0)
while True:
    s,ii=cap.read()
    image=cv2.resize(ii,(0,0),None,0.25,0.25)
    image= cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face=face_recognition.face_locations(image)
    encodeing=face_recognition.face_encodings(image,face)
    for ff,eee in zip(face,encodeing):
        m=face_recognition.compare_faces(eee,ee)
        faced=face_recognition.face_distance(eee,ee)
        print(faced)
        match=n.argmin(faced)
        print(match)
        if m:
            n2=c[match].upper()
            q.append(n2)
            attendance(n2)




