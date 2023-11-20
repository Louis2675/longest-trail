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
        if random:
            if len_graphe == 0:
                try:
                    len_graphe = int(input("Entrez la taille du graphe : "))
                except ValueError:
                    print("Veuillez entrer un nombre entier.")
                    len_graphe = int(input("Entrez la taille du graphe : "))
                try:
                    densite = float(input("Entrez la densité du graphe : "))
                except ValueError:
                    print("Veuillez entrer un nombre entre 0 et 1 (plus le nombre est proche de 0 moins de chance d'avoir des arêtes) : ")
                    densite = float(input("Entrez la densité du graphe : "))
            self.graphe = generer_graphe_aleatoire_pondere(len_graphe, densite)
            self.taille = len_graphe
        else:
            self.graphe = graphe
            self.taille = len(graphe)

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
            if random.random() <= densite and j != i: # Partie aléatoire (on met l'arrete ou non)
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

    return G_pondere



if __name__ == "__main__":
    print(generer_graphe_aleatoire_pondere(4))