import os
import glob

def elimina_file_csv_png(directory):
    # Crea il percorso completo alla directory
    directory_path = os.path.abspath(directory)

    # Costruisci i pattern di ricerca per i file .csv e .png
    pattern_csv = os.path.join(directory_path, '*.csv')
    pattern_png = os.path.join(directory_path, 'grafico_*.png')

    # Utilizza glob per ottenere la lista dei file .csv e .png
    file_list_csv = glob.glob(pattern_csv)
    file_list_png = glob.glob(pattern_png)

    # Unisci le due liste di file
    file_list = file_list_csv + file_list_png

    # Elimina i file
    for file_path in file_list:
        try:
            os.remove(file_path)
            #print(f"File eliminato: {file_path}")
        except Exception as e:
            print(f"Errore durante l'eliminazione di {file_path}: {e}")

# Specifica il percorso della directory in cui desideri eliminare i file .csv e .png
directory_da_pulire = "."

# Chiama la funzione per eliminare i file .csv e .png
elimina_file_csv_png(directory_da_pulire)
