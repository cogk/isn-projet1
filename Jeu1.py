# Victoire, Salomé, Mathieu
from tkinter import *
from random import randrange
import time

fen = Tk()
fen.title("Guidez-moi !")

largeur_fen = 500
hauteur_fen = 500
fen.geometry(str(largeur_fen) + "x" + str(hauteur_fen) + "+0+0") # On redimensionne la fenêtre.

canvas = Canvas(fen, width=largeur_fen, height=hauteur_fen, bg='#ccf')
canvas.place(x=0, y=0)

rayon_cercle = 12
diamètre_cercle = 2 * rayon_cercle

objets_cercles = []
objets_lignes = []
coordonnées_cercles = []
index_cercles_reliés = []

index_dernier_cercle = None # contient la position dans les listes du dernier cercle cliqué (pour faire partir la flèche suivante)

premier_clic = True
def événement_clic(event):
    global index_dernier_cercle, premier_clic

    x_souris, y_souris = event.x, event.y

    for i, cercle in enumerate(objets_cercles):
        if i in index_cercles_reliés: # si le cercle est déjà relié
            continue # on passe au prochain cercle pour tester s'il est cliqué

        # i est la position de `cercle` dans la liste `cercles` tout comme dans `coordonnées`.
        x1, y1, x2, y2 = coordonnées_cercles[i]
        if (x1 < x_souris < x2) and (y1 < y_souris < y2): # si le cercle est cliqué
            canvas.itemconfig(cercle, fill='red')
            milieu_dernier_cercle = ((x1 + x2)/2, (y1 + y2)/2)

            if (index_dernier_cercle != None):
                relier_cercles(index_dernier_cercle, i)

            index_dernier_cercle = i
            index_cercles_reliés.append(i)

            if premier_clic == True:
                premier_clic = False
                démarrer_chrono()

            if len(index_cercles_reliés) == len(objets_cercles):
                # Tous les cercles ont étés reliés.
                arrêter_chrono()

            break # on a trouvé le cercle cliqué : on arrête de tester les autres


def relier_cercles(indexA, indexB):
    tracer_ligne(coordonnées_cercles[indexA], coordonnées_cercles[indexB])

def tracer_ligne(coords_cercleA, coords_cercleB):
    xA, yA, _, _ = coords_cercleA
    xB, yB, _, _ = coords_cercleB
    ligne = canvas.create_line(xA + rayon_cercle, yA + rayon_cercle, xB + rayon_cercle, yB + rayon_cercle, fill='orange', width=2)
    objets_lignes.append(ligne)



heure_départ = None
durée_totale = None
record_chrono = None

def démarrer_chrono():
    global heure_départ
    heure_départ = time.time()

def arrêter_chrono():
    global durée_totale, record_chrono
    heure_arrivée = time.time()
    durée_totale = heure_arrivée - heure_départ

    if record_chrono == None:
        record_chrono = durée_totale
    elif durée_totale < record_chrono:
        record_chrono = durée_totale

label_chrono = Label(fen, text='(chrono)')
label_chrono.place(relx=0.5, rely=0.05, anchor='center')

label_record = Label(fen, text='Record: ---')
label_record.place(relx=0.85, rely=0.05, anchor='center')

def afficher_chrono():
    durée_actuelle = 0
    if heure_départ == None:
        durée_actuelle = 0
    elif durée_totale == None:
        durée_actuelle = time.time() - heure_départ
    else:
        durée_actuelle = durée_totale

    label_chrono.config(text='{:3.1f} secondes'.format(durée_actuelle))

    if record_chrono != None:
        label_record.config(text='Record: {:3.1f} s.'.format(record_chrono))

    fen.after(100, afficher_chrono)



def nouvelle_partie():
    global heure_départ, durée_totale, premier_clic, index_dernier_cercle, objets_cercles, objets_lignes, coordonnées_cercles, index_cercles_reliés
    heure_départ = None
    durée_totale = None
    premier_clic = True
    index_dernier_cercle = None

    for cercle in objets_cercles:
        canvas.delete(cercle)
    for ligne in objets_lignes:
        canvas.delete(ligne)

    objets_cercles = []
    objets_lignes = []
    coordonnées_cercles = []
    index_cercles_reliés = []

    for i in range(0, 14):
        x, y = randrange(diamètre_cercle, largeur_fen - diamètre_cercle), randrange(75 + diamètre_cercle, hauteur_fen - diamètre_cercle - 75)
        # On laisse une marge en haut et en bas pour le bouton, le chrono et le texte explicatif
        cercle = canvas.create_oval(x, y , x + diamètre_cercle, y + diamètre_cercle, fill='blue')

        objets_cercles.append(cercle)
        coordonnées_cercles.append((x, y , x + diamètre_cercle, y + diamètre_cercle))



label_règles = Label(fen, text='Cliquez pour relier les cercles le plus vite possible.')
label_règles.place(relx=0.5, rely=0.95, anchor='center')

Bouton_rejouer = Button(fen, text='Rejouer', command=nouvelle_partie)
Bouton_rejouer.place(relx=0.1, rely=0.05, anchor='center')

# On teste à chaque déplacement
fen.bind('<Button-1>', événement_clic)
fen.after(10, afficher_chrono)

nouvelle_partie()
fen.mainloop()