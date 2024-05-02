import tkinter as tk
import cv2 as cv
import numpy as np
from PIL import ImageTk, Image
from tkinter import filedialog as fd

A = 0


def select_files():
    global A
    label.config(image=None)
    filetypes = (
        ('image files', '*.jpg'),
        ('image files', '*.jpeg'),
        ('image files', '*.jfif'),
        ('image files', '*.pjpeg'),
        ('image files', '*.pjp'),
        ('image files', '*.png'),
        ('All files', '*.*')
    )
    filenames = fd.askopenfilename(
        title='Open files',
        initialdir='/',
        filetypes=filetypes
    )
    image = Image.open(filenames)
    A = cv.imread(filename=filenames)
    A = cv.cvtColor(A, cv.COLOR_BGR2RGB)
    image = image.resize((316, 392))
    test = ImageTk.PhotoImage(image)
    label.config(image=test)
    label.image = test
    save = tk.Button(fenetre, command=save_image, text="Sauvegarder")
    save.place(x=828, y=507, width=158, height=42)
    label.place(x=32, y=91)


B = 0


def save_image():
    global B
    if type(B) == np.ndarray:
        B = cv.cvtColor(B, cv.COLOR_RGB2BGR)
        folder_path = fd.askdirectory()
        if folder_path:
            cv.imwrite(f"{folder_path}/modified.png", B)
    else:
        pass


def traiter(event):
    global A, B
    if type(A) == np.ndarray:
        B = A
        B = B.astype(np.float64)
        if bleu.get() > 100:
            B[:, :, 2] = (255 - B[:, :, 2]) * ((bleu.get() - 100) / 100) + B[:, :, 2]
        else:
            B[:, :, 2] = B[:, :, 2] * bleu.get() / 100
        if vert.get() > 100:
            B[:, :, 1] = (255 - B[:, :, 1]) * ((vert.get() - 100) / 100) + B[:, :, 1]
        else:
            B[:, :, 1] = B[:, :, 1] * vert.get() / 100
        if rouge.get() > 100:
            B[:, :, 0] = (255 - B[:, :, 0]) * ((rouge.get() - 100) / 100) + B[:, :, 0]
        else:
            B[:, :, 0] = B[:, :, 0] * rouge.get() / 100
        B = B.astype(np.uint8)
        array_to_img = Image.fromarray(B, "RGB")
        image = array_to_img.resize((316, 392))
        test = ImageTk.PhotoImage(image)
        label1.config(image=None)
        label1.config(image=test)
        label1.image = test
        label1.place(x=670, y=91)
    else:
        pass


fenetre = tk.Tk()

fenetre.title("hello")
fenetre.geometry("1000x600")
fenetre.resizable(False, False)

blue_label = tk.Label(fenetre, text="Bleu")
green_label = tk.Label(fenetre, text="Vert")
red_label = tk.Label(fenetre, text="Rouge")

bleu = tk.Scale(fenetre, from_=0, to=200, orient=tk.HORIZONTAL, command=traiter)
bleu.set(100)
vert = tk.Scale(fenetre, from_=0, to=200, orient=tk.HORIZONTAL, command=traiter)
vert.set(100)
rouge = tk.Scale(fenetre, from_=0, to=200, orient=tk.HORIZONTAL, command=traiter)
rouge.set(100)
get_image = tk.Button(fenetre, text="Open file", command=select_files)
get_image.place(x=32, y=30, width=158, height=42)

label = tk.Label(image=None)
label1 = tk.Label(image=None)
red_label.place(x=411, y=51, width=195, height=51)
rouge.place(x=411, y=122, width=195, height=51)
green_label.place(x=411, y=193, width=195, height=51)
vert.place(x=411, y=264, width=195, height=51)
blue_label.place(x=411, y=335, width=195, height=51)
bleu.place(x=411, y=406, width=195, height=51)

fenetre.mainloop()
