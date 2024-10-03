import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imgBackground = cv2.imread("Resources/background.png")

#Importing the mode Images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))

#Load the encoding file
print("Loading Encoded ...")
file = open("EncodeFile.p","rb")
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown,studentIds = encodeListKnownWithIds
print("Encoded file loaded")
# print("studentIds",studentIds)


while True:
    success, img = cap.read()

    imgS = cv2.resize(img,(0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)

    # Resize bức ảnh, đọc kỹ chỗ này
    img_resized = cv2.resize(img, (640, 480))  # Resize ảnh về (480, 640)
    img = img_resized

    imgBackground[162:162+480,55:55+640] = img
    imgBackground[44:44+633,808:808+414] = imgModeList[0]

    for encodeFace, faceLoc in zip(encodeCurFrame,faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        # print("matches",matches)
        # print("faceDis",faceDis)
        #
        matchIndex = np.argmin(faceDis)
        # print("matchIndex",matchIndex)

        if matches[matchIndex]:
            # print("Known Face detected")
            # print(studentIds[matchIndex])
            y1, x2, y2, x1 = faceLoc


    cv2.imshow("Web cam background",imgBackground)
    cv2.waitKey(1)