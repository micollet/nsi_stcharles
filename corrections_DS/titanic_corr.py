# ==========================================================
# Importation des modules (Ne pas modifier)
# ==========================================================

import csv
from module_graphique import tracer_graphique

# ==========================================================
# Données pour les tests (Ne pas modifier)
# ==========================================================

donnees_test = [
    {'name': 'A', 'age': '10', 'class': '1st', 'survived': 'yes', 'fare': '50'},
    {'name': 'B', 'age': '40', 'class': '1st', 'survived': 'no', 'fare': '100'},
    {'name': 'C', 'age': '5', 'class': '3rd', 'survived': 'no', 'fare': '10'},
    {'name': 'D', 'age': 'NA', 'class': '3rd', 'survived': 'yes', 'fare': '10'},
    {'name': 'E', 'age': '60', 'class': '3rd', 'survived': 'yes', 'fare': '10'}
]

# ==========================================================
# 1. CHARGEMENT DES DONNÉES (Ne pas modifier)
# ==========================================================
def charger_donnees(nom_fichier):
    """
    Charge les données d'un fichier CSV dans une liste de dictionnaires.

    Paramètre :
        - nom_fichier (str) : chemin du fichier .csv

    Sortie :
        - liste (list) : une liste de dictionnaires (un par passager)
    """
    donnees = []
    with open(nom_fichier, mode='r', encoding='utf-8-sig') as f:
        lecteur = csv.DictReader(f, delimiter=';')
        for ligne in lecteur:
            donnees.append(dict(ligne))
    return donnees
path='/home/mikael/enseignement/2025_2026/Terminale_NSI/evaluation/evaluation_pratique/NSI_EVALUATION_PRATIQUE_3/'
data = charger_donnees(path +'titanic.csv')
for indice in range(3):
    print(data[indice])

# ==========================================================
# QUESTION 1 : Le passager le plus âgé
# ==========================================================
def trouver_doyen(liste):
    """
    Trouve le nom et l'âge de la personne la plus âgée qui a survécu.

    Paramètre :
        - liste (list) : liste de dictionnaires (données Titanic)

    Sortie :
        - tuple : (nom (str), age (float))
    """
    nom_max = ""
    age_max = 0
    for passager in liste:
        if passager['age'] != 'NA' and passager["survived"] == "yes":
            age_actuel = float(passager['age'])
            if age_actuel > age_max:
                age_max = age_actuel
                nom_max = passager['name']
    return nom_max, age_max

# TEST
assert trouver_doyen(donnees_test) == ('E', 60.0)

# ==========================================================
# QUESTION 2 : Prix moyen du billet
# ==========================================================
def calculer_prix_moyen(liste):
    """
    Calcule la moyenne des tarifs des billets.

    Paramètre :
        - liste (list) : liste de dictionnaires (données Titanic)

    Sortie :
        - moyenne (float) : prix moyen arrondi à 2 chiffres
    """
    somme = 0
    compteur = 0
    for passager in liste:
        if passager['fare'] != 'NA':
            somme = somme + float(passager['fare'])
            compteur = compteur + 1

    if compteur == 0: return 0.0
    return round(somme / compteur, 2)

# TEST

assert calculer_prix_moyen(donnees_test) == 36.0

# ==========================================================
# QUESTION 3 : Filtrage des enfants rescapés
# ==========================================================
def extraire_enfants_rescapes(liste):
    """
    Extrait les noms des enfants de moins de 12 ans ayant survécu.

    Paramètre :
        - liste (list) : liste de dictionnaires (données Titanic)

    Sortie :
        - noms (list) : liste de chaînes de caractères (noms)
    """
    noms = []
    for passager in liste:
        if passager['age'] != 'NA':
            age_num = float(passager['age'])
            if age_num < 12 and passager['survived'] == 'yes':
                noms.append(passager['name'])
    return noms

# TEST
assert extraire_enfants_rescapes(donnees_test) == ['A']

# ==========================================================
# QUESTION 4 : Taux de survie par catégorie
# ==========================================================
def calculer_taux_survie(liste):
    """
    Calcule le pourcentage de survie interne à chaque classe.

    Paramètre :
        - liste (list) : liste de dictionnaires (données Titanic)

    Sortie :
        - taux (dict) : dictionnaire {classe: pourcentage} arrondi à 2 chiffres
    """
    total_classe = {}
    survivants_classe = {}


    for passager in liste:
        classe = passager['class']


        if classe in total_classe.keys():
            total_classe[classe] = total_classe[classe] + 1
        else:
            total_classe[classe] = 1


        if passager['survived'] == 'yes':
            if classe in survivants_classe.keys():
                survivants_classe[classe] = survivants_classe[classe] + 1
            else:
                survivants_classe[classe] = 1

    resultats = {}
    for classe in total_classe.keys():
        nb_total = total_classe[classe]


        if classe in survivants_classe.keys():
            nb_surv = survivants_classe[classe]
        else:
            nb_surv = 0


        resultats[classe] = round((nb_surv / nb_total) * 100, 2)

    return resultats

# TEST
stats = calculer_taux_survie(donnees_test)
assert stats['1st'] == 50.0
assert stats['3rd'] == 66.67


# ==========================================================
# PROGRAMME PRINCIPAL (Ne pas modifier)
# ==========================================================

data = charger_donnees(path+'titanic.csv')

nom_d, age_d = trouver_doyen(data)
prix_m = calculer_prix_moyen(data)
enfants = extraire_enfants_rescapes(data)
stats_s = calculer_taux_survie(data)

print(f"\nRésultats du fichier :")
print(f"- Doyen : {nom_d} ({age_d} ans)")
print(f"- Prix moyen : {prix_m} £")
print(f"- Enfants sauvés : {len(enfants)}")

tracer_graphique(stats_s, "Taux de survie par catégorie (%)")


