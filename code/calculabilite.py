"""
Fichier contenant les fonctions de resolution de la calculabilite du probleme du plus long chemin simple
"""

from fonctions import *


def calculabilite(graphe):
    """
    Calcule le plus grand chemin et sa taille dans le graphe.

    Entrée:
        graphe (Graphe): Le graphe à évaluer.

    Sortie:
        tuple: Un tuple contenant le plus grand chemin et sa taille.
    """
    return (taille_maximale_parcours_valide(graphe)[2], taille_maximale_parcours_valide(graphe)[0]) # on retourne le plus grand chemin et sa taille


def calculabilite_suivi(graphe):
    """
    Calcule le plus grand chemin et sa taille dans le graphe avec suivi.

    Entrée:
        graphe (Graphe): Le graphe à évaluer.

    Sortie:
        tuple: Un tuple contenant le plus grand chemin et sa taille.
    """
    return (taille_maximale_parcours_valide_suivi(graphe)[2], taille_maximale_parcours_valide(graphe)[0]) # on retourne le plus grand chemin et sa taille
