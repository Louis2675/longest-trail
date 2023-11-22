"""
Fichier contenant les fonctions de resolution de la calculabilite du probleme du plus long chemin simple
"""


from fonctions import *


def decidabilite(graphe, k):
    """
    Détermine si le graphe possiblement de longueur > k pour le plus grand parcours
    Entrée:
        graphe (Graphe): Le graphe a tester
        k (int): La taille testee.
    Sortie:
        bool: True si le graphe est possiblement plus grand; False sinon
    """
    if taille_maximale_parcours_valide(graphe)[0] >= k: # si la taille max du chemin > k
        return True
    return False


def decidabilite_suivi(graphe, k):
    """
    Donne le plus grand parcours et sa taille k avec suivi
    Entrée:
        graphe (Graphe): Le graphe a tester
        k (int): La taille testee.
    Sortie:
        le + grand parcours
    """
    if taille_maximale_parcours_valide_suivi(graphe)[0] >= k: # si la taille max du chemin > k
        print("La taille du plus grand parcours est plus grande que {} alors True".format(k))
        return True
    print("La taille du parcours le plus grand est inferieur a {}".format(k))
    return False
