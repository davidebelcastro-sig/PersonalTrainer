import customtkinter
import tkinter as tk
from tkinter import PhotoImage, filedialog
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from sys import platform
import cv2
import corsa.testing.test as run
import pesi.squat.check_sx as squat
import pesi.pieg.testing.test as pieg
from tkinter import messagebox
import multiprocessing

def show_popup(title,comment):
    messagebox.showinfo(title,comment)

def on_closing():
    if messagebox.askokcancel("Chiusura", "Vuoi davvero chiudere l'applicazione?"):
        root.destroy()



def select_video_corsa():
    start="./corsa/testing/"
    # Apre una finestra di dialogo per selezionare un video
    video_file = filedialog.askopenfilename(initialdir=start,filetypes=[("Video files", "*.mp4 *.avi *.mkv *.mov *.MOV")])
    # Verifica se l'utente ha selezionato un video o ha annullato la finestra di dialogo
    if video_file:
        # Apre il video
        result = multiprocessing.Queue()
        process = multiprocessing.Process(target=run.esegui, args=(video_file,result,))
        process.start()
        cap = cv2.VideoCapture(video_file)
        # Verifica se il video è stato aperto correttamente
        if not cap.isOpened():
            print("Errore nell'apertura del video")
            exit()
        
        # Calcola l'altezza in base all'aspetto originale del video
        original_width = int(cap.get(3))
        original_height = int(cap.get(4))
        if original_width > original_height: #se il video è orizzontale
            desired_width = original_width // 2
            desired_height = int(desired_width * original_height / original_width)
        else: #se il video è verticale
            desired_height = original_height // 2
            desired_width = int(desired_height * original_width / original_height)
        cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Video', desired_width, desired_height)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Video', frame)
            # Gestione dell'evento di chiusura della finestra
            key = cv2.waitKey(25)
            if key == ord('q') or cv2.getWindowProperty('Video', cv2.WND_PROP_VISIBLE) < 1:
                break

        process.join()
        risultati = result.get()
        gomiti,schiena,volto = risultati
        show_popup("Giudizio Corsa", "Gomiti: " + gomiti + "\n"
                            "Schiena: " + schiena + "\n"
                            "Volto: " + volto)
        cap.release()
        cv2.destroyAllWindows()


def select_video_piegamenti():
    start = "./pesi/pieg/video/test"
    # Apre una finestra di dialogo per selezionare un video
    video_file = filedialog.askopenfilename(initialdir=start,filetypes=[("Video files", "*.mp4 *.avi *.mkv *.mov *.MOV")])
    # Verifica se l'utente ha selezionato un video o ha annullato la finestra di dialogo
    if video_file:
        # Apre il video
        result = multiprocessing.Queue()
        process = multiprocessing.Process(target=pieg.esegui, args=(video_file,result,))
        process.start()
        cap = cv2.VideoCapture(video_file)
        # Verifica se il video è stato aperto correttamente
        if not cap.isOpened():
            print("Errore nell'apertura del video")
            exit()
        
        # Calcola l'altezza in base all'aspetto originale del video
        original_width = int(cap.get(3))
        original_height = int(cap.get(4))
        if original_width > original_height: #se il video è orizzontale
            desired_width = original_width // 2
            desired_height = int(desired_width * original_height / original_width)
        else: #se il video è verticale
            desired_height = original_height // 2
            desired_width = int(desired_height * original_width / original_height)
        cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Video', desired_width, desired_height)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Video', frame)
            # Gestione dell'evento di chiusura della finestra
            key = cv2.waitKey(25)
            if key == ord('q') or cv2.getWindowProperty('Video', cv2.WND_PROP_VISIBLE) < 1:
                break
        process.join()
        risultati = result.get()
        gomiti,spalle = risultati
        show_popup("Giudizio Piegamenti braccia", "Gomiti: " + gomiti + "\n"
                            "Braccia: " + spalle)
        cap.release()
        cv2.destroyAllWindows()


