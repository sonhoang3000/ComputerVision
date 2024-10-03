import os

import cv2

# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)

imgBackground = cv2.imread("Resources/background.png")

#Importing the mode Images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))

print(imgModeList)

# while True:
#     success, img = cap.read()
#
#     # Resize bức ảnh, đọc kỹ chỗ này
#     img_resized = cv2.resize(img, (640, 480))  # Resize ảnh về (480, 640)
#     img = img_resized
#
#     imgBackground[162:162+480,55:55+640] = img
#     imgBackground[44:44+633,808:808+414] = imgModeList[0]
#
#
#     cv2.imshow("Web cam background",imgBackground)
#     cv2.waitKey(1)