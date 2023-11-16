import pandas as pd
# Sostituisci 'file.csv' con il percorso del tuo file CSV
df = pd.read_csv('gomiti_dav_mal_pieg.csv')
media_colonna0 = df['sx'].mean()
media_colonna1 = df['dx'].mean()
media = (media_colonna0 + media_colonna1) / 2
fp = open("thresold.txt", "a")
fp.write("Gomiti: " + str(media) + "\n")

# Sostituisci 'file.csv' con il percorso del tuo file CSV
df = pd.read_csv('mani_spalle_larghe_dav_mal_pieg.csv')
media_colonna0 = df['sx'].mean()
media_colonna1 = df['dx'].mean()
media = (media_colonna0 + media_colonna1) / 2
fp = open("thresold.txt", "a")
fp.write("Spalle(Larghe): " + str(media) + "\n")

# Sostituisci 'file.csv' con il percorso del tuo file CSV
df = pd.read_csv('mani_spalle_strette_dav_mal_pieg.csv')
media_colonna0 = df['sx'].mean()
media_colonna1 = df['dx'].mean()
media = (media_colonna0 + media_colonna1) / 2
fp = open("thresold.txt", "a")
fp.write("Spalle(Strette): " + str(media) + "\n")
