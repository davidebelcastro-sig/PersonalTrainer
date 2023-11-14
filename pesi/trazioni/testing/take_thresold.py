import pandas as pd
import os

def run():
    # Sostituisci 'file.csv' con il percorso del tuo file CSV
    try:
        os.remove("thresold.txt")
    except:
        pass

    df = pd.read_csv('piedi_traz.csv')
    media = df['piede'].mean()
    fp = open("thresold.txt", "a")
    fp.write("Piedi: " + str(media) + "\n")   

    df = pd.read_csv('gomiti_traz.csv')
    media_colonna0 = df['sx'].mean()
    media_colonna1 = df['dx'].mean()
    #media = (media_colonna0 + media_colonna1) / 2
    fp = open("thresold.txt", "a")
    fp.write("Gomiti: " + str(media_colonna0) + "\n")

    # Sostituisci 'file.csv' con il percorso del tuo file CSV
    df = pd.read_csv('schiena_traz.csv')
    media_colonna0 = df['sx'].mean()
    media_colonna1 = df['dx'].mean()
    media = (media_colonna0 + media_colonna1) / 2
    fp = open("thresold.txt", "a")
    fp.write("Schiena: " + str(media_colonna0) + "\n")


