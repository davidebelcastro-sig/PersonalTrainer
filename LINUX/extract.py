import zipfile

# Percorso del file ZIP da decomprimere
zip_file_path1 = "./pesi/squat/scende/sx/modello_cnn_scende.zip"
zip_file_path2 = "./pesi/squat/schiena/sx/modello_cnn_schiena.zip"

# Percorso della cartella di destinazione per l'estrazione
extracted_folder1 = "./pesi/squat/scende/sx/"
extracted_folder2 = "./pesi/squat/schiena/sx/"


#controllo che non sia gia stato estratto
import os.path
if os.path.exists(extracted_folder1+"modello_cnn_scende.pkl"):
    pass
else:
    # Apri il file ZIP in modalità lettura
    with zipfile.ZipFile(zip_file_path1, 'r') as zip_ref:
        # Estrai tutti i file contenuti nel file ZIP nella cartella di destinazione
        zip_ref.extractall(extracted_folder1)

if os.path.exists(extracted_folder2+"modello_cnn_schiena.pkl"):
    pass
else:
    # Apri il file ZIP in modalità lettura
    with zipfile.ZipFile(zip_file_path2, 'r') as zip_ref:
        # Estrai tutti i file contenuti nel file ZIP nella cartella di destinazione
        zip_ref.extractall(extracted_folder2)