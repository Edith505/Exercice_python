import math


# Exercice 1 : Programme qui demande le nom et l'âge et l'afficher
def demande_nom_age():
    nom = input("Entrer votre nom : ")
    age = int(input("Entrer votre age : "))
    print("Bonjour", nom, ", tu as", age)


# Exercice 2 : Programme qui affiche l'age d'une personne à partir de son année de naissance
def affiche_age():
    anne = int(input("Entrer votre année de naissance : "))
    age = 2025 - anne
    print("Vous avez", age, "ans")


# Exercice 3 : Programe qui calcule le périmètre et la surface d'un rectangle
def calcule_permietre_surface(longeur, largeur):
    perimetre = 2 * (longeur + largeur)
    surface = longeur * largeur
    print("le perimetre = ", perimetre, "et le surface = ", surface)


# Exercice 4 : Programme qui calcule et affiche la puissance de x par y
def puissance(x, y):
    p = x ** y
    print(x, "^", y, ":", p)


# Exercice 5 : Programme opérations, somme, produit, soustraction et la division
def operation(x, y):
    somme = x + y
    produit = x * y
    soustraction = x - y
    division = 0
    try:
        division = x / y
    except ValueError:
        print("erreur, on ne peut pas diviser par 0")
    finally:
        print("somme =", somme, ",produit =", produit, ",soustraction =", soustraction, ",division =",
              format(division, ".2f"))


# Exercice 6 : Programme qui calcule et affiche la moyenne de 5 notes
def calcul_moyenne(note1, note2, note3, note4, note5):
    somme = note1 + note2 + note3 + note4 + note5
    moyenne = somme / 5
    print("moyenne =", moyenne)


# Exercice 7 : Programme qui echoge le contenu des deux variables
def echange(x, y):
    print("Avant echange, x :", x, "et y :", y)
    temp = x
    x = y
    y = temp
    print("Avant echange, x :", x, "et y :", y)


# Exercice 8 : Programme qui calcule et affiche le volume d'une sphère
def sphere(rayon):
    volume = (4 * math.pi * rayon ** 3) / 3
    print("volume =", format(volume, ".2f"))


# Exercice 9 : Programme qui convertie la durée en heures, minutes et secondes
def calcule_temps(t):
    h = t // 3600
    m = (t % 3600) // 60
    s = (t % 3600) % 60
    print("temps =", h, "h ", m, "m ", s, "s.")


# Exercice 10 : Programme qui calcule la distance entre deux points A et B du plan
def distance_point():
    xa = int(input("Entrer le coordonnée de xa : "))
    ya = int(input("Entrer le coordonnée de ya : "))
    print("A(", xa, ",", ya, ")")
    xb = int(input("Entrer le coordonnée de xb : "))
    yb = int(input("Entrer le coordonnée de yb : "))
    print("B(", xb, ",", yb, ")")
    distance = math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)
    print("distance =", format(distance, ".2f"))


# Exercice 11 : calcule de 3 resistances en serie et en parallele
def resistance():
    r1 = int(input("Entrer la resistance R1 : "))
    r2 = int(input("Entrer la resistance R2 : "))
    r3 = int(input("Entrer la resistance R3 : "))
    resistance_serie = r1 + r2 + r3
    resistance_parallele = 1 / (1 / r1 + 1 / r2 + 1 / r3)
    question = input("en serie ou parallèle? (Tapez s ou p) : ")
    if question == "s":
        print("Resistance  = ", resistance_serie)
    elif question == "p":
        print("Resistance  = ", format(resistance_parallele, ".2f"))


# Exercice 12 : Programme qui retourne si deux nombres ont le meme signe ou nom
def meme_signe(x, y):
    if not x * y > 0:
        print(x, "et", y, "sont deux signes differents")
    else:
        print(x, "et", y, "sont de même signe")


# Exercice 13 : Programme qui change contenues de deux variables selon une condition
def changer_contenu(x, y):
    a = x
    b = y
    print("Avant X :", x, "et Y :", y)
    if x * y > 0:
        temp = x
        x = y
        y = temp
    else:
        x = a + b
        y = a * b
    print("Après X :", x, "et Y :", y)


# Exercice 14 : nombre de photocopies et le prix : 0.30 centime les 10 premiers, 0.25 les 20 suivants et 0.20 au-delà
def prix_photocopie():
    while True:
        nombre_photocopie = int(input("Entrer le nombre de photocopies : "))
        if nombre_photocopie <= 0:
            print("Le nombre de photocopies doit être supérieur à 0.")
        else:
            break

    if nombre_photocopie <= 10:
        prix_final = nombre_photocopie * 0.30
    elif nombre_photocopie <= 30:
        prix_final = (10 * 0.30) + ((nombre_photocopie - 10) * 0.25)
    else:
        prix_final = (10 * 0.30) + (20 * 0.25) + ((nombre_photocopie - 30) * 0.20)

    print("Le prix total de photocopies = ", format(prix_final, ".2f"))


