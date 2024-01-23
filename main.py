from Partie1 import*
from Partie2 import*
from Partie3 import*
from Partie4 import*
from Partie5 import*
#*********\\ Fonction pour afficher le menu principal.//************
print("*************************************************")
print("********** WELCOME TO IMAGE PROCESSING **********")
print("*************************************************")
def afficher_menu_principal():
    print("\n---------------- Menu Principal  -----------------------------")
    print("1. Partie1 : Les opérations d'entrée/sortie sur les images")
    print("2. Partie2 : Les images Noir et blanc")
    print("3. Partie3 : Les images en niveau de gris")
    print("4. Partie4 : Opérations élémentaires sur les images en mode gris")
    print("5. Partie5 : Les images RGB")
    print("6. Quitter")
    choix_principal = input("Choisissez une option : ")
    return choix_principal

#******************\\ Fonction principale.//**********************
def main():
    choix_principal = afficher_menu_principal()

    while choix_principal != "6":
        if choix_principal == "1":
            print("Sous-menu - Les opérations d'entrée/sortie sur les images")
            print("1. Afficher une image")
            print("2. Ouvrir une image")
            print("3. Sauvegarder une image")
            print("4. Pour retourner au menu principal")
            choix_partie1 = input("Choisissez une option : ")

            if choix_partie1 == "1":
                ch=input("Donner le chemin de l'image : ")
                img=ouvrirImage(ch)
                AfficherImg(img)

            elif choix_partie1 == "2":
                ch=input("Donner le chemin de l'image : ")
                img=ouvrirImage(ch)
                AfficherImg(img)

            elif choix_partie1 == "3":
                ch=input("Donner le chemin de l'image : ")
                img=ouvrirImage(ch)
                saveImage(img)
                print("image sauvegardée")

            elif choix_partie1 == "4":
                choix_principal=6

            else:
                print("Option invalide. Veuillez réessayer.")

        if choix_principal == "2":
           #********\\ Partie 2 - Les images Noir et blanc.//*****
            print("Sous-menu - Les images Noir et blanc")
            print("1. Créer une image noire")
            print("2. Créer une image blanche")
            print("3. Créer une image noir et blanc")
            print("4. Créer le négatif d'une image")
            print("5. Pour retourner au menu principal")
            choix_partie2 = input("Choisissez une option : ")

            if choix_partie2 == "1":
                h = int(input("Hauteur de l'image noire : "))
                l = int(input("Largeur de l'image noire : "))
                img = image_noire(h, l)
                AfficherImg(img)
                print("Image noire créée avec succès!")

            elif choix_partie2 == "2":
                h = int(input("Hauteur de l'image blanche : "))
                l = int(input("Largeur de l'image blanche : "))
                img = image_blanche(h, l)
                AfficherImg(img)
                print("Image blanche créée avec succès!")

            elif choix_partie2 == "3":
                h = int(input("Hauteur de l'image noir et blanc : "))
                l = int(input("Largeur de l'image noir et blanc : "))
                img = creerImgBlancNoir(h, l)
                AfficherImg(img)
                print("Image noir et blanc créée avec succès!")

            elif choix_partie2 == "4":
                chemin = input("Chemin de l'image : ")
                img = ouvrirImage(chemin)
                img_negatif = negatif(img)
                AfficherImg(img_negatif)
                print("Négatif de l'image créé avec succès!")
            elif choix_partie2 == "5":
                choix_principal=6
            else:
                print("Option invalide. Veuillez réessayer.")

        elif choix_principal == "3":
            #**********\\ Partie 3 - Les images en niveau de gris.//**************
            print("Sous-menu - Les images en niveau de gris")
            print("1. Calculer la luminance d'une image")
            print("2. Calculer le contraste d'une image")
            print("3. Afficher la profondeur d'une image")
            print("4. Ouvrir une image (qui retourne la matrice de l'image indiquer dans le projet)")
            print("5. Pour retourner au menu principal")
            choix_partie3 = input("Choisissez une option : ")

            if choix_partie3 == "1":
                chemin = input("Chemin de l'image : ")
                img = ouvrir(chemin)
                lum = luminance(img)
                print("Luminance de l'image : ", lum)

            elif choix_partie3 == "2":
                chemin = input("Chemin de l'image : ")
                img = ouvrir(chemin)
                contr = constrast(img)
                print("Contraste de l'image : ", contr)

            elif choix_partie3 == "3":
                chemin = input("Chemin de l'image : ")
                img = ouvrir(chemin)
                prof = profondeur(img)
                print("Profondeur de l'image : ", prof, " bits par pixel")

            elif choix_partie3 == "4":
                img = ouvrir()
                print("La matrice de cette image A : ",img)
            
            elif choix_partie3 == "5":
                choix_principal=6

            else:
                print("Option invalide. Veuillez réessayer.")

        elif choix_principal == "4":
            #**********\\ Partie 4 - Opérations sur les images.//*********************
            print("Sous-menu - Opérations sur les images")
            print("1. Inverser une image")
            print("2. Effectuer la transformation par la symétrie d’axe vertical")
            print("3. Poser verticalement deux images")
            print("4. Poser horizontalement deux images")
            print("5. Pour retourner au menu principal")
            choix_partie4 = input("Choisissez une option : ")

            if choix_partie4 == "1":
                chemin = input("Chemin de l'image : ")
                img = ouvrir(chemin)
                img_inverse = inverser(img)
                AfficherImg(img_inverse)
                print("Inverse de l'image réalisé avec succès!")

            elif choix_partie4 == "2":
                chemin = input("Chemin de l'image : ")
                img = ouvrir(chemin)
                img_symV = flipH(img)
                AfficherImg(img_symV)
                print("Transformation par la symétrie d’axe vertical réalisée avec succès!")

            elif choix_partie4 == "3":
                chemin1 = input("Chemin de la première image : ")
                chemin2 = input("Chemin de la deuxième image : ")
                img1 = ouvrir(chemin1)
                img2 = ouvrir(chemin2)
                img_poseeV = poserV(img1, img2)
                AfficherImg(img_poseeV)
                print("Pose verticale des deux images réalisée avec succès!")

            elif choix_partie4 == "4":
                chemin1 = input("Chemin de la première image : ")
                chemin2 = input("Chemin de la deuxième image : ")
                img1 = ouvrir(chemin1)
                img2 = ouvrir(chemin2)
                img_poseeH = poserH(img1, img2)
                AfficherImg(img_poseeH)
                print("Pose horizontale des deux images réalisée avec succès!")

            elif choix_partie1 == "5":
                choix_principal=6

            else:
                print("Option invalide. Veuillez réessayer.")

        elif choix_principal == "5":
            #**********\\ Partie 5 - Traitement d'images avancé.//*****************
            print("Sous-menu - Traitement d'images avancé")
            print("1. Initialiser une image RGB (Partie 5)")
            print("2. Effectuer la symétrie horizontale d'une image RGB (Partie 5)")
            print("3. Effectuer la symétrie verticale d'une image RGB (Partie 5)")
            print("4. Convertir une image RGB en niveaux de gris (Partie 5)")
            print("5. Pour retourner au menu principal")
            choix_partie5 = input("Choisissez une option : ")

            if choix_partie5 == "1":
                h = int(input("Hauteur de l'image RGB : "))
                l = int(input("Largeur de l'image RGB : "))
                img_rgb = initImageRGB(h, l)
                AfficherImg(img_rgb)
                print("Image RGB créée avec succès!")

            elif choix_partie5 == "2":
                chemin = input("Chemin de l'image RGB : ")
                img_rgb = ouvrir(chemin)
                img_symH = symetrieH(img_rgb)
                AfficherImg(img_symH)
                print("Symétrie horizontale de l'image RGB réalisée avec succès!")

            elif choix_partie5 == "3":
                chemin = input("Chemin de l'image RGB : ")
                img_rgb = ouvrir(chemin)
                img_symV = symetrieV(img_rgb)
                AfficherImg(img_symV)
                print("Symétrie verticale de l'image RGB réalisée avec succès!")

            elif choix_partie5 == "4":
                chemin = input("Chemin de l'image RGB : ")
                img_rgb = ouvrir(chemin)
                img_gris = grayscale(img_rgb)
                AfficherImg(img_gris)
                print("Conversion de l'image RGB en niveaux de gris réalisée avec succès!")

            elif choix_partie5 == "5":
                choix_principal=6

            else:
                print("Option invalide. Veuillez réessayer.")

        else:
            print("Option invalide. Veuillez réessayer.")

        choix_principal = afficher_menu_principal()

    print("Programme terminé.")

#**********\\ Appeler la fonction principale.//*******************************
if __name__ == "__main__":
    main()