def select_video_squat():
    # Apre una finestra di dialogo per selezionare un video
    start = "./pesi/squat/video/test"
    video_file = filedialog.askopenfilename(initialdir=start,filetypes=[("Video files", "*.mp4 *.avi *.mkv *.mov *.MOV")])
    # Verifica se l'utente ha selezionato un video o ha annullato la finestra di dialogo
    if video_file:
        # Apre il video
        cap = cv2.VideoCapture(video_file)
        # Verifica se il video è stato aperto correttamente
        if not cap.isOpened():
            print("Errore nell'apertura del video")
            exit()
        
        # Calcola l'altezza in base all'aspetto originale del video
        original_width = int(cap.get(3))
        original_height = int(cap.get(4))
        if original_width > original_height: #se il video è orizzontale
            desired_width = original_width // 2
            desired_height = int(desired_width * original_height / original_width)
        else: #se il video è verticale
            desired_height = original_height // 2
            desired_width = int(desired_height * original_width / original_height)
        cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Video', desired_width, desired_height)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Video', frame)
            # Gestione dell'evento di chiusura della finestra
            key = cv2.waitKey(25)
            if key == ord('q') or cv2.getWindowProperty('Video', cv2.WND_PROP_VISIBLE) < 1:
                break

        scende,schiena = squat.esegui(video_file)
        show_popup("Giudizio Squat", "Schiena: " + schiena + "\n"
                            "Scende: " + scende)
        cap.release()
        cv2.destroyAllWindows()

def select_video_nuoto():
    start="./nuoto/testing/"
    # Apre una finestra di dialogo per selezionare un video
    video_file = filedialog.askopenfilename(initialdir=start,filetypes=[("Video files", "*.mp4 *.avi *.mkv *.mov *.MOV")])
    # Verifica se l'utente ha selezionato un video o ha annullato la finestra di dialogo
    if video_file:
        # Apre il video
        cap = cv2.VideoCapture(video_file)
        # Verifica se il video è stato aperto correttamente
        if not cap.isOpened():
            print("Errore nell'apertura del video")
            exit()
        
        # Calcola l'altezza in base all'aspetto originale del video
        original_width = int(cap.get(3))
        original_height = int(cap.get(4))
        if original_width > original_height: #se il video è orizzontale
            desired_width = original_width // 2
            desired_height = int(desired_width * original_height / original_width)
        else: #se il video è verticale
            desired_height = original_height // 2
            desired_width = int(desired_height * original_width / original_height)
        cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Video', desired_width, desired_height)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Video', frame)
            # Gestione dell'evento di chiusura della finestra
            key = cv2.waitKey(25)
            if key == ord('q') or cv2.getWindowProperty('Video', cv2.WND_PROP_VISIBLE) < 1:
                break
        cap.release()
        cv2.destroyAllWindows()


width = 589
height = 600

root = customtkinter.CTk()
root.title("AI Personal trainer")
# Imposta la funzione on_closing come gestore della chiusura della finestra
root.protocol("WM_DELETE_WINDOW", on_closing)

x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.resizable(False, False)

#root.iconbitmap("sport_icon.ico")


# Carica l'immagine da utilizzare come sfondo 
background_image = Image.open("pic1.png")
enhancer = ImageEnhance.Brightness(background_image)
# Scurisci l'immagine
darkened_background = enhancer.enhance(0.6)  # Modifica il valore per regolare l'intensità del darkening
draw = ImageDraw.Draw(darkened_background)
font = ImageFont.truetype("Gobold Bold Italic.otf", 50)
draw.text((400, 350), "AI personal \n  trainer", font=font, fill="#93f233")
darkened_background.save("pic1_darkened.png")


# Carica l'immagine scurita come sfondo
background_image = PhotoImage(file="pic1_darkened.png")
# Crea una label con l'immagine come sfondo
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Copre l'intera finestra principale


btn1 = customtkinter.CTkButton(master = root, text = "Squat", height=40, corner_radius=8, fg_color="transparent",
                hover_color="white", border_color="#93f233", text_color="#93f233", border_width=2, command=select_video_squat)
btn1.place(relx=0.3, rely=0.7, anchor="center")
btn2 = customtkinter.CTkButton(master = root, text = "Piegamenti braccia", height=40, corner_radius=8, fg_color="transparent", 
                hover_color="white", border_color="#93f233", text_color="#93f233", border_width=2, command=select_video_piegamenti)
btn2.place(relx=0.7, rely=0.7, anchor="center")
btn3 = customtkinter.CTkButton(master = root, text = "Corsa", height=40, corner_radius=8, fg_color="transparent", 
                hover_color="white", border_color="#93f233", text_color="#93f233", border_width=2, command=select_video_corsa)
btn3.place(relx=0.3, rely=0.8, anchor="center")
btn4 = customtkinter.CTkButton(master = root, text = "Nuoto", height=40, corner_radius=8, fg_color="transparent", 
                hover_color="white", border_color="#93f233", text_color="#93f233", border_width=2, command=select_video_nuoto)
btn4.place(relx=0.7, rely=0.8, anchor="center")


root.mainloop()
