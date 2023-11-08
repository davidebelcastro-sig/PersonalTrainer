import cv2
from cvzone.PoseModule import PoseDetector
import csv
import numpy as np
import os
from corsa.testing import take_thresold
#import take_thresold solo su esecuzione singola senza gui

def start(video_file):
    cap = cv2.VideoCapture(video_file)
    detector = PoseDetector()
    try:
        os.remove("volto_corsa.csv")
    except:
        pass
    try:
        os.remove("schiena_corsa.csv")
    except:
        pass
    try:
        os.remove("piede_corsa.csv")
    except:
        pass
    try:
        os.remove("gomito_corsa.csv")
    except:
        pass
    with open('volto_corsa.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["volto"])
    with open('schiena_corsa.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["sx", "dx"])
    with open('piede_corsa.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["sx", "dx"])
    with open('gomito_corsa.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["sx", "dx"])
    
    while True:
        try:
            success, img = cap.read()
            #img = cv2.resize(img, (1280, 720))
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
            #cv2.imshow("Image", img)
            with open('volto_corsa.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                #differenza asse x tra volto medio x e spalla x, sx e dx
                #voglio vedere se ho spalla sx o dx avanti
                if point11[0] > point12[0]: #spalla sx avanti 
                    sp = abs(mediaX_volto - point11[0])
                else:
                    sp = abs(mediaX_volto - point12[0])
                writer.writerow([sp]) #più è piccolo e più la testa è dritta 

            with open('schiena_corsa.csv', 'a', newline='') as file:  # se tallone sinitro è in piu in basso di punta piede sinistro corre male
                writer = csv.writer(file)
                #distanza orizzontale tra spalla sinistra e bacino sinostro
                dist1 = abs(point11[0] - point23[0])
                dist2 = abs(point12[0] - point24[0])
                writer.writerow([dist1, dist2])
                #piu è vicino a 0 meglio è

            with open('piede_corsa.csv', 'a', newline='') as file:  # se tallone sinitro è in piu in basso di punta piede sinistro corre male
                writer = csv.writer(file)
                rapportoSx = point31[1] / point29[1]  
                rapportoDx = point32[1] / point30[1]
                writer.writerow([rapportoSx, rapportoDx])
                #maggiore di 1 meglio è
                
            with open('gomito_corsa.csv', 'a', newline='') as file:  # se tallone sinitro è in piu in basso di punta piede sinistro corre male
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
        except:
            break     


def esegui(video_file):
    #leggo i parametri di thresold.txt(giusti)
    with open('corsa/davide/bene/thresold.txt', 'r') as file:
        data = file.readlines()
        gomiti_vero = data[0].split(":")[1].strip()
        schiena_vero = data[1].split(":")[1].strip()
        volto_vero = data[2].split(":")[1].strip()
    start(video_file)
    take_thresold.run()
    #leggere i valori di thresold.txt
    with open('thresold.txt', 'r') as file:
        data = file.readlines()
        gomiti = data[0].split(":")[1].strip()
        schiena = data[1].split(":")[1].strip()
        volto = data[2].split(":")[1].strip()
    #confrontare i valori
    err_gomiti = -1
    err_schiena = -1
    err_volto = -1
    if float(gomiti) > float(gomiti_vero):
        err_gomiti = "no" #errore nella posizione dei gomiti
    else:
        err_gomiti = "ok"
    if float(schiena) > float(schiena_vero):
        err_schiena = "no" #errore nella posizione della schiena
    else:
        err_schiena = "ok"
    if float(volto) > float(volto_vero):
        err_volto = "no"
    else:
        err_volto = "ok"
    return err_gomiti, err_schiena, err_volto


