import cv2
import time
from cvzone.PoseModule import PoseDetector
import csv
import numpy as np
import math

cap = cv2.VideoCapture("./video/trazioni_male2.mov")
detector = PoseDetector()


now = time.time()
#caturo da 3 a 9 secondi
while True:
    try:
        success, img = cap.read()
        #img = cv2.resize(img, (1280, 720))
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)
        if lmList:
            try:
                point31 = lmList[0][31] #piede sinistro punta
                point32 = lmList[0][32] #piede destro punta
            except:
                pass

        cv2.imshow("run", img)

        
        with open('./male/piedi_mal_sus_traz.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            #voglio la differenza asse x tra punta piede sx e punta piede dx
            diff_piedi = abs(point31[0]-point32[0])
            writer.writerow([diff_piedi])
            #piu è vicino a 0 meglio è
    except:
        break


   #y aumenta verso il basso
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
