import cv2
import time
from cvzone.PoseModule import PoseDetector
import csv
import numpy as np
import math

cap = cv2.VideoCapture("gomiti1.mp4")
detector = PoseDetector()


now = time.time()
#caturo da 3 a 9 secondi
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)

    if lmList:
        try:
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

 
    with open('gomito_dav_mal_corsa.csv', 'a', newline='') as file:  # se tallone sinitro è in piu in basso di punta piede sinistro corre male
        writer = csv.writer(file)
        # Calcola la diagonale tra il polso e la spalla
        diagonale_polso_spallaSX = np.sqrt((point11[0] - point15[0])**2 + (point11[1] - point15[1])**2)

        # Calcola l'intersezione tra spalla e polso
        x_intersezione = (point11[0] + point15[0]) / 2
        y_intersezione = (point11[1] + point15[1]) / 2
        intersezione = (x_intersezione, y_intersezione)

        # Calcola la diagonale secondaria tra il gomito e l'intersezione tra spalla e polso
        diagonale_secondariaSX = np.sqrt((x_intersezione - point13[0])**2 + (y_intersezione - point13[1])**2) * 2

        # Calcola la diagonale tra il polso e la spalla
        diagonale_polso_spallaDX = np.sqrt((point12[0] - point16[0])**2 + (point12[1] - point16[1])**2)

        # Calcola l'intersezione tra spalla e polso
        x_intersezione = (point12[0] + point16[0]) / 2
        y_intersezione = (point12[1] + point16[1]) / 2
        intersezione = (x_intersezione, y_intersezione)

        # Calcola la diagonale secondaria tra il gomito e l'intersezione tra spalla e polso
        diagonale_secondariaDX = np.sqrt((x_intersezione - point14[0])**2 + (y_intersezione - point14[1])**2) * 2

        writer.writerow([diagonale_polso_spallaSX / diagonale_secondariaSX, diagonale_polso_spallaDX / diagonale_secondariaDX])  
        
        #vicinoall 1,2 max 3 allora sto sui 90
        

   #y aumenta verso il basso
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


















