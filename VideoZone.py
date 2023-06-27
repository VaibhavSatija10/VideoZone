import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import cv2
import numpy as np
import face_recognition
import os
import requests
from datetime import datetime
from tkinter import *
import json

path = 'Images_Attendance'
images = []
tempArray=[]
tempArray2=[]
x={}
classNames = []
Listsarray=[1,2,3,4,5,6 ]
myList = os.listdir(path)
# print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)
#
#
# data = r.json()
# print(data)
url = 'https://attendence-production.up.railway.app/api/class/postdata'
url2= 'https://attendence-production.up.railway.app/api/class/attendence'
myobj={"hiw":"dscds"}

win = Tk()  ## win is a top or parent window

win.geometry("200x100")

b = Button(win, text="Submit")

b.pack()  # using pack() geometry

def findEncodings(images):
    encodeList =[]
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
#
# def markAllAttendance(classNames):
#     # print(classNames)
#     with open('Attendance.csv', 'r+') as f:
#         myDataList = f.readlines()
#         nameList = []
#         for line in myDataList:
#             entry = line.split(',')
#             nameList.append(entry[0])
#             # f.writelines(f'\n{name}')
#         if classNames not in nameList:
#             time_now = datetime.now()
#             tString = time_now.strftime('%H:%M:%S')
#             dString = time_now.strftime('%m/%d/%Y')
#             f.writelines(f'\n{classNames},{tString},{dString},{"absent"}')
# x = requests.post(url, json = myobj)

def markAttendance(name):
    # print(name)
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            # f.writelines(f'\n{name}')
        if name not in nameList:
            time_now = datetime.now()
            tString = time_now.strftime('%H:%M:%S')
            dString = time_now.strftime('%m/%d/%Y')
            f.writelines(f'\n{name},{tString},{dString},{"present"}')
# x = requests.post(url, json = myobj)


encodeListKnown = findEncodings(images)
print('Encoding Complete')
# markAllAttendance(classNames)
# print(x.text)
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()

            # a = np.append(name, name[0])
            arr = np.array([name])
            tempArray=np.append(tempArray, np.array([name]))
            tempArray2=np.unique(tempArray)
            list2 = tempArray2.tolist()

            # res = np.unique(arr)
            # print(arr)
            if len(tempArray2)<2:

                print(list2)
            else:

                # Uncomment for api

                print(list2)
                # r = requests.post(url, json={'data' : list2})
                # print(r.text )
                # print(list2)
                # r2 = requests.get(url2)
                # geek = json.loads(r2.text)
                # print(geek['data'])


                # PresentData = r2.text.getProperty('id')

                # print(PresentData)
                markAttendance(name)
                cv2.destroyAllWindow()



            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 250, 0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        markAttendance(name)

    cv2.imshow('webcam', img)
    if cv2.waitKey(10) == 13:
        break
cap.release()
cv2.destroyAllWindow()
path = 'Images_Attendance'
images = []
tempArray=[]
tempArray2=[]

classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList =[]
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            time_now = datetime.now()
            tString = time_now.strftime('%H:%M:%S')
            dString = time_now.strftime('%d/%m/%Y')
            f.writelines(f'\n{name},{tString},{dString}')

encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()

            # a = np.append(name, name[0])
            arr = np.array([name])
            tempArray=np.append(tempArray, np.array([name]))
            tempArray2=np.unique(tempArray)

            # res = np.unique(arr)
            # print(arr)
            print(tempArray2)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 250, 0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

    cv2.imshow('webcam', img)
    win.mainloop()
    if cv2.waitKey(10) == 13:
        break
cap.release()
cv2.destroyAllWindow()

