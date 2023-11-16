import pandas as pd
import os

def run():
    # Sostituisci 'file.csv' con il percorso del tuo file CSV
    try:
        os.remove("thresold.txt")
    except:
        pass
    df = pd.read_csv('piede_leg.csv')
    media = df['piede'].mean()
    fp = open("thresold.txt", "a")
    fp.write("Piede: " + str(media) + "\n")

    # Sostituisci 'file.csv' con il percorso del tuo file CSV
    df = pd.read_csv('scende_leg.csv')
    media_colonna0 = df['sx'].mean()
    media_colonna1 = df['dx'].mean()
    media = (media_colonna0 + media_colonna1) / 2
    fp = open("thresold.txt", "a")
    fp.write("Scende: " + str(media_colonna0) + "\n")


