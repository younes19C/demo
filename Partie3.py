import numpy as np
from Partie1 import ouvrirImage

#***************\\ Question1: Calcule la luminance moyenne de l'image.//*******************
def luminance(Img):
    return (Img.max() + Img.min()) / 2

#***************\\ Question2: Calcule le contraste de l'image.//*******************
def contraste(Img):
    s = 0
    for i in Img:
        for j in i:
            s += (j[0] - luminance(Img))**2  #Utilisation de j[0] car les trois canaux ont la même valeur
    return (1 / (len(Img) * len(Img[0]))) * s

#***************\\ Question3: Valeur maximale d'un pixel dans l'image.//*******************
def profondeur(Img):
    # Détermine la profondeur de couleur (en bits) de l'image.
    if Img.ndim == 2:
        if Img.max() == 1:
            return 1
        else:
            return 8
    else:
        return 24  # Par unité de bits pour les images couleur

#***************\\ Question4: La matrice représentant l'image A.//***************
def ouvrir(chemin="C:\\Users\\camar\\OneDrive\\Pictures\\Image du projet1.PNG"):
    return ouvrirImage(chemin)


