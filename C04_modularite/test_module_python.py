import random
import os
import datetime

def lancer_des():
    return random.randint(1,6)

def liste_fichiers(repertoire):
    return os.listdir(repertoire)

def afficher_date_actuelle():
    print(datetime.datetime.now())

print(lancer_des())
print(liste_fichiers('/home/mikael/athle'))

afficher_date_actuelle()