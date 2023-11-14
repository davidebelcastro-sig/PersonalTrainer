import cv2
import time
from cvzone.PoseModule import PoseDetector
import csv
import numpy as np
import math

cap = cv2.VideoCapture("./video/trazioni_male1.mov")
detector = PoseDetector()


now = time.time()
#caturo da 3 a 9 secondi
while True:
    try:
        success, img = cap.read()
        # img = cv2.resize(img, (1280, 720))
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)

        if lmList:
            try:
                point11 = lmList[0][11] #spalla sinistra
                point12 = lmList[0][12] #spalla destra
                point13 = lmList[0][13] #gomito sinistro
                point14 = lmList[0][14] #gomito destro 
            except:
                pass

        cv2.imshow("run", img)

        
        with open('./male/gomiti_mal_sus_traz.csv', 'a', newline='') as file: 
            writer = csv.writer(file)
            #calcolo differenza asse x tra gomito sx e spalla sx
            diff_sx = abs(point11[0] - point13[0])
            #calcolo differenza asse x tra gomito dx e spalla dx
            diff_dx = abs(point12[0] - point14[0])
            writer.writerow([diff_sx, diff_dx])
            #piu è vicino a 0 meglio è
    except:
        break

   #y aumenta verso il basso
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
