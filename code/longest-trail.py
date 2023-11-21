"""
Fichier gerant le lancement du programme.
Permet de choisir entre une excecution avec suivi et sans suivi.
"""

from graphes import Graphe
from fonctions import calculabilite, decidabilite, decidabilite_suivi, calculabilite_suivi

suivi = ""
while not (suivi in ["oui", "non"]):
    suivi = input("Voulez-vous un suivi du programme ? (oui/non) : ")
    suivi = suivi.lower()

Graphe_test_base = Graphe([[(3, 2)], [(2, 1), (4, 3)], [(1,1), (4, 4), (3, 5)], [(0, 2), (2, 5)], [(1, 3), (2, 4)]], False)
liste_graphes_generiques = [Graphe_test_base]

entree = ""
while not (entree in ["d", "b", "c"]):
    entree = input("Désirez-vous le programme en décidabilité (d) ou en calculabilité (c) ou les deux (b) ? ")
    entree = entree.lower()

entree_graphe = ""
while not (entree_graphe in ["oui", "non"]):
    entree_graphe = input("Voulez-vous un graphe générique ? (oui/non) : ")
    entree_graphe = entree_graphe.lower()

if entree_graphe == "oui":
    num_graphe = -1
    while not (0 <= num_graphe <= len(liste_graphes_generiques)):
        try:
            num_graphe = int(input("Donnez le numéro du graphe générique que vous voulez utiliser : (de 0 à {}) : ".format(len(liste_graphes_generiques) -1)))
        except ValueError:
            print("Veuillez entrer un nombre entier.")
            num_graphe = int(input("Donnez le numéro du graphe générique que vous voulez utiliser : (de 0 à {}) : ".format(len(liste_graphes_generiques))))
    Graphe = liste_graphes_generiques[num_graphe]

else:
    Graphe = Graphe([], True)

print("Votre graphe est : {}".format(Graphe.graphe))

if entree == "d" or entree == "b":
    print("On commence la decidabilite...")
    try:
        k = int(input("Entrez la taille minimale du chemin : "))
    except ValueError:
        print("Veuillez entrer un nombre entier.")
        k = int(input("Entrez la taille minimale du chemin : "))
    
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

if suivi == "oui":
    if entree == "c" or entree == "b":
        print("on commence la calculabilite...")
        print("Le parcours le plus grand sans passer deux fois par le meme sommet est :", calculabilite_suivi(Graphe)[0], "; max_len =", calculabilite(Graphe)[1])
else:
    if entree == "c" or entree == "b":
        print("on commence la calculabilite...")
        print("Le parcours le plus grand sans passer deux fois par le meme sommet est :", calculabilite(Graphe)[0], "; max_len =", calculabilite(Graphe)[1])