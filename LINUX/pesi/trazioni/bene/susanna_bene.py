import cv2
import time
from cvzone.PoseModule import PoseDetector
import csv
import numpy as np
import math

cap = cv2.VideoCapture("./video/trazioni_bene.mov")
detector = PoseDetector()


now = time.time()
#caturo da 3 a 9 secondi
while True:
    success, img = cap.read()
    #img = cv2.resize(img, (1280, 720))
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)

    if lmList:
        try:
            point11 = lmList[0][11] #spalla sinistra
            point12 = lmList[0][12] #spalla destra
            point13 = lmList[0][13] #gomito sinistro
            point14 = lmList[0][14] #gomito destro
            point15 = lmList[0][15] #mano sx
            point16 = lmList[0][16] #mano dx
            point17 = lmList[0][17] #mano sx
            point18 = lmList[0][18] #mano dx
            point19 = lmList[0][19] #mano sx
            point20 = lmList[0][20] #mano dx
            point21 = lmList[0][21] #mano sx
            point22 = lmList[0][22] #mano dx
            point23 = lmList[0][23] #bacino sinistro
            point24 = lmList[0][24] #bacino destro
            point31 = lmList[0][31] #piede sinistro punta
            point32 = lmList[0][32] #piede destro punta
            media_manosx_x = np.mean([point15[0], point17[0], point19[0], point21[0]])
            media_manodx_x = np.mean([point16[0], point18[0], point20[0], point22[0]])
        except:
            pass

    cv2.imshow("run", img)

    
    with open('./bene/piedi_bn_sus_traz.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        #voglio la differenza asse x tra punta piede sx e punta piede dx
        diff_piedi = abs(point31[0]-point32[0])
        writer.writerow([diff_piedi])
        #piu è vicino a 0 meglio è

    with open('./bene/schiena_bn_sus_traz.csv', 'a', newline='') as file: 
        writer = csv.writer(file)
        #distanza orizzontale tra spalla sinistra e bacino sinostro
        dist1 = abs(point11[0] - point23[0])
        dist2 = abs(point12[0] - point24[0])
        writer.writerow([dist1, dist2])
        #piu è vicino a 0 meglio è
    
    with open('./bene/gomiti_bn_sus_traz.csv', 'a', newline='') as file: 
        writer = csv.writer(file)
        #calcolo differenza asse x tra gomito sx e spalla sx
        diff_sx = abs(point11[0] - point13[0])
        #calcolo differenza asse x tra gomito dx e spalla dx
        diff_dx = abs(point12[0] - point14[0])
        writer.writerow([diff_sx, diff_dx])
        #piu è vicino a 0 meglio è

   #y aumenta verso il basso
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
