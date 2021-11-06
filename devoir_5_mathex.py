"""
Devoir 5 de maths Expertes
"""

# -----
# On définit ici les fonctions qui nous aideront à résoudre le reste de l'énnoncé

def diviseurs(n):
    """fonction qui renvoie la liste des diviseurs d'un nombre"""
    return [i for i in range(1, n + 1) if n % i == 0]

def est_premier(n):
    """fonction qui teste si un nombre est premier, basée sur son nombre de diviseurs"""
    return len(diviseurs(n)) == 2

# -----

# On trouve la solution de la ligne 5 en testant toutes les possibilités
def ligne_5():
    i = 0  # nombre qui sera mis au carré pour énumérer les carrés parfaits
    carr = str(i**2) # Astuce permettant de lire séparemment les chiffres de i**2
    while len(carr) <= 5:  # Tant que la longueur de carr n'est pas supérieure à 5
        
        # Si la longueur est égale à 5 et que le 3e chiffre est égal à 7 et que le 5e chiffre est égal à 1
        if len(carr) == 5 and carr[2] == "7" and carr[4] == "1":
            
            # Si le produit des chiffres est égal à 756
            if int(carr[0]) * int(carr[1]) * int(carr[2]) * int(carr[3]) * int(carr[4]) == 756:
                
                # On affiche le carré correspondant au critères, sans utiliser de return au cas où il y aurait plusieurs carrés parfaits
                print(carr)
        i += 1  # On incrémente i
        carr = str(i**2)  # On met à jour la valeur de carr avec le nouveau i

ligne_5()

print("-----" * 3)  # On affiche un séparateur entre les fonctions

# On trouve tous les nombres premiers de deux chifres commençant par 2
def colone_d():
    for i in range(100):  # On parcourt les chiffres de 0 à 99
        if i//10 == 2:  # Si le premier chiffre est égal à 2
            if est_premier(i):  # Si i est premier
                print(i)  # On affiche i

colone_d()

print("-----" * 3)  # On affiche un séparateur entre les fonctions

# fonction qui affiche tous les nombres divisibles par 11 de 4 chiffres et
# commençant par le chiffre 6 et finissant par le chiffre 4
def colone_b():
    for i in range(10000):  # On parcourt les chiffres de 0 à 9999
        if i//1000 == 6:  # Si le premier chiffre est égal à 6
            if i % 11 == 0:  # Si le reste de la division par 11 est égal à 0
                if i % 10 == 4:  # Si le dernier chiffre est égal à 4
                    print(i)  # On affiche i

colone_b()

print("-----" * 3)  # On affiche un séparateur entre les fonctions

# fonction qui trouve tous les multiples de 139 de trois chiffres, dont le premier chiffre est 9 et le deuxième est soit 1, soit 7
def multiples_139():
    for i in range(1000):  # On parcourt les chiffres de 0 à 999
        if i//100 == 9:  # Si le premier chiffre est égal à 9
            if i % 10 == 1 or i % 10 == 7:  # Si le deuxième chiffre est égal à 1 ou 7
                if i % 139 == 0:  # Si le reste de la division par 139 est égal à 0
                    print(i)  # On affiche i

multiples_139()

print("-----" * 3)  # On affiche un séparateur entre les fonctions
