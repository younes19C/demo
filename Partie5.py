import random
import numpy as np
from math import floor

# M=[[[210, 100, 255],[100, 50, 255],[90, 90, 255],[90, 90, 255],[90, 90, 255],[90, 80, 255]],
# [[190, 255,89],[ 201, 255,29],[200, 255,100],[100, 255,90],[20, 255,200], [100, 255,80]],
# [[255,0, 0],[ 255,0, 0],[255,0, 0],[255,0, 0],[255,0, 0], [255,0, 0]]]
#****\\ Question 1: Valeurs des expressions suivantes : //*****#
# # print(M[0][1][1]) ------> le resultat est : 50
# # print(M[1][0][1]) ------> le resultat est : 255
# # print(M[2][1][0]) ------> le resultat est : 255
#*******************\\ Question 2: Valeurs des expressions suivantes : //***************
"""
La quantité de mémoire nécessaire pour stocker une image RGB en octets peut être
calculée en utilisant la formule M*N*3/8 où M et N représentent les dimensions
l'image en pixels.
Justification :
        Chaque pixel utilise trois canaux (Rouge, Vert, Bleu), et avec une profondeur 
        de couleur de 8 bits par canal, chaque canal nécessite 8 bits (1 octet).
        La formule (M * N * 3) / 8 exprime la quantité totale de mémoire
        nécessaire en octets pour stocker une image de dimensions M x N.
"""
#******\\ Question3: Fonction pour initialiser une image RGB avec des valeurs aléatoires.//****
def initImageRGB(h, l):
    """Initialise une image RGB avec des valeurs de pixels aléatoires."""
    img = [[[random.randrange(255) for i in range(3)] for j in range(l)] for k in range(h)]
    return img
#***************\\ Question 4: Symétrie horizontale et verticale.//***********************
# Q4 >> a
def symetrieH(img):
    """Effectue la symétrie horizontale de l'image."""
    return img[::-1]

# Q4 >> b
def symetrieV(img):
    """Effectue la symétrie verticale de l'image."""
    img3 = [[[0] for i in range(len(img[0]))] for j in range(len(img))]
    for i in range(len(img)):
        img3[i] = list(img[i][::-1])
    return np.array(img3)

#***************\\ Question 5: Renvoie une image en niveaux de gris... //********************
def grayscale(imageRGB):
    """Convertit une image RGB en niveaux de gris en calculant la moyenne des composantes de couleur."""
    e = [[floor(((j.max() + j.min()) / 2)) for j in i] for i in np.array(imageRGB)]
    return e
