#!/usr/bin/env python3

from tkinter import *
import os
# from PIL import Image, ImageTk

chemin_absolu = os.path.abspath(__file__) # où est situé ce fichier
nom_dossier = os.path.dirname(chemin_absolu) # dans quel dossier
os.chdir(nom_dossier) # on se déplace dans ce dossier-là


fen = Tk()
fen.title("Sauver le Prince")

largeur_fen = 500
hauteur_fen = 500
fen.geometry(str(largeur_fen) + "x" + str(hauteur_fen) + "+0+0") # On redimensionne la fenêtre.
fond = Canvas(fen, width=largeur_fen, height=hauteur_fen, bg='#b0bec5')
fond.place(x=0, y=0)


# objet1=Label(fen,text="Sauver le Prince !",bg="#e64a19", font=("Times", 15, "bold"))
# objet1.place(x=205,y=450)

def sauver_prince():
    bouton_jouer.destroy()

    # relx=.5, rely=.5 -> on centre le repère au milieu

    titre = Label(fen, text="Choisissez un jeu !")
    titre.place(relx=.5, rely=.1, anchor="center")

    bouton1 = Button(fen, text="Guidez-moi jusqu'au château !", command=jeu1)
    bouton1.place(y = -75, relx=.5, rely=.5, anchor="center")

    bouton2 = Button(fen, text="Attention aux obstacles !", command=jeu2)
    bouton2.place(y = 0, relx=.5, rely=.5, anchor="center")

    bouton3 = Button(fen, text="Y'a qu'a casser les briques !", command=jeu3)
    bouton3.place(y = 75, relx=.5, rely=.5, anchor="center")

    quitter = Button(fen, text="Quitter", command=lambda: fen.destroy())
    quitter.place(relx=.5, rely=.9, anchor="center")

def jeu1():
    import Jeu1
def jeu2():
    import Jeu2
def jeu3():
    import Jeu3



#image = Image.open("Smiley Isn")
#photo = ImageTk.PhotoImage(image)

#canvas = Tk.Canvas(fen, width = image.size[0], height = image.size[1])
#canvas.create_image(0,0, anchor = Tk.NW, image=photo)
#canvas.pack()


bouton_jouer = Button(fen, text="Sauvez le Prince !", fg='blue', command=sauver_prince)
bouton_jouer.place(relx=.5, rely=.5, anchor="center")

fen.mainloop()
