import cv2
from cvzone.PoseModule import PoseDetector
import csv
import numpy as np
import os
from pesi.legpress.testing import take_thresold
import multiprocessing
#import take_thresold solo su esecuzione singola senza gui

def start(video_file):
    cap = cv2.VideoCapture(video_file)
    detector = PoseDetector()
    try:
        os.remove("piede_leg.csv")
    except:
        pass
    try:
        os.remove("scende_leg.csv")
    except:
        pass

    with open('piede_leg.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["piede"])
    with open('scende_leg.csv', 'a', newline='') as file:
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
                    point23 = lmList[0][23] #bacino sinistro
                    point24 = lmList[0][24] #bacino destro
                    point29 = lmList[0][29] #tallone sinistro
                    point30 = lmList[0][30] #tallone destro
                    point31 = lmList[0][31] #piede sinistro punta
                    point32 = lmList[0][32] #piede destro punta
                except:
                    pass  

            with open('piede_leg.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                #voglio la differenza asse y tra punta piede sx e punta piede dx
                diff_piedi = abs(point31[1]-point32[1])
                writer.writerow([diff_piedi])
                #piu è vicino a 0 meglio è

            with open('scende_leg.csv', 'a', newline='') as file: 
                writer = csv.writer(file)
                #distanza orizzontale tra spalla sinistra e bacino sinostro
                dist1 = abs(point29[0] - point23[0])
                dist2 = abs(point30[0] - point24[0])
                writer.writerow([dist1, dist2])
                #piu è vicino a 0 meglio è
                        
        #y aumenta verso il basso
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except:
            break     


def esegui(video_file):
    #leggo i parametri di thresold.txt(giusti)
    with open('pesi/legpress/bene/thresold.txt', 'r') as file:
        data = file.readlines()
        piedi_vero = data[0].split(":")[1].strip()
        scende_vero = data[1].split(":")[1].strip()
    start(video_file)
    take_thresold.run()
    #leggere i valori di thresold.txt
    with open('thresold.txt', 'r') as file:
        data = file.readlines()
        piedi = data[0].split(":")[1].strip()
        scende = data[1].split(":")[1].strip()
    
    #confrontare i valori
    err_piedi = -1
    err_scende = -1
    if float(piedi) > float(piedi_vero)+10:
        err_piedi = "no" #errore nella posizione dei gomiti
    else:
        err_piedi = "ok"
   
    if float(scende) > float(scende_vero)+30:
        err_scende = "no"
    else:
        err_scende = "ok"
    return err_piedi, err_scende



