#Écrire  un programme Python  qui permet  d’afficher le message Bonjour.
def afficher():
    print("Bonjour")

#Écrire  un programme Python permettant de saisir deux nombres et d'afficher leur produit.  
def afficher_nombre():
    x = input("nombre 1 : ")
    y = input("nombre 2 : ")
    print("resultat", x,"*", y, "=", int(x) * int(y))

#Écrire  un programme Python  qui  permet d'échanger le contenu de deux entiers  A et B  saisis par l'utilisateur. et afficher ces entiers  après l’échange.
def echanger_contenu():
    A = input("Inserer le nombre A : ")
    B = input("Inserer le nombre B : ")
    print("Valeur avant echange, A :", A,"et B : ", B)
    TEMP = A 
    A = B 
    B = TEMP 
    print("Valeur après echange, A :", A,"et B : ", B)

#Écrire un un programme Python qui  permet d'afficher si un nombre  entier saisi au  clavier est pair ou impair.
def paire_impaire():
    nombre = input("Entrer le nombre : ")
    if int(nombre) % 2 == 0:
        print("Le nombre", nombre, "est paire")
    else:
        print("Le nombre", nombre, "est impaire")

#Écrire un programme Python  qui permet d'afficher le plus grand de trois entiers saisis  au clavier. 
def plus_grand():
    x = input("nombre 1 : ")
    y = input("nombre 2 : ")
    z = input("nombre 3 : ")
    if int(x) > int(y) & int(x) > int(z):
        print(x, "est le plus grand nombre entre : ",x,y,z)
    elif int(y) > int(x) & int(y) > int(z):
        print(x, "est le plus grand nombre entre : ",x,y,z)
    else:
        print(z, "est le plus grand nombre entre : ",x,y,z)

"""Execution des codes"""
print("---------------/ Excecution des code /----------------")
plus_grand()