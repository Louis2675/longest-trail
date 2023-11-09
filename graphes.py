"""
Fichier contenant la classe graphe pondérée
"""

class Graphe:
    """
    La classe Graphe contient notre graphe non orienté et pondéré
    """
    def __init__(self, couple_gpondere_gnormal):
        """
        Fonction initialisant la classe Graphe et ses attributs
        Entree : Le couple contenant le graphe pondere sous forme de liste et le graphe non pondere sous forme de liste
        """
        self.graphe_pondere = couple_gpondere_gnormal[0]
        self.graphe_simple = couple_gpondere_gnormal[1]
        self.arretes = {}#completer sous forme de dictionnaire (0: 1;2, 3: 4) etc

def generer_graphe_complet(n): G = [[j for j in range(n) if j != i] for i in range(n)]; return G

def generer_graphe_aleatoire(taille=4, densite=0.4):
    """
    Fonction qui génère un graphe aléatoire non orienté et non pondéré
    """
    import random
    G = []
    for i in range(taille):
        G.append([])
    
    for i in range(taille):
        for j in range(i + 1, taille):  
            if random.random() > densite and j != i: # Partie aléatoire (on met l'arrete ou non)
                G[i].append(j)
                G[j].append(i)
    
    return G

    
def generer_graphe_aleatoire_pondere(taille=4, densite=0.4):

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

    return G_pondere, graphe



if __name__ == "__main__":
    print(generer_graphe_aleatoire_pondere(4))