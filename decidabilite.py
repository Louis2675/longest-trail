from graphes import Graphe

def permutations(liste):
    """
    Génère toutes les permutations d'une liste donnée.
    Entrée:
        liste (list): La liste à permuter.
    Sortie:
        list: Une liste de toutes les permutations possibles de la liste d'entrée.
    """
    # Si la liste d'entrée ne contient qu'un seul élément, retourner cette liste
    if len(liste) == 1:
        return [liste]
    else:
        result = []
        # Pour chaque élément dans la liste d'entrée
        for i in range(len(liste)):
            # Retirer l'élément actuel de la liste
            remaining_elements = liste[:i] + liste[i+1:]
            # Générer toutes les permutations des éléments restants
            for perm in permutations(remaining_elements):
                # Ajouter l'élément actuel à chaque permutation générée
                result.append([liste[i]] + perm)
        # Retourner la liste de toutes les permutations possibles
        return result
    

def generer_parcours(graphe):
    """
    Génère tous les chemins possibles à travers un graphe.
    Entrée:
        graphe (Graphe): Le graphe à parcourir.
    Sortie:
        list: Une liste de toutes les permutations possibles des sommets du graphe.
    """
    # Créer une liste de tous les sommets du graphe
    sommets = [i for i in range(graphe.taille)]
    # Créer une liste vide pour stocker tous les chemins possibles
    liste_parcours = []
    # Pour chaque sommet dans le graphe
    for i in range(graphe.taille):
        # Générer toutes les permutations des premiers i+1 sommets
        liste_parcours.append(permutations(sommets[:i+1]))
    # Retourner la liste de tous les chemins possibles
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

def reducion_taille(graphe, liste_parcours):
    """
    Permet de retirer
    """

def decidabilite_brute(graphe, longueur_cible):
    """
    Détermine si un chemin de longueur au moins longueur_cible existe dans le graphe.
    Entrée:
        graphe (Graphe): Le graphe à parcourir.
        longueur_cible (int): La longueur minimale du chemin recherché.
    Sortie:
        bool: True si un chemin de longueur au moins longueur_cible existe, False sinon.
    """
    # TODO: implémenter la fonction de décision de manière brute


if __name__ == "__main__":
    # Créer un graphe à partir d'une liste d'adjacence pondérée
    G = Graphe([[(5, 2)], [(2, 1), (4, 3)], [(1,1), (4, 4), (3, 5)], [(0, 2), (2, 5)], [(1, 3), (2, 4)]], False)
    # Générer tous les chemins possibles à travers le graphe

    print(arrete_existe(G, 0, 1))
    print(generer_parcours(G))
    print()
    print()
    print("Liste des parcours valides : ")
    print(test_arretes_parcours(G, generer_parcours(G)))