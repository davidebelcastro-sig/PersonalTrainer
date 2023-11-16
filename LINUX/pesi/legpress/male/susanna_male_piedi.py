import cv2
import time
from cvzone.PoseModule import PoseDetector
import csv


cap = cv2.VideoCapture("./video/legpress_male1.mov")
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
            point23 = lmList[0][23] #bacino sinistro
            point24 = lmList[0][24] #bacino destro
            point29 = lmList[0][29] #tallone sinistro
            point30 = lmList[0][30] #tallone destro
            point31 = lmList[0][31] #piede sinistro punta
            point32 = lmList[0][32] #piede destro punta
        except:
            pass

    cv2.imshow("run", img)

    
    with open('./male/piedi_mal_sus_leg.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        #voglio la differenza asse y tra punta piede sx e punta piede dx
        diff_piedi = abs(point31[1]-point32[1])
        writer.writerow([diff_piedi])
        #piu è vicino a 0 meglio è


   #y aumenta verso il basso
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

