import os

file_path1 = "./pesi/squat/scende/sx/modello_cnn_scende.pkl"
file_path2 = "./pesi/squat/schiena/sx/modello_cnn_schiena.pkl"

if os.path.exists(file_path1):
    os.remove(file_path1)
    print("File Removed!")
else:
    print("File not exist!")

if os.path.exists(file_path2):
    os.remove(file_path2)
    print("File Removed!")
else:
    print("File not exist!")
