import cv2
from cvzone.PoseModule import PoseDetector
import matplotlib.pyplot as plt
import keras
import numpy as np
import pickle



with open('pesi/squat/schiena/sx/modello_cnn_schiena.pkl', 'rb') as file:
    model_schiena = pickle.load(file)

with open('pesi/squat/scende/sx/modello_cnn_scende.pkl', 'rb') as file:
    model_scende = pickle.load(file)

def crea_grafico(path,name1,name2):
    cap = cv2.VideoCapture(path)
    detector = PoseDetector()
    total_points = {}
    total_points['scende_sx'] = []
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
                    point25 = lmList[0][25] #gamba sinistra
                    point23 = lmList[0][23] #bacino sinistro
                    #cv2.imshow("run", img)
                    scende_sx = abs(point25[1] - point23[1])
                    total_points['scende_sx'].append([scende_sx])
                    point11 = lmList[0][11] #spalla sinistra
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
    y_scende_sx = []
    for i in range(len(total_points['scende_sx'])):
        y_scende_sx.append(i)
    x_scende_sx = []
    for i in range(len(total_points['scende_sx'])):
        x_scende_sx.append(total_points['scende_sx'][i][0])
    plt.plot(x_scende_sx, y_scende_sx, label = "scende sx")
    plt.savefig(name1)
    plt.clf()

    #plot i punti schiena sx
    x_schiena_sx = []
    for i in range(len(total_points['schiena_sx'])):
        x_schiena_sx.append(i)
    y_schiena_sx = []
    for i in range(len(total_points['schiena_sx'])):
        y_schiena_sx.append(total_points['schiena_sx'][i][0])

        
    plt.plot(x_schiena_sx, y_schiena_sx, label = "schiena sx")
    plt.savefig(name2)
    plt.clf()

def prediction_schiena(path,model):
    #testing su una foto
    input_shape = (64, 64, 3)  # Dimensione dell'immagine di input
    img = keras.preprocessing.image.load_img(path, target_size=input_shape[:2])
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalizzazione
    predictions = model.predict(img_array)
    # Classificazione "ok" o "non ok" in base alla probabilità di uscita
    threshold = 0.550  # Soglia per la classificazione
    if predictions[0,0] > threshold:
        class_label = 'ok'
    else:
        class_label = 'no'
    return class_label

def prediction_scende(path,model):
    #testing su una foto
    input_shape = (64, 64, 3)  # Dimensione dell'immagine di input
    img = keras.preprocessing.image.load_img(path, target_size=input_shape[:2])
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalizzazione
    predictions = model.predict(img_array)
    # Classificazione "ok" o "non ok" in base alla probabilità di uscita
    threshold = 0.645  # Soglia per la classificazione
    if predictions[0,0] > threshold:
        class_label = 'ok'
    else:
        class_label = 'no'
    return class_label
   

def esegui(path):
    name1 = "grafico_scende.png"
    name2 = "grafico_schiena.png"
    crea_grafico(path,name1,name2)
    risp_scende = prediction_scende(name1,model_scende)
    risp_schiena = prediction_schiena(name2,model_schiena)
    return risp_scende,risp_schiena



    

