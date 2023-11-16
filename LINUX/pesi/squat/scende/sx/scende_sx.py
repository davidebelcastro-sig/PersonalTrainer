import cv2
import time
from cvzone.PoseModule import PoseDetector
import csv
import numpy as np
import matplotlib.pyplot as plt




def crea_grafico(path,name):
    cap = cv2.VideoCapture(path)
    detector = PoseDetector()
    total_points = {}
    total_points['scende_sx'] = []
    while True:
        try:    
            success, img = cap.read()
            #img = cv2.resize(img, (1174, 724))
            #print(img.shape)
            img = detector.findPose(img)
            lmList = detector.findPosition(img, draw=False)

            if lmList:
                try:
                    point25 = lmList[0][25] #gamba sinistra
                    point23 = lmList[0][23] #bacino sinistro
                    cv2.imshow("run", img)
                    scende_sx = abs(point25[1] - point23[1])
                    total_points['scende_sx'].append([scende_sx])
                except:
                    pass
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except:
            break

    #plot i punti schiena sx
    y_scende_sx = []
    for i in range(len(total_points['scende_sx'])):
        y_scende_sx.append(i)
    x_scende_sx = []
    for i in range(len(total_points['scende_sx'])):
        x_scende_sx.append(total_points['scende_sx'][i][0])

        
    plt.plot(x_scende_sx, y_scende_sx, label = "scende sx")
    plt.savefig(name)
    plt.clf()


def start():
    path = "video/test/bene.MOV"
    name = "test_bene.png"
    crea_grafico(path,name)
    path = "video/test/male.MOV"
    name = "test_male.png"
    crea_grafico(path,name)


if __name__ == "__main__":
    start()

