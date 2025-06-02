# 1- Écrire un programme Python qui permet d’afficher le message Bonjour.
def afficher():
    print("Bonjour")


# 2- Écrire un programme Python permettant de saisir deux nombres et d'afficher leur produit.
def afficher_nombre():
    x = input("nombre 1 : ")
    y = input("nombre 2 : ")
    print("resultat", x, "*", y, "=", int(x) * int(y))


# 3- Écrire un programme Python qui permet d'échanger le contenu de deux entiers A et B saisis par l'utilisateur. Et afficher ces entiers après l’échange.
def echanger_contenu():
    a = input("Inserer le nombre A : ")
    b = input("Inserer le nombre B : ")
    print("Valeur avant echange, A :", a, "et B : ", b)
    temp = a
    a = b
    b = temp
    print("Valeur après echange, A :", a, "et B : ", b)


# 4- Écrire un programme Python qui permet d'afficher si un nombre entier saisi au clavier est pair ou impair.
def paire_impaire():
    nombre = input("Entrer le nombre : ")
    if int(nombre) % 2 == 0:
        print("Le nombre", nombre, "est pair")
    else:
        print("Le nombre", nombre, "est impair")


# 5- Écrire un programme Python qui permet d'afficher le plus grand de trois entiers saisis au clavier.
def plus_grand():
    x = int(input("nombre 1 : "))
    y = int(input("nombre 2 : "))
    z = int(input("nombre 3 : "))
    if x > y and x > z:
        print(x, "est le plus grand nombre entre : ", x, y, z)
    elif y > z:
        print(x, "est le plus grand nombre entre : ", x, y, z)
    else:
        print(z, "est le plus grand nombre entre : ", x, y, z)


# 6- Écrire un programme Python qui permet d'évaluer une note saisie au clavier
# (si la note est supérieur à 10 alors, il affiche validé sinon non validé (NB : la note comprise entre 0 et 20).
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
    n = int(input("nombre n : "))
    m = int(input("nombre m : "))
    produit = n * m
    if produit > 0:
        print("Le produit de ", n, "et", m, "est positif")
    elif produit == 0:
        print("Le produit de ", n, "et", m, "est null")
    else:
        print("Le produit de ", n, "et", m, "est negatif")


# 8- Écrire un programme Python qui permet de calculer la valeur absolue d'un entier saisi par l'utilisateur.
def valeur_absolut():
    val = int(input("Entrer le nombre : "))
    if val < 0:
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
# Écrire un programme Python permettant de saisir le prix total HT et de calculer le montant TTC en prenant en compte la réduction et la TVA=20%. *
def calcul_reduction_ttc():
    ht = float(input("Prix total HT : "))
    if ht > 200:
        ht = ht * 0.85
    ttc = ht * 1.20
    print("Montant TTC à payer :", round(ttc, 2))


# 11- Écrire un programme Python qui permet d'afficher le message "Bonsoir" 10 fois. Utilisant la boucle while.
def afficher_boucle():
    i = 1
    while i <= 10:
        print("Bonjour", i, "fois")
        i += 1


# 12 - Écrire un programme Python permettant de calculer la somme S= 1+2+3+... + 10. Utilisant la boucle while.
def calcule_somme():
    s = 0
    i = 1

    while i <= 10:
        s += i
        if i < 10:
            print(i, end=" + ")
        else:
            print(i, end=" = ")
        i += 1
    print(s)


# 13 - Écrire un programme Python permettant de calculer la somme S=1+2+3+... + N, où N saisi par l’utilisateur. Utilisant la boucle while.
def calcule_somme_n():
    n = int(input("Entrer le nombre de somme : "))
    s = 0
    i = 1
    print("S(", n, ") : ", end="")
    while i <= n:
        s += i
        if i < n:
            print(i, end=" + ")
        else:
            print(i, end=" = ")
        i += 1
    print(s)


#  14 - Écrire un programme Python qui permet d'afficher le message "bonjour" 10 fois. Utilisant la boucle for.
def afficher_bonjour_for():
    for i in range(1, 11):
        print("Bonjour", i, "fois")


# 15 - Écrire un programme Python qui permet de calculer la somme S=1+2+3+4+….+ N. où N saisi au clavier par l'utilisateur. Utilisant la boucle for.
def calcule_somme_n2():
    n = int(input("Entrer le nombre : "))
    s = 0
    print("S(", n, ") : ", end="")
    for i in range(1, n + 1):
        s += i
        if i < n:
            print(i, end=" + ")
        else:
            print(i, end=" = ")
        i += 1
    print(s)


# 16 - Écrire un programme Python qui permet d'afficher la table de multiplication de 5. Utilisant la boucle For.
def table_multiplication():
    table = int(input("Entrer la table multiplication : "))
    n = int(input("Entrer le nombre de table : "))
    for i in range(n + 1):
        print(i, "x", table, "=", i * table)


# 17 - Écrivez un programme Python, entrez deux nombres de l'utilisateur et trouvez le plus grand diviseur commun en utilisant la boucle for.
def plus_grand_diviseur():
    a = int(input("Entrez le premier nombre : "))
    b = int(input("Entrez le deuxième nombre : "))

    min_ab = min(a, b)
    pgcd = 1

    for i in range(1, min_ab + 1):
        if a % i == 0 and b % i == 0:
            pgcd = i
    print("Le plus grand diviseur commun est :", pgcd)


# 18 - Programe qui sert a convertir des degrers Celsius en degrés frhrenheit
def conversion():
    try:
        degrer_celsieus = int(input("Entrer un nombre : "))
        degrer_fahrence = int(degrer_celsieus * (9 / 5) + 32)
        print(f"{degrer_celsieus} c = {degrer_fahrence} f")
    except ValueError:
        print("Données en entrées non-conrrectes")


# 19 - programme qui retourne la chaine de caractères passée en argument à l'envers
def reverse(texte):
    print(texte[::-1])


# 20 - programme qui retourne le nombre de voyelles dans une chaine de caracteres
def get_value_is_number(text):
    voyelle = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in text.lower():
        if char in voyelle:
            count += 1
    print(f"le nombre de voyelle est : {count}")


# 21 - programme qui retourne l'abreviation d'un nom et prénom : ex John Doe = John D.
def abreviation(texte):
    liste = texte.split()
    print(f"{liste[0]} {liste[1][0].upper()}.")


# 22 - Programme qui retourne chaque chiffre que contient le nombre passé en argurment au carré et concaténez-les. Puis retournez le nombre concatené final
def square_digits(num):
    result = ""
    number = str(num)
    for i in number:
        result += str((int(i) ** 2))
    print(result)

"""Execution des codes"""
print("---------------/ Excecution des code /----------------")

square_digits(5225)
