import pandas as pd
# Sostituisci 'file.csv' con il percorso del tuo file CSV
df = pd.read_csv('gomito_dav_mal_corsa.csv')
media_colonna0 = df['sx'].mean()
media_colonna1 = df['dx'].mean()
media = (media_colonna0 + media_colonna1) / 2
fp = open("thresold.txt", "a")
fp.write("Gomiti: " + str(media) + "\n")

# Sostituisci 'file.csv' con il percorso del tuo file CSV
df = pd.read_csv('schiena_dav_mal_corsa.csv')
media_colonna0 = df['sx'].mean()
media_colonna1 = df['dx'].mean()
media = (media_colonna0 + media_colonna1) / 2
fp = open("thresold.txt", "a")
fp.write("Schiena: " + str(media) + "\n")

# Sostituisci 'file.csv' con il percorso del tuo file CSV
df = pd.read_csv('volto_dav_mal_corsa.csv')
media_colonna0 = df['volto'].mean()
media = (media_colonna0 + media_colonna1) / 2
fp = open("thresold.txt", "a")
fp.write("Volto: " + str(media) + "\n")
