import cv2
import time
from cvzone.PoseModule import PoseDetector
import csv
import numpy as np
import matplotlib.pyplot as plt




def start(path, name):
    cap = cv2.VideoCapture(path)
    detector = PoseDetector()
    total_points = {}
    total_points['schiena_sx'] = []
    while True:
        try:    
            success, img = cap.read()
            #img = cv2.resize(img, (1174, 724))
            #print(img.shape)
            img = detector.findPose(img)
            lmList = detector.findPosition(img, draw=False)

            if lmList:
                try:
                    point11 = lmList[0][11] #spalla sinistra
                    point23 = lmList[0][23] #bacino sinistro
                    cv2.imshow("run", img)
                    diffX_schiena_sx = point11[0] - point23[0]
                    diffX_schiena_sx = abs(diffX_schiena_sx)
                    total_points['schiena_sx'].append([diffX_schiena_sx])
                except:
                    pass
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except:
            break

    #plot i punti schiena sx
    x_schiena_sx = []
    for i in range(len(total_points['schiena_sx'])):
        x_schiena_sx.append(i)
    y_schiena_sx = []
    for i in range(len(total_points['schiena_sx'])):
        y_schiena_sx.append(total_points['schiena_sx'][i][0])

        
    plt.plot(x_schiena_sx, y_schiena_sx, label = "schiena sx")
    plt.savefig(name)
    plt.clf()

def run():
    path = "video/test/bene.MOV"
    name = "test_bene.png"
    start(path, name)
    path =  "video/test/male1.MOV"
    name = "test_male.png"
    start(path, name)


if __name__ == "__main__":
    run()