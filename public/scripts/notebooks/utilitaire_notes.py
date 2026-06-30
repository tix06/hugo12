def somme(tab):
    """calcule la somme de la liste tab
    """
    s = 0
    for x in tab:
        s += x
    return s

def moyenne(tab):
    """calcule la moyenne des valeurs de la liste tab
    """
    return somme(tab)/len(tab)