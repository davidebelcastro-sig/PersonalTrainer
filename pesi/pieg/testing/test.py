import cv2
from cvzone.PoseModule import PoseDetector
import csv
import numpy as np
import os
from pesi.pieg.testing import take_thresold
#import take_thresold solo su esecuzione singola senza gui

def start(video_file):
    cap = cv2.VideoCapture(video_file)
    detector = PoseDetector()
    try:
        os.remove("spalla_pieg.csv")
    except:
        pass
    try:
        os.remove("gomito_pieg.csv")
    except:
        pass
    with open('spalla_pieg.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["sx", "dx"])
    with open('gomito_pieg.csv', 'a', newline='') as file:
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
                    media_manosx_x = np.mean([point15[0], point17[0], point19[0], point21[0]])
                    media_manodx_x = np.mean([point16[0], point18[0], point20[0], point22[0]])
                except:
                    pass         
            with open('spalla_pieg.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                #calcolo differenza asse x tra mano sx e spalla sx
                diff_sx = abs(point11[0] - media_manosx_x)
                #calcolo differenza asse x tra mano dx e spalla dx
                diff_dx = abs(point12[0] - media_manodx_x)
                writer.writerow([diff_sx, diff_dx])

            with open('gomito_pieg.csv', 'a', newline='') as file: 
                writer = csv.writer(file)
                #calcolo differenza asse x tra gomito sx e spalla sx
                diff_sx = abs(point11[0] - point13[0])
                #calcolo differenza asse x tra gomito dx e spalla dx
                diff_dx = abs(point12[0] - point14[0])
                writer.writerow([diff_sx, diff_dx])
                        


        #y aumenta verso il basso
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except:
            break     


def esegui(video_file):
    #leggo i parametri di thresold.txt(giusti)
    with open('pesi/pieg/bene/thresold.txt', 'r') as file:
        data = file.readlines()
        gomiti_vero = data[0].split(":")[1].strip()
        spalle_vero = data[1].split(":")[1].strip()
    start(video_file)
    take_thresold.run()
    #leggere i valori di thresold.txt
    with open('thresold.txt', 'r') as file:
        data = file.readlines()
        gomiti = data[0].split(":")[1].strip()
        spalla = data[1].split(":")[1].strip()
    #confrontare i valori
    err_gomiti = -1
    err_spalle = -1
    if float(gomiti) > float(gomiti_vero)+10:
        err_gomiti = "no" #errore nella posizione dei gomiti
    else:
        err_gomiti = "ok"
    if float(spalla) > float(spalle_vero)+10:
        err_spalle = "no" #errore nella posizione della schiena
    else:
        err_spalle = "ok"
    return err_gomiti, err_spalle


