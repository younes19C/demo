import numpy as np
from Partie1 import AfficherImg 
#***************\\ Question1: Crée une image entièrement noire de dimensions h x l./*****
def image_noire(h, l):
    img = np.zeros((h, l))
    return img

#***************\\ Question2: Crée une image entièrement blanche de dimensions h x l./*****
def image_blanche(h, l):
    img = np.ones((h, l))
    return img

#**************\\ Question3: Crée une image en noir et blanc basée sur un motif de damier../*****
def creerImgBlancNoir(h, l):
    img = np.array([[(i + j) % 2 for i in range(l)] for j in range(h)])
    return img

#***************\\ Question4: Crée le négatif de l'image spécifiée.//*******************
def negatif(Img):
    img = np.array([[1 - j for j in i] for i in Img])
    return img

AfficherImg(image_noire(10,10))
AfficherImg(image_blanche(10,10))
AfficherImg(creerImgBlancNoir(10,10))
AfficherImg(negatif(creerImgBlancNoir(10,10)))

