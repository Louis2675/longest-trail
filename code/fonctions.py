"""
Fichier qui contient l'ensemble des fonctions pour le bon fonctionnement du programme.
"""

from time import sleep
from graphes import Graphe


def permutations(liste, n):
    """
    Genere toutes les permutations d'une liste
    Entrée:
        liste (list): La liste à permuter.
        n (int): La taille des permutations.
    Sortie : 
        La liste de toutes les permutations.
    """
    if n == 0:
        return [[]]
    else:
        resultat = []
        for i in range(len(liste)): # Pour parcourir la liste
            reste = liste[:i] + liste[i+1:] # On initie premier element + reste
            for perm in permutations(reste, n-1): # Pour le reste
                resultat.append([liste[i]] + perm) # On ajoute dans les permutations
        return resultat


def permutations_de_taille_n(x, n):
    """
    Fonction qui genere toutes les permutations de taille n pour x nombres
    Entree : 
        x (int): Le nombre de nombres.
        n (int): La taille des permutations.
    """
    liste = [i for i in range(x)] # Liste des sommets
    return permutations(liste, n) # On fait toutes les permutations des tailles n 


def generer_parcours(graphe):
    """
    Génère tous les parcours possibles à travers le graphe.
    Entrée:
        graphe (Graphe): Le graphe à parcourir.
    Sortie:
        La liste de tous les parcours possibles.
    """
    liste_parcours = [] # liste des parcours a retourner
    for i in range(graphe.taille +1): # pour toutes les tailles
        liste_parcours.append(permutations_de_taille_n(graphe.taille, i)) # on met les permutations de taille i
    return liste_parcours


def arrete_existe(graphe, sommet1, sommet2):
    """
    Détermine si une arête existe entre deux sommets donnés.
    Entrée:
        graphe (Graphe): Le graphe à parcourir.
        sommet1 (int): Le premier sommet.
        sommet2 (int): Le deuxième sommet.
    Sortie:
        bool: True si une arête existe entre les deux sommets, False sinon.
    """
    for i in range(len(graphe.graphe[sommet1])): # On parcourt le graphe pour checker les arretes
        if graphe.graphe[sommet1][i][0] == sommet2: # Si les deux existent
            return True
    return False


def test_arretes_parcours(graphe, liste_parcours):
    """
    Vérifie si les arêtes d'un parcours sont valides dans le graphe.

    Entrée:
        graphe (Graphe): Le graphe à tester.
        liste_parcours (list): La liste des parcours à évaluer.

    Sortie:
        list: La liste des parcours valides.
    """
    liste_parcours_valide = [] # Liste des parcours a retourner
    for i in range(len(liste_parcours)): # on parcourt tous les parcours
        for j in range(len(liste_parcours[i])): # dans chaques tailles 
            valide = True
            for k in range(len(liste_parcours[i][j]) -1): # on verifie toutes les arretes
                if arrete_existe(graphe, liste_parcours[i][j][k], liste_parcours[i][j][k+1]) == False: # si l'arrete existe
                    valide = False
            if valide == True:
                liste_parcours_valide.append(liste_parcours[i][j]) # si tout est bon on ajoute
    return liste_parcours_valide            


def taille_arrete(graphe, sommet1, sommet2):
    """
    Détermine la taille d'une arête entre deux sommets donnés.
    Entrée:
        graphe (Graphe): Le graphe à parcourir.
        sommet1 (int): Le premier sommet.
        sommet2 (int): Le deuxième sommet.
    Sortie:
        int: La taille de l'arête entre les deux sommets, False si l'arête n'existe pas.
    """

    for i in range(len(graphe.graphe[sommet1])): # on parcourt le graphe
        if graphe.graphe[sommet1][i][0] == sommet2: # si l'arrete existe (evite des erreurs)
            return graphe.graphe[sommet1][i][1] # on retourne la taille de l'arrete
    return False


def taille_parcours(graphe, parcours):
    """
    Détermine la taille d'un parcours donné.
    Entrée:
        graphe (Graphe): Le graphe à parcourir.
        parcours (list): Le parcours à évaluer.
    Sortie:
        int: La taille du parcours, False si le parcours n'est pas valide.
    """
    taille = 0
    for i in range(len(parcours) - 1): # pour toutes les arretes du parcours
        taille += taille_arrete(graphe, parcours[i], parcours[i+1]) # on ajoute la taille de toutes les arretes
    return taille


def taille_maximale_parcours_valide(graphe):
    """
    Détermine la taille maximale d'un parcours valide dans le graphe.
    Entrée:
        graphe (Graphe): Le graphe à parcourir.
    Sortie:
        tuple: La taille maximale d'un parcours valide, son numero et le chemin en question
    """
    liste_parcours = generer_parcours(graphe) # liste de base
    liste_parcours_valide = test_arretes_parcours(graphe, liste_parcours) # liste avec les arretes valides
    taille_max = (0, 0)
    for i in range(len(liste_parcours_valide)): # on parcourt tous les chemins et on cherche le plus grand
        if taille_parcours(graphe, liste_parcours_valide[i]) > taille_max[0]: # si le chemin est plus grand que taille_max
            taille_max = (taille_parcours(graphe, liste_parcours_valide[i]), i, liste_parcours_valide[i]) # taille_max = chemin
    return taille_max


def taille_maximale_parcours_valide_suivi(graphe):
    """
    Détermine la taille maximale d'un parcours valide dans le graphe. avec suivi
    Entrée:
        graphe (Graphe): Le graphe à parcourir.
    Sortie:
        tuple: La taille maximale d'un parcours valide, son numero et le chemin en question
    """
    print("On commence par générer tous les parcours possibles (meme les parcours non valides)...")
    input()
    print()
    sleep(1)
    liste_parcours = generer_parcours(graphe) # on initie la liste
    print("On obtient les parcours suivants :")
    print(liste_parcours)
    print()
    sleep(1)
    print("On elimine ensuite les parcours avec les arretes non valides...")
    input()
    liste_parcours_valide = test_arretes_parcours(graphe, liste_parcours) # avec les parcours valides
    print()
    sleep(1)
    print("On obtient ensuite les parcours suivants : ")
    print(liste_parcours_valide)
    print()
    sleep(1)
    print("On determine ensuite le parcours avec la plus grande taille du lot...")
    input()
    sleep(1)
    taille_max = (0, 0)
    print("taille_max = 0")
    for i in range(len(liste_parcours_valide)): # pour trouver la taille-max
        if taille_parcours(graphe, liste_parcours_valide[i]) > taille_max[0]: # on compare chemin actuel avec ancien plus grand
            taille_max = (taille_parcours(graphe, liste_parcours_valide[i]), i, liste_parcours_valide[i]) # si actuel plus grand alors actuel = taille_max
            print("Le parcours {} est plus grand que la taille max, taille_max = {}".format(i, taille_parcours(graphe, liste_parcours_valide[i])))
    return taille_max


