"""
Fichier contenant et initialisant la classe graphe et ses initialisations.
"""


from graphes import Graphe


def permutations(liste, n):
    if n == 0:
        return [[]]
    else:
        result = []
        for i in range(len(liste)):
            remaining_elements = liste[:i] + liste[i+1:]
            for perm in permutations(remaining_elements, n-1):
                result.append([liste[i]] + perm)
        return result


def permutations_de_taille_n(x, n):
    liste = [i for i in range(x)]
    return permutations(liste, n)


def generer_parcours(graphe):
    """
    Génère tous les parcours possibles à travers le graphe.
    Entrée:
        graphe (Graphe): Le graphe à parcourir.
    Sortie:
        list: La liste de tous les parcours possibles.
    """
    liste_parcours = []
    for i in range(graphe.taille +1):
        liste_parcours.append(permutations_de_taille_n(graphe.taille, i))
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
    for i in range(len(graphe.graphe[sommet1])):
        if graphe.graphe[sommet1][i][0] == sommet2:
            return True
    return False


def test_arretes_parcours(graphe, liste_parcours):
    liste_parcours_valide = []
    for i in range(len(liste_parcours)):
        for j in range(len(liste_parcours[i])):
            valide = True
            for k in range(len(liste_parcours[i][j]) -1):
                if arrete_existe(graphe, liste_parcours[i][j][k], liste_parcours[i][j][k+1]) == False:
                    valide = False
            if valide == True:
                liste_parcours_valide.append(liste_parcours[i][j])
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

    for i in range(len(graphe.graphe[sommet1])):
        if graphe.graphe[sommet1][i][0] == sommet2:
            return graphe.graphe[sommet1][i][1]
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
    for i in range(len(parcours) - 1):
        taille += taille_arrete(graphe, parcours[i], parcours[i+1])
    return taille


def taille_maximale_parcours_valide(graphe):
    """
    Détermine la taille maximale d'un parcours valide dans le graphe.
    Entrée:
        graphe (Graphe): Le graphe à parcourir.
    Sortie:
        int: La taille maximale d'un parcours valide.
    """
    liste_parcours = generer_parcours(graphe)
    liste_parcours_valide = test_arretes_parcours(graphe, liste_parcours)
    taille_max = (0, 0)
    for i in range(len(liste_parcours_valide)):
        if taille_parcours(graphe, liste_parcours_valide[i]) > taille_max[0]:
            taille_max = (taille_parcours(graphe, liste_parcours_valide[i]), i, liste_parcours_valide[i])
    return taille_max

def decidabilite(graphe, k):
    """
    Détermine si le graphe est k-coloriable.
    Entrée:
        graphe (Graphe): Le graphe à colorier.
        k (int): Le nombre de couleurs.
    Sortie:
        bool: True si le graphe est k-coloriable, False sinon.
    """
    if taille_maximale_parcours_valide(graphe)[0] >= k:
        return True
    return False


def calculabilite(graphe):
    return (taille_maximale_parcours_valide(graphe)[2], taille_maximale_parcours_valide(graphe)[0]) 


if __name__ == "__main__":
    # Créer un graphe à partir d'une liste d'adjacence pondérée
    G = Graphe([[(3, 2)], [(2, 1), (4, 3)], [(1,1), (4, 4), (3, 5)], [(0, 2), (2, 5)], [(1, 3), (2, 4)]], False)
    Gperm = Graphe([[(3, 2)], [(2, 1), (4, 3)], [(2, 1), (4, 3)]], False)
    # Générer tous les chemins possibles à travers le graphe
    print("Liste de tous les chemins passant maximum une fois par sommet :")
    print(generer_parcours(G))
    print()
    print()
    print("Liste des parcours valides : ")
    liste = test_arretes_parcours(G, generer_parcours(G))
    print(liste)
    print()
    print("Tailles des parcours valides")
    for i in range(len(liste)):
        print("{}.".format(i), taille_parcours(G, liste[i]), end=" ; ")
    print()
    print()
    print("Taille maximale d'un parcours valide : ", taille_maximale_parcours_valide(G)[0])
    print("Le parcours numéro :", taille_maximale_parcours_valide(G)[1])

    print()

    print("Le parcours a t-il un chemin de taille 14 sans passer deux fois par le meme sommet ?", decidabilite(G, 14))
    print("Le parcours a t-il un chemin de taille 15 sans passer deux fois par le meme sommet ?", decidabilite(G, 15))

    print("Le parcours le plus grand est : ", calculabilite(G))