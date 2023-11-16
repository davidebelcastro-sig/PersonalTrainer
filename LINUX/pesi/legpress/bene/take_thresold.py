import pandas as pd
# Sostituisci 'file.csv' con il percorso del tuo file CSV
df = pd.read_csv('piedi_bn_sus_leg.csv')
media= df['piede'].mean()
fp = open("thresold.txt", "a")
fp.write("Piedi: " + str(media) + "\n")



df = pd.read_csv('scende_bn_sus_leg.csv')
media_colonna0 = df['sx'].mean()
#media_colonna1 = df['dx'].mean()
#media = (media_colonna0 + media_colonna1) / 2
fp.write("Scende: " + str(media_colonna0) + "\n")