# Exercice 15 : Programme qui demande age d'un enfant et affiche le categorie
def demande_age():
    while True:
        age = int(input("Entrer votre age : "))
        if age < 6 or age > 16:
            print("L'age doit être comprie entre a 0 et 16")
        else:
            break

    if age < 8:
        categorie = "Poussins"
    elif age < 10:
        categorie = "Pupille"
    elif age < 12:
        categorie = "Minime"
    else:
        categorie = "Cadete"
    print("votre categorie est", categorie)


# Exercice 16 : Programme qui affiche la moyenne et la mention des notes (5 notes)
def affiche_moyen():
    tableau_note = []

    while len(tableau_note) < 5:
        try:
            note = int(input(f"Entrez la note {len(tableau_note) + 1} : "))
            if 0 <= note <= 20:
                tableau_note.append(note)
            else:
                print("La note doit être entre 0 et 20.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

    moyen = sum(tableau_note) / len(tableau_note)

    print("Moyenne =", format(moyen, ".2f"))

    if moyen < 10:
        mention = "Insuffisant"
    elif moyen == 10:
        mention = "Juste"
    elif moyen < 12:
        mention = "Passable"
    elif moyen < 14:
        mention = "Assez bien"
    elif moyen < 17:
        mention = "Bien"
    else:
        mention = "Très bien"

    print("Mention =", mention)


# Exercice 17 : Programme qui afficher les élements impaire et paire d'une liste
def liste_paire_impaire():
    liste_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    liste_impaire = []
    liste_paire = []

    for i in liste_original:
        if i % 2 == 0:
            liste_paire.append(i)
        else:
            liste_impaire.append(i)
    print(liste_paire)
    print(liste_impaire)


# Exercice 18 : Programme qui calcule les solutions d'une équation du second degré
def equation_seconde_degre():
    try:
        a = int(input("Entrer la valeur de a : "))
        b = int(input("Entrer la valeur de b : "))
        c = int(input("Entrer la valeur de c : "))

        if a == 0:
            print("Ce n'est pas une équation du second degré (a ≠ 0).")
            return

        print(f"\nL'équation est : {a}x² + {b}x + {c} = 0")

        delta = b ** 2 - 4 * a * c
        print(f"Alors, Δ = {delta}")

        if delta < 0:
            print("Aucune solution réelle (Δ < 0).")
        elif delta == 0:
            x = -b / (2 * a)
            print(f"(Δ = 0), Donc : x = {x}")
        else:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            print(f"(Δ > 0), Donc : x₁ = {x1}, x₂ = {x2}")
    except ValueError:
        print("Veuillez entrer uniquement des nombres valides.")


# Exercice 19 : Programme qui affiche si une personne est imposable ou pas
def impot():
    """
    Les hommes de plus de 20 ans paient l'impôt
    Les femmes paient l'impôt si elles ont entre 18 et 35 ans
    Les autres ne paient pas d'impôt.
    """
    try:
        age = int(input("Entrer la valeur de age : "))
        sex = input("Entrer le sex : (m) si homme - (f) si une femme : ").lower()

        if (age > 20 and sex == "m") or (18 < age < 35 and sex == "f"):
            print("Imposable")
        else:
            print("Ne pas Imposable")

    except ValueError:
        print("Veuillez entrer un age valide")


# Exercice 20 : Programme qui calcule le prix TTC d'un produit connaissant son prix hors taxe et sa categorie
def prix_ttc():
    try:
        pth = int(input("Entrer la valeur de pth : "))
        categorie = (input("Entrer la valeur de categor (A, B ou C) : ")).upper()
        if categorie not in ("A", "B", "C"):
            print("Veuillez entrer un categor valide")
            return

        if categorie == "A":
            pttc = pth + pth * 0.07
        elif categorie == "B":
            pttc = pth + pth * 0.2
        else:
            pttc = pth + pth * 0.25

        print("La PTTC de ce produit est : ", format(pttc, ".2f"))
    except ValueError:
        print("Veuillez entrer un categor valide")


# Exercice 21 : mini-Calculatrice
def calculator():
    try:
        nombre_1 = int(input("Entrer la valeur de nombre 1: "))
        nombre_2 = int(input("Entrer la valeur de nombre 2: "))
        operator = input("Choisisser un operateur (+ , - , * , / , // ou % ) : ").strip()

        if operator not in ("+", "-", "*", "/", "//", "%"):
            print("Veuillez entrer un operateur valide")
            return

        if operator == "+":
            solution = nombre_1 + nombre_2
        elif operator == "-":
            solution = nombre_1 - nombre_2
        elif operator == "*":
            solution = nombre_1 * nombre_2
        elif operator == "/":
            if nombre_2 == 0:
                print("Division par zéro impossible.")
                return
            solution = nombre_1 / nombre_2
        elif operator == "//":
            if nombre_2 == 0:
                print("Division par zéro impossible.")
                return
            solution = nombre_1 // nombre_2
        else:
            if nombre_2 == 0:
                print("Modulo par zéro impossible.")
                return
            solution = nombre_1 % nombre_2

        print(f"La solution de {nombre_1} {operator} {nombre_2} = {solution}")

    except ValueError:
        print("Erreur : Nombre invalide")


# Exercice 21 : Programme qui demande à l'utilisateur de saisir un nombre affiche quelque chose en fonction du nombre saisi
def affiche_nombre():
    nbr = int(input("Entrer la valeur de nombre (6, 4, 2, 8): "))
    if nbr == 6:
        print("le personnage va à droite")
    elif nbr == 4:
        print("le personnage va à gauche")
    elif nbr == 8:
        print("le personnage va en haut")
    elif nbr == 2:
        print("le personnage va en bas")
    else:
        print("erreur de saisie, le personnage ne bouge pas")


# Exercice 22 : Programme qui verifie si un nombre est pair ou impair
def pair_impair():
    nbr = int(input("Entrer le nombre : "))
    if nbr % 2 == 0:
        print(f"le nombre {nbr} est paire")
    else:
        print(f"le nombre {nbr} est impaire")


# Exercice 23 : Programme qui vérifie si une année est bissextile ou non
def annee_bissextile():
    try:
        annee = int(input("Entrer la valeur de annee: "))
        if not (0 <= annee <= 2025):
            print("Veuillez entrer un annee entre 0 et 2025")
            return

        if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
            print(f"Le annee {annee} est bisextile")
        else:
            print(f"{annee} n'est pas bisextile")

    except ValueError:
        print("erreur de saisie")


# Exercice 24 : Programme qui retourne le type d'un caractère
def type_caractere():
    caractere = input("Entrer une caractere : ")
    if 'a' <= caractere <= 'z' or 'A' <= caractere <= 'Z':
        print(f"{caractere} est un alphabet")
    elif '0' <= caractere <= '9':
        print(f"{caractere} est un nombre")
    else:
        print(f"{caractere} est un caractère spécial")


# Exercice 25 : Programme qui affiche les dix nombres suivants d'un nombre demande
def dix_nombre_suivant():
    initial = int(input("Entrer la valeur de initial: "))
    for i in range(initial + 1, initial + 11):
        print(i)


# Exercice 26 : Programme qui calcule et affiche la somme de 1/n
def somme_fraction():
    try:
        n = int(input("Entrer la valeur de initial: "))
        s = 0
        for i in range(1, n + 1):
            s += (1 / i)
        print(format(s, ".2f"))

    except ValueError:
        print("Veuillez entrer un nombre valide")
        somme_fraction()


# Exercice 27 : Programme qui calcule et affiche la somme S = 1 + 10 + 100+...+ 10^n
def somme_puissance():
    try:
        p = int(input("Entrer la puissance: "))
        s = 0
        for i in range(p + 1):
            s += (10 ** i)
        print(format(s))

    except ValueError:
        print("Veuillez entrer un nombre valide")
        somme_fraction()


# Exerice 28 : Programme qui demande un nombre positi no nul de départ, et qui calcule sa factorielle
def factorielle():
    try:
        n = int(input("Entrer la valeur de n : "))
        if n < 0:
            print("Veuillez entrer un nombre positif")
            return

        else:
            f = 1
            for i in range(2, n + 1):
                f *= i
        print(f)
    except ValueError:
        print("Veuillez entrer un nombre valide")


# Exercice 29 : Programme qui calcule la somme des carrées des n premiers entiers impairs
def calcul_somme_premier():
    try:
        n = int(input("Entrer la valeur de n : "))
        if n < 0:
            print("Veuillez entrer un nombre positif")
            return

        s = 0
        for i in range(n):
            impaire = 2 * i + 1
            s += impaire ** 2
        print(s)

    except ValueError:
        print("Veuillez entrer un nombre valide")


# Exercice 30 : Programme qui affichie les diviseurs d'un entier positif n non nul
def afficher_diviseurs():
    try:
        n = int(input("Entrer un entier positif non nul : "))
        if n <= 0:
            print("Veuillez entrer un entier positif non nul.")
            return

        print(f"Les diviseurs de {n} sont :")
        for i in range(1, n + 1):
            if n % i == 0:
                print(i, end=" ")

    except ValueError:
        print("Erreur : veuillez entrer un entier valide.")

# -------------------/ Application /----------------
afficher_diviseurs()
