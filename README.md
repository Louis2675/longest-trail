# Le problème du plus long chemin simple (longest-trail)

Trouvez le probleme en détail <a href="https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_la_plus_longue_cha%C3%AEne">ici</a>

Ce projet porte sur des graphes :  <a href="https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_la_plus_longue_cha%C3%AEne">en théorie des graphes</a>

<br>

## Setup

### Lancer vos tests 

<p>Clonez <a href="https://github.com/Louis2675/longest-trail">cette repo GitHub</a> sur votre ordinateur (ou téléchargez les fichiers directement) puis lancez le fichier <code>2048.py</code> pour jouer au jeu.</p>

### Alternatives en cas de problème avec le lancement du jeu

Lancer le fichier via **Powershell** : 

1. Localiser le directoire dans lequel vous avez téléchargé le dossier 
```powershell
cd <votre directoire>
```
2. Une fois que votre terminal est pointé vers le bon dossier utilisez la commande suivante
```powershell
 python -u "<votre directoire>/2048.py"
```

# Informations relatives au projet

## Arborescence du projet

<details>
 <summary>2048-game</summary>
 <br>
 <details>
  <summary>code</summary>
  <ul>
   <li>2048.py
   <li>classement.py
   <li>partie.py
   <li>saisie.py
   <li>pile.py
   <li>grille.py
   <li>parametres.py
   <li>highscores.txt
   <li>last_games.bk
   <li>best_game.omgbk
   <li><details><summary><code>Fichiers facultatifs</code></summary>
          <ul>
            <li>bot2048.py
            <li>pygame2048.py
            <li>pygameButtons.py
          </ul></details>
  </ul>
 </details> 
  <details>
    <summary>Facultatif</summary>
      <ul>
        <li><details><summary>soundtrack</summary>
          <ul>
            <li>fond.mp3
            <li>move.mp3
            <li>objectif.mp3
            <li>perdu.mp3
          </ul>
        </details>
        <li>2048logo.png
      </ul>
  </details>
  <ul>
    <li>Instructions.pdf
    <li>LICENSE
    <li>README.md
  </ul> 
</details>

## Paramètres et librairies utilisés

### <u>Paramètres</u>

#### Code
- `N` : nombre de cases sur une ligne et une colonne (default = 4)
- `MAX` : puissance de 2 de la dernière valeur à atteindre (default = 11)
- `PROBA_4` : % de chance qu'une case 4 apparaisse au lieu d'un 2 (default = 20)
- `APPARITIONS` : nombre de cases qui apparaissent à chaque tour de jeu (default = 1)
- `RETOUR_EN_ARRIERE` : nombre de coups à jouer avant de pouvoir faire 1 retour en arrière (default = 5) 

#### Classement
- `LEADER_MAX` : Ce parametre determine la taille du tableau des meilleurs scores. (default = 10)

#### Bot
- `COUPS_AVANCE` : nombre de coups que le bot intelligent peut voir en avance (default = 3)

#### Pygame
- `MUSIQUE` : détermine si le jeu pygame doit jouer de la musique ou non (default = True)


### <u>Librairies</u>

- `random (.randint et .choice)` : Cette librairie nous permet de determiner un certain hasard pour le placement des cases.
- `keyboard (.is_pressed)` : Cette librairie est utilisée pour determiner la saisie en stream lors du jeu.
- `pygame` : Cette librairie rend le jeu 100 fois meilleur en optimisant l'interface

<br>

## Remerciements

<details>
 <Summary><code>Auteurs du projet</code></summary>
 <ul>
    <li> <a href="https://github.com/Louis2675">Louis Declerck</a>
    <li> <a href="https://github.com/KaiYT1">Kai Tano Bague</a>
 </ul>
</details>