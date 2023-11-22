"""
Fichier gerant le lancement du programme.
Permet de choisir entre une excecution avec suivi et sans suivi.
"""

from graphes import Graphe
from calculabilite import calculabilite, calculabilite_suivi
from decidabilite import decidabilite, decidabilite_suivi


# Saisie pour le suivi dans le programme
suivi = ""
while not (suivi in ["oui", "non"]):
    suivi = input("Voulez-vous un suivi du programme ? (oui/non) : ")
    suivi = suivi.lower()


# Un graphe de base 
Graphe_test_base = Graphe([[(3, 2)], [(2, 1), (4, 3)], [(1,1), (4, 4), (3, 5)], [(0, 2), (2, 5)], [(1, 3), (2, 4)]], False)
Graphe_test_second = Graphe([[(1, 5), (2, 9), (4, 1), (6, 9)], [(0, 5), (2, 5), (3, 8), (4, 10), (7, 2), (8, 10)], [(0, 9), (1, 5), (3, 8), (4, 2), (8, 3)], [(1, 8), (2, 8), (6, 4)], [(0, 1), (1, 10), (2, 2), (5, 7)], [(4, 7)], [(0, 9), (3, 4), (7, 4)], [(1, 2), (6, 4), (8, 8)], [(1, 10), (2, 3), (7, 8)]], False)
liste_graphes_generiques = [Graphe_test_base] # Tests : Decidabilite avec le graphe numero 0 : k = 14 : true puis reesayer avec k = 15; Avec le graphe 2, test 65 : true puis reesayer avec 66 : False calculabilite 14 et 65 respectivement pour le 1 et 2


# Quel type de programme : decidabilite, calculabilite ou les deux 
entree = ""
while not (entree in ["d", "b", "c"]):
    entree = input("Désirez-vous le programme en décidabilité (d) ou en calculabilité (c) ou les deux (b) ? ")
    entree = entree.lower()


# Saisie Graphe generique ou aleatoire
entree_graphe = ""
while not (entree_graphe in ["oui", "non"]):
    entree_graphe = input("Voulez-vous un graphe générique ? (oui/non) : ")
    entree_graphe = entree_graphe.lower()

if entree_graphe == "oui":
    num_graphe = -1
    while not (0 <= num_graphe <= len(liste_graphes_generiques)):
        # Numero du graphe generique
        num_graphe = input("Donnez le numéro du graphe générique que vous voulez utiliser : (de 0 à {}) : ".format(len(liste_graphes_generiques) -1))
        try:
            num_graphe = int(num_graphe)
        except ValueError:
            print("Veuillez entrer un nombre entier.")
            num_graphe = -1
    Graphe = liste_graphes_generiques[num_graphe]

else: # sinon on genere un graphe aleatoire
    Graphe = Graphe([], True)

print("Votre graphe est : {}".format(Graphe.graphe))

if entree == "d" or entree == "b": # si entree d ou b on commence decidabilite
    print("On commence la decidabilite...")
    # on demande la taille minimale du chemin
    try:
        k = int(input("Entrez la taille minimale du chemin : "))
    except ValueError:
        print("Veuillez entrer un nombre entier.")
        k = int(input("Entrez la taille minimale du chemin : "))
    
    # Sasie pour les tests de 0 a k
    test_all = ""
    while not(test_all in ["oui", "non"]):
        test_all = input("Voulez-vous tester toutes les tailles de 0 a k ? (oui/non) : ")
        test_all = test_all.lower()

    if test_all == "oui" and suivi == "oui":
        for i in range(k+1):
            print("k = {} : {}".format(i, decidabilite_suivi(Graphe, i)))
        
    elif test_all == "oui" and suivi == "non":
        for i in range(k+1):
            print("k = {} : {}".format(i, decidabilite(Graphe, i)))

    elif test_all == "non" and suivi == "oui":
        print("k = {} : {}".format(k, decidabilite_suivi(Graphe, k)))

    else:
        print("k = {} : {}".format(k, decidabilite(Graphe, k)))

# On commence la calculabilite avec suivi ou non
if suivi == "oui":
    if entree == "c" or entree == "b":
        print("on commence la calculabilite...")
        print("Le parcours le plus grand sans passer deux fois par le meme sommet est :", calculabilite_suivi(Graphe)[0], "; max_len =", calculabilite(Graphe)[1])
else:
    if entree == "c" or entree == "b":
        print("on commence la calculabilite...")
        print("Le parcours le plus grand sans passer deux fois par le meme sommet est :", calculabilite(Graphe)[0], "; max_len =", calculabilite(Graphe)[1])