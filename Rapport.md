# Rapport de projet - longest trail

Rapport sur le problème du plus long chemin simple


> _**Version problème de décidabilité :**
Problème : Chemin de longueur minorée
Entrée : G un graphe non orienté et pondéré et k un nombre entier
Sortie : existe-t-il un chemin de longueur au moins k ne passant pas deux fois par un même sommet ?_
>
>_**Version problème de calculabilité :**
Problème : Plus long chemin simple
Entrée : G un graphe non orienté et pondéré
Sortie : le plus long chemin ne passant pas deux fois par un même sommet*_


# Introduction


Le problème du plus long chemin simple contient deux versions différentes : **la calculabilité et la décidabilité.** Ces deux versions prennent place au sein de structures de données de type graphe.

- La calculabilité demande le plus long chemin ne passant pas deux fois par un même sommet.
- La décidabilité demande s’il existe un chemin de longueur au moins k ne passant pas deux fois par un même sommet

Ce projet utilise la recherche exhaustive ou par force brute *(méthode algorithmique qui consiste principalement à essayer toutes les solutions possibles)*. Par exemple pour trouver le maximum d'un certain ensemble de valeurs, on consulte toutes les valeurs.

# Résolution du problème

## Présentation du problème de décidabilité

_La décidabilité demande s’il existe un chemin de longueur au moins k ne passant pas deux fois par un même sommet_

La résolution du problème de décidabilité se fait en plusieurs étapes : 

1. <u>On commence par prendre un graphe pondéré et non orienté.</u>

Pour ce faire, on utilise la `classe Graphe` initialisée dans le fichier graphes.py. Dans cette classe, nous avons initialisé deux possibilités de graphe : un graphe donné par l'utilisateur en entrée pour l'objet et un graphe généré aléatoirement (c'est le parametre random de la fonction `__init__`).

2. <u>On génère toutes les chemins possibles avec les sommets du Graphe en entrée.</u>

