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
    except:
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
    print("Après X :", x,"et Y :", y)

# -------------------/ Application /----------------
changer_contenu(-8, -4)
