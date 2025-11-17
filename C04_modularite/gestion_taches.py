#module gestion des taches

def ajouter_tache(tache,liste_tache):
    if tache not in liste_tache:
        liste_tache.append(tache)

def supprimer_tache(tache,liste_tache):
    if tache in liste_tache:
        liste_tache.remove(tache)

def afficher_taches(liste_taches):
    print(len(liste_taches)," tache(s) dans la liste")
    for t in liste_taches:
        print(t)