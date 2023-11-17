import cv2
import time
from cvzone.PoseModule import PoseDetector
import csv
import numpy as np
import math

cap = cv2.VideoCapture("video.mp4")
detector = PoseDetector()


now = time.time()
#caturo da 3 a 9 secondi
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)

    if lmList:
        try:
            point0 = lmList[0][0]
            point1 = lmList[0][1]
            point2 = lmList[0][2]
            point3 = lmList[0][3]
            point4 = lmList[0][4]
            point5 = lmList[0][5]
            point6 = lmList[0][6]
            point7 = lmList[0][7]
            point8 = lmList[0][8]
            point9 = lmList[0][9]
            point10 = lmList[0][10] #volto
            #media asse x e asse y dei 11 punti
            mediaX_volto = np.mean([point0[0], point1[0], point2[0], point3[0], point4[0], point5[0], point6[0], point7[0], point8[0], point9[0], point10[0]])
            mediaY_volto = np.mean([point0[1], point1[1], point2[1], point3[1], point4[1], point5[1], point6[1], point7[1], point8[1], point9[1], point10[1]])
            point11 = lmList[0][11] #spalla sinistra
            point12 = lmList[0][12] #spalla destra
            point13 = lmList[0][13] #gomito sinistro
            point14 = lmList[0][14] #gomito destro
            point15 = lmList[0][15]
            point16 = lmList[0][16]
            point17 = lmList[0][17]
            point18 = lmList[0][18]
            point19 = lmList[0][19]
            point20 = lmList[0][20]
            point21 = lmList[0][21]
            point22 = lmList[0][22]
            point23 = lmList[0][23] #bacino sinistro
            point24 = lmList[0][24] #bacino destro
            point25 = lmList[0][25] #gamba sinistra
            point26 = lmList[0][26] #gamba destra
            point27 = lmList[0][27] #caviglia sinistro
            point28 = lmList[0][28] #caviglia destro
            point29 = lmList[0][29] # tallone sinistro
            point30 = lmList[0][30] #tallone destro
            point31 = lmList[0][31]  #punta piede sinistro
            point32 = lmList[0][32]  #punta piede destro
        except:
            pass

    cv2.imshow("run", img)

    
    with open('volto_sus_mal_corsa.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        #differenza asse x tra volto medio x e spalla x, sx e dx
        #voglio vedere se ho spalla sx o dx avanti
        if point11[0] > point12[0]: #spalla sx avanti 
            sp = abs(mediaX_volto - point11[0])
        else:
            sp = abs(mediaX_volto - point12[0])
        writer.writerow([sp]) #più è piccolo e più la testa è dritta 

       #y aumenta verso il basso
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
