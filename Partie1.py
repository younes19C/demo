from matplotlib import pyplot as plt

#***************\\ Question 1 : Affiche une image en niveaux de gris.//****************
def AfficherImg(img, m=1, n=0):
    plt.axis("off")  # désactive les axes
    plt.imshow(img, cmap='gray', interpolation="nearest", vmax=m, vmin=n)
    plt.show()

#***************\\ Question 2 : Ouvre une image à partir du chemin spécifié. //********
def ouvrirImage(chemin):
    img = plt.imread(chemin)
    return img

#*************\\ Question 3 :Enregistre l'image spécifiée sous le nom 'image1.png'.//**
def saveImage(img):
    plt.imsave("image1.png", img)





