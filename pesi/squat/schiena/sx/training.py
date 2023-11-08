import tensorflow as tf
from tensorflow import keras
import numpy as np
import pickle

# Parametri
input_shape = (64, 64, 3)  # Dimensione dell'immagine di input
num_classes = 1  # Numero di classi (solo 'ok')

# Creazione del modello CNN
def create_model(input_shape, num_classes):
    model = keras.Sequential([
        keras.layers.Input(shape=input_shape),
        keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Flatten(),
        keras.layers.Dense(512, activation='relu'),
        keras.layers.Dense(num_classes, activation='sigmoid')  # Cambia 'softmax' a 'sigmoid'
    ])
    return model

# Creazione del modello
model = create_model(input_shape, num_classes)

# Compilazione del modello
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  # Cambia la funzione di loss

# Fase di allenamento
train_data_dir = 'train'

train_datagen = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=input_shape[:2],
    batch_size=32,
    class_mode='binary')  # Utilizziamo 'binary' poiché ora abbiamo solo due classi (ok e non ok)

model.fit(train_generator, epochs=10)
# Salva il modello in un file
with open('modello_cnn_schiena.pkl', 'wb') as file:
    pickle.dump(model, file)
