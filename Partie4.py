import numpy as np
from Partie3 import *  

#***************\\ Question1: Inverse d'une image.//***************
def inverser(img):
    #Calcule l'inverse d'une image en inversant les valeurs des pixels.
    inv = np.array([[255 - j for j in i] for i in img])
    return inv

#***************\\ Question2: La transformée d'une image par la symétrie d’axe vertical.//****
def flipH(img):
    t = [img[i][::-1] for i in range(len(img))]  # Inverse l'ordre des pixels dans chaque ligne de l'image
    return t

#***************\\ Question3: Poser vertical d'une image.//***************
def poserV(img1, img2):
    # Superpose deux images verticalement si elles ont la même profondeur et la même largeur.
    img3 = []
    if profondeur(img1) == profondeur(img2) and len(img1[0]) == len(img2[0]):
        img3 += list(img1) + list(img2)  # Concatène les lignes des deux images pour créer une nouvelle image
        np.array(img3)
    return img3

#***************\\ Question4: Poser horizontal d'une image.//***************
def poserH(img1, img2):
    #Superpose deux images horizontalement si elles ont la même profondeur et la même hauteur.
    img3 = [[[0] for i in range(len(img1[0]) + len(img2[0]))] for j in range(len(img1))]
    if profondeur(img1) == profondeur(img2) and len(img1) == len(img2):
        for i in range(len(img1)):
            img3[i] = list(img1[i]) + list(img2[i])  # Concatène les colonnes des deux images pour créer une nouvelle image
    return np.array(img3)


