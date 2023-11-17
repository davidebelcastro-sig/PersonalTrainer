import cv2
from cvzone.PoseModule import PoseDetector
import csv
import numpy as np
import os
from pesi.trazioni.testing import take_thresold
import multiprocessing
#import take_thresold solo su esecuzione singola senza gui

def start(video_file):
    cap = cv2.VideoCapture(video_file)
    detector = PoseDetector()
    try:
        os.remove("schiena_traz.csv")
    except:
        pass
    try:
        os.remove("gomiti_traz.csv")
    except:
        pass
    try:
        os.remove("piedi_traz.csv")
    except:
        pass
    with open('schiena_traz.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["sx", "dx"])
    with open('gomiti_traz.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["sx", "dx"])
    with open('piedi_traz.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["piede"])

    
    while True:
        try:
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
                    point23 = lmList[0][23] #bacino sinistro
                    point24 = lmList[0][24] #bacino destro
                    point31 = lmList[0][31] #piede sinistro punta
                    point32 = lmList[0][32] #piede destro punta
            
                except:
                    pass         
            with open('piedi_traz.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                #voglio la differenza asse x tra punta piede sx e punta piede dx
                diff_piedi = abs(point31[0]-point32[0])
                writer.writerow([diff_piedi])
                #piu è vicino a 0 meglio è

            with open('schiena_traz.csv', 'a', newline='') as file: 
                writer = csv.writer(file)
                #distanza orizzontale tra spalla sinistra e bacino sinostro
                dist1 = abs(point11[0] - point23[0])
                dist2 = abs(point12[0] - point24[0])
                writer.writerow([dist1, dist2])
                #piu è vicino a 0 meglio è
            
            with open('gomiti_traz.csv', 'a', newline='') as file: 
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
        except:
            break     


def esegui(video_file):
    #leggo i parametri di thresold.txt(giusti)
    with open('pesi/trazioni/bene/thresold.txt', 'r') as file:
        data = file.readlines()
        piedi_vero = data[0].split(":")[1].strip()
        gomiti_vero = data[1].split(":")[1].strip()
        schiena_vero = data[2].split(":")[1].strip()
    start(video_file)
    take_thresold.run()
    #leggere i valori di thresold.txt
    with open('thresold.txt', 'r') as file:
        data = file.readlines()
        piedi = data[0].split(":")[1].strip()
        gomiti = data[1].split(":")[1].strip()
        schiena = data[2].split(":")[1].strip()
    #confrontare i valori
    err_gomiti = -1
    err_piedi = -1
    err_schiena = -1
    if float(gomiti) > float(gomiti_vero)+5:
        err_gomiti = "no" #errore nella posizione dei gomiti
    else:
        err_gomiti = "ok"
    if float(piedi) > float(piedi_vero)+10:
        err_piedi = "no" #errore nella posizione della schiena
    else:
        err_piedi = "ok"
    if float(schiena) > float(schiena_vero)+10:
        err_schiena = "no"
    else:
        err_schiena = "ok"
    return err_gomiti, err_piedi, err_schiena



