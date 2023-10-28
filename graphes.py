"""
Fichier contenant la classe Graphe, utilisée pour le projet.
"""

class Graphe:
    def __init__(self, A, S):
        self.sommets = S
        self.arcs = A

    def matrice_adjacence(self):
        n = len(self.sommets)
        M = [[0 for _ in range(n)] for _ in range(n)]
        for (i, j) in self.arcs:
            M[i][j] = 1
        return M

    def convertir_indexe_sommet(self, S):
        n = len(self.sommets)
        for i in range(n):
            self.sommets[i] = chr(65 + i)
        return None

    def tableau_adjanence(self):
        n = len(self.sommets)
        T = [[] for _ in range(n)]
        for (i, j) in self.arcs:
            T[i].append(j)
        return T

    def dictionnaire_adjancence(self):
        n = len(self.sommets)
        D = {}
        for i in range(n):
            D[i] = []
        for (i, j) in self.arcs:
            D[i].append(j)
        return D

    def parcours_largeur_graphe(self, sommet_depart=0):
        n = len(self.sommets)
        parcours = []
        file = [sommet_depart]
        while file:
            sommet = file.pop(0)
            if sommet not in parcours:
                parcours.append(sommet)
                for voisin in self.dictionnaire_adjancence()[sommet]:
                    file.append(voisin)
        return parcours

    def parcours_profondeur_graphe(self, sommet_depart=0):
        n = len(self.sommets)
        parcours = []
        pile = [sommet_depart]
        while pile:
            sommet = pile.pop()
            if sommet not in parcours:
                parcours.append(sommet)
                for voisin in self.dictionnaire_adjancence()[sommet]:
                    pile.append(voisin)
        return parcours

def generer_graphe_aleatoire(n):
    import random; G = [[j for j in range(n) if j != i and random.random() < 0.5] for i in range(n)]; return G


def generer_graphe_complet(n): 
    G = [[j for j in range(n) if j != i] for i in range(n)]; return G