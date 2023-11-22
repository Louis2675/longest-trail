"""
Fichier contenant la classe graphe pondérée
"""

class Graphe:
    """
    La classe Graphe contient notre graphe non orienté et pondéré
    """
    def __init__(self, graphe=[], random=True, len_graphe=0):
        """
        Fonction initialisant la classe Graphe et ses attributs
        Entree : Le couple contenant le graphe pondere sous forme de liste et le graphe non pondere sous forme de liste
        """
        if random: # si on veut un graphe aleatoire
            if len_graphe == 0:
                # Saisie pour la taille du graphe
                len_graphe = -1
                while len_graphe == -1:
                    try:
                        len_graphe = input("Entrez la taille du graphe : ")
                        len_graphe = int(len_graphe)
                    except ValueError:
                        print("Veuillez entrer un nombre entier.")
                        len_graphe = -1 
                # Saisie pour la densite du graphe
                densite = -1
                while densite == -1 or densite < 0 or densite > 1:
                    try:
                        densite = input("Entrez la densité du graphe : ")
                        densite = float(densite)
                    except ValueError:
                        print("Veuillez entrer un nombre entre 0 et 1 (plus le nombre est proche de 0 moins de chance d'avoir des arêtes) : ")
                        densite = -1
            self.graphe = generer_graphe_aleatoire_pondere(len_graphe, densite) # On genere donc ensuite le graphe avec les infos recueillies
            self.taille = len_graphe # on initialise la taille
        else:
            self.graphe = graphe # on prend le graphe en entree 
            self.taille = len(graphe) # et sa taille

def generer_graphe_aleatoire(taille=4, densite=0.4):
    """
    Génère un graphe aléatoire non orienté et non pondéré.

    Entrée:
        taille (int): Le nombre de sommets du graphe (par défaut 4).
        densite (float): La densité de l'arête entre deux sommets (par défaut 0.4).

    Sortie:
        list: Le graphe aléatoire généré sous forme de liste d'adjacence.
    """
    import random
    G = [] # le graphe en liste
    for i in range(taille):
        G.append([])
    
    for i in range(taille): # pour tous les sommets
        for j in range(i + 1, taille):  
            if random.random() <= densite and j != i: # Partie aléatoire (on met l'arrete ou non)
                G[i].append(j) # On met l'arrete dans les deux sens car non oriente
                G[j].append(i) # On met l'arrete dans les deux sens car non oriente
    
    return G

    
def generer_graphe_aleatoire_pondere(taille=4, densite=0.4):
    """
    Génère un graphe aléatoire non orienté et pondéré.

    Entrée:
        taille (int): Le nombre de sommets du graphe (par défaut 4).
        densite (float): La densité de l'arête entre deux sommets (par défaut 0.4).

    Sortie:
        list: Le graphe aléatoire pondéré généré sous forme de liste d'adjacence.
    """
    import random

    graphe = generer_graphe_aleatoire(taille, densite) # On recupere un graphe aleatoire
    G_pondere = []
    poids = {}  # Dictionnaire pour stocker les poids des arêtes déjà générés

    for i in range(len(graphe)):
        G_pondere.append([])
        for j in graphe[i]:
            if (i, j) not in poids and (j, i) not in poids:  # Si le poids de l'arête n'a pas encore été généré
                poids[(i, j)] = poids[(j, i)] = random.randint(1, 10)  # Générer un poids aléatoire
            G_pondere[i].append((j, poids[(i, j)]))  # Ajouter l'arête pondérée au graphe

    return G_pondere

