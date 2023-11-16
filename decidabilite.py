from graphes import Graphe

def permutations(input_list):
    if len(input_list) == 0:
        return []
    elif len(input_list) == 1:
        return [input_list]
    else:
        result = []
        for i in range(len(input_list)):
            remaining_elements = input_list[:i] + input_list[i+1:]
            for perm in permutations(remaining_elements):
                result.append([input_list[i]] + perm)
        return result

def generer_combinaisons(input_list):
    if len(input_list) == 0:
        return [[]]
    else:
        result = []
        for comb in generer_combinaisons(input_list[1:]):
            result += [comb, [input_list[0]] + comb]
        return result
    
def decidabilite_brute(graphe, longueur_cible):
    """
    Entrée : graphe un graphe non orienté et pondéré et longueur_cible un nombre entier
    Sortie : existe-t-il un chemin de longueur au moins longueur_cible ne passant pas deux fois par un même sommet ?
    """

if __name__ == "__main__":
    G = Graphe([[(5, 2)], [(2, 1), (4, 3)], [(1,1), (4, 4), (3, 5)], [(0, 2), (2, 5)], [(1, 3), (2, 4)]], False)
    print(permutations([1,2,3,4,5]))    
