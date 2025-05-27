# 1- Écrire  un programme Python  qui permet  d’afficher le message Bonjour.
def afficher():
    print("Bonjour")

# 2- Écrire  un programme Python permettant de saisir deux nombres et d'afficher leur produit.  
def afficher_nombre():
    x = input("nombre 1 : ")
    y = input("nombre 2 : ")
    print("resultat", x,"*", y, "=", int(x) * int(y))

# 3- Écrire  un programme Python  qui  permet d'échanger le contenu de deux entiers  A et B  saisis par l'utilisateur. et afficher ces entiers  après l’échange.
def echanger_contenu():
    A = input("Inserer le nombre A : ")
    B = input("Inserer le nombre B : ")
    print("Valeur avant echange, A :", A,"et B : ", B)
    TEMP = A 
    A = B 
    B = TEMP 
    print("Valeur après echange, A :", A,"et B : ", B)

# 4- Écrire un un programme Python qui  permet d'afficher si un nombre  entier saisi au  clavier est pair ou impair.
def paire_impaire():
    nombre = input("Entrer le nombre : ")
    if int(nombre) % 2 == 0:
        print("Le nombre", nombre, "est pair")
    else:
        print("Le nombre", nombre, "est impair")

# 5- Écrire un programme Python  qui permet d'afficher le plus grand de trois entiers saisis  au clavier. 
def plus_grand():
    x = input("nombre 1 : ")
    y = input("nombre 2 : ")
    z = input("nombre 3 : ")
    if int(x) > int(y) and int(x) > int(z):
        print(x, "est le plus grand nombre entre : ",x,y,z)
    elif int(y) > int(z):
        print(x, "est le plus grand nombre entre : ",x,y,z)
    else:
        print(z, "est le plus grand nombre entre : ",x,y,z)

# 6- Écrire un programme Python  qui permet d'évaluer une note saisi au  clavier   
#(si la note est supérieur à 10 alors il affiche validé sinon non validé  (NB : la note comprise entre 0 et 20 ). 
def afficher_valide():
    note = input("Entrer la note : ")
    if 0 <= int(note) <= 20:
        if int(note) > 10:
            print("Validé")
        else:
            print("Non validé")
    else:
        print("la note doit être comprise entre 0 et 20")
        afficher_valide()

# 7- Écrire un programme Python qui demande deux nombres m et n à l’utilisateur et l’informe ensuite si le produit de ces deux nombres est positif ou négatif.
# On inclut dans le programme le cas où le produit peut être nul. 
def produit_nombre():
    n = input("nombre n : ")
    m = input("nombre m : ")
    produit = int(n) * int(m)
    if produit > 0:
        print("Le produit de ", n, "et",m, "est positif")
    elif produit == 0:
        print("Le produit de ", n, "et",m, "est null")
    else:
        print("Le produit de ", n, "et",m, "est negatif")


# 8- Écrire un programme Python qui permet de calculer la valeur absolue d'un entier saisi  par l'utilisateur.
def valeur_absolut():
    val = int(input("Entrer le nombre : "))
    if val < 0 :
        absolu = -val
    else:
        absolu = val
    print(absolu)

# 9- Écrire un programme Python qui permet de calculer la moyenne de trois entiers saisis par l'utilisateur.
def moyenne():
    val_1 = int(input("valeur 1 : "))
    val_2 = int(input("valeur 2 : "))
    val_3 = int(input("valeur 3 : "))
    somme = val_1 + val_2 + val_3
    moyen = somme // 3
    print(moyen)

# 10- Une boutique propose à ces clients, une réduction de 15% pour les montants d’achat supérieurs à 200 dh.
# Écrire un programme Python permettant de saisir le prix total HT et de calculer le  montant TTC en prenant en compte la réduction et la TVA=20%. *
def calcul_reduction_ttc():
    ht = float(input("Prix total HT : "))
    if ht > 200:
        ht = ht * 0.85
    ttc = ht * 1.20 
    print("Montant TTC à payer :", round(ttc, 2))


"""Execution des codes"""
print("---------------/ Excecution des code /----------------")
