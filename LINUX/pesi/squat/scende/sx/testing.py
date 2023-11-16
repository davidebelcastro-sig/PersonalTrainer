import pickle
import keras
import numpy as np
import os

with open('modello_cnn_scende.pkl', 'rb') as file:
    model = pickle.load(file)

def run(path):
    #testing su una foto
    input_shape = (64, 64, 3)  # Dimensione dell'immagine di input
    img = keras.preprocessing.image.load_img(path, target_size=input_shape[:2])
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalizzazione

    class_index = np.argmax(model.predict(img_array), axis=1)[0]

    class_names = ["no","ok"]
    result = class_names[class_index]
    return result


if __name__ == "__main__":

    i = 0
    for el in os.listdir("test/ok"):
        i += 1
        path = "test/ok/"+el
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
        print("test: ",i)
        print("INPUT: ",path)
        print("Expected: ok")
        print(f"Result: {class_label}")
        print(predictions[0,0])
        print("\n\n\n\n\n\n")
    for el in os.listdir("test/no"):
        i+=1
        path = "test/no/"+el
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
        print("test: ",i)
        print("INPUT: ",path)
        print("Expected: no")
        print(f"Result: {class_label}")
        print(predictions[0,0])
        print("\n\n\n\n\n\n")








