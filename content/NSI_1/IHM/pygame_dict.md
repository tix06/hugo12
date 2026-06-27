---
Title: dictionnaires pour inventaire
description: utilite des dictionnaires pour mon Escape Game
weight: 11
---

# Les dictionnaires Python pour gérer un escape game

**Durée** : 1 heure  
**Prérequis** : Connaître les listes Python  
**Objectif** : Découvrir les dictionnaires et comprendre pourquoi ils sont essentiels pour gérer les objets et états d'un jeu

---

## 1. Rappel : Les listes, ce que vous connaissez déjà (10 min)

### Structure des listes

Une **liste** est une collection ordonnée d'éléments, accessibles par leur **position** (index).

```python
# Liste de prénoms
prenoms = ["Alice", "Bob", "Charlie"]

# Accès par index (position)
print(prenoms[0])  # Affiche : Alice
print(prenoms[1])  # Affiche : Bob
print(prenoms[2])  # Affiche : Charlie
```

### Utiliser les listes pour un jeu : première tentative

Imaginons qu'on veuille gérer un objet de notre escape game avec une liste :

```python
# Un objet "clé" représenté par une liste
cle = ["clé dorée", 150, 200, False, "Une petite clé qui brille"]
#      [0] nom      [1] x  [2] y  [3] ramassée  [4] description

# Accès aux informations
print(cle[0])  # nom
print(cle[1])  # position x
print(cle[3])  # est-elle ramassée ?
```

### Le problème avec les listes

❌ **Difficile à lire** : Que représente `cle[3]` ? Il faut se souvenir de l'ordre  
❌ **Difficile à maintenir** : Si on ajoute une propriété, tous les indices changent  
❌ **Erreurs faciles** : Confondre l'ordre des éléments  
❌ **Code cryptique** : `if objet[3] == False:` ne dit rien sur ce qu'on vérifie

**Exercice mental** : Si on a 10 objets différents avec des propriétés différentes, comment s'en sortir avec des listes ?

---

## 2. Introduction aux dictionnaires (15 min)

### Qu'est-ce qu'un dictionnaire ?

Un **dictionnaire** est une collection d'éléments accessibles par leur **nom** (clé) plutôt que par leur position.

**Analogie** : Un dictionnaire papier
- Dans un dictionnaire français, on cherche un mot (la clé) pour obtenir sa définition (la valeur)
- On ne dit pas "donne-moi le 1547ème mot", mais "donne-moi la définition de 'escape'"

### Syntaxe de base

```python
# Création d'un dictionnaire
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Accès par clé (beaucoup plus clair !)
print(personne["nom"])    # Affiche : Alice
print(personne["age"])    # Affiche : 25
print(personne["ville"])  # Affiche : Paris
```

**Structure** :
```python
dictionnaire = {
    "clé1": valeur1,
    "clé2": valeur2,
    "clé3": valeur3
}
```

- Les **clés** sont généralement des chaînes de caractères (entre guillemets)
- Les **valeurs** peuvent être de n'importe quel type : nombres, chaînes, booléens, listes, ou même d'autres dictionnaires !

### Comparaison liste vs dictionnaire

```python
# AVEC UNE LISTE (difficile à lire)
cle_liste = ["clé dorée", 150, 200, False, "Une petite clé qui brille"]
nom = cle_liste[0]
est_ramassee = cle_liste[3]

# AVEC UN DICTIONNAIRE (clair et explicite)
cle_dict = {
    "nom": "clé dorée",
    "x": 150,
    "y": 200,
    "ramassee": False,
    "description": "Une petite clé qui brille"
}
nom = cle_dict["nom"]
est_ramassee = cle_dict["ramassee"]
```

**Quelle version préférez-vous lire ?**

### Opérations de base sur les dictionnaires

#### Accéder à une valeur
```python
joueur = {"nom": "Alice", "vie": 100, "niveau": 1}

print(joueur["nom"])      # Alice
print(joueur["vie"])      # 100
```

#### Modifier une valeur
```python
joueur["vie"] = 80        # La vie passe à 80
joueur["niveau"] = 2      # Le niveau passe à 2
```

#### Ajouter une nouvelle paire clé-valeur
```python
joueur["score"] = 1500    # Ajoute une nouvelle clé "score"
```

#### Vérifier si une clé existe
```python
if "vie" in joueur:
    print("Le joueur a des points de vie")

if "magie" in joueur:
    print("Le joueur a de la magie")
else:
    print("Pas de magie")  # Ceci sera affiché
```

#### Supprimer une paire clé-valeur
```python
del joueur["score"]       # Supprime la clé "score"
```

#### Obtenir une valeur avec une valeur par défaut
```python
# Si la clé n'existe pas, retourne une valeur par défaut
magie = joueur.get("magie", 0)  # Retourne 0 si "magie" n'existe pas
```

---

## 3. Les dictionnaires pour l'escape game (20 min)

### 3.1. Représenter un objet du jeu

Au lieu d'utiliser des listes compliquées, utilisons des dictionnaires pour chaque objet :

```python
porte = {
    "nom": "porte",
    "x": 300,
    "y": 200,
    "largeur": 150,
    "hauteur": 300,
    "verrouille": True,
    "description": "Une lourde porte en bois",
    "message_verrouille": "La porte est fermée à clé",
    "message_ouvert": "Vous ouvrez la porte et sortez. Victoire !"
}

cle = {
    "nom": "clé",
    "x": 100,
    "y": 400,
    "largeur": 30,
    "hauteur": 15,
    "ramassee": False,
    "description": "Une petite clé dorée",
    "dans_inventaire": False
}

tableau = {
    "nom": "tableau",
    "x": 450,
    "y": 150,
    "largeur": 200,
    "hauteur": 150,
    "examine": False,
    "description": "Un tableau représentant un paysage",
    "description_detaillee": "En examinant de plus près, vous voyez un code : 1234"
}
```

**Avantages** :
✅ Chaque objet peut avoir des propriétés différentes  
✅ Le code est auto-documenté (on comprend ce que fait `objet["verrouille"]`)  
✅ Facile d'ajouter de nouvelles propriétés  
✅ Pas de confusion sur l'ordre des éléments

### 3.2. Gérer une collection d'objets

On peut mettre tous les objets dans une liste :

```python
objets = [
    {
        "nom": "porte",
        "x": 300,
        "y": 200,
        "largeur": 150,
        "hauteur": 300,
        "verrouille": True,
        "description": "Une lourde porte en bois"
    },
    {
        "nom": "clé",
        "x": 100,
        "y": 400,
        "largeur": 30,
        "hauteur": 15,
        "ramassee": False,
        "description": "Une petite clé dorée"
    },
    {
        "nom": "coffre",
        "x": 550,
        "y": 350,
        "largeur": 100,
        "hauteur": 80,
        "ouvert": False,
        "description": "Un vieux coffre poussiéreux"
    }
]
```

### 3.3. Parcourir et utiliser les objets

```python
# Afficher tous les objets
for objet in objets:
    print(f"Objet : {objet['nom']} à la position ({objet['x']}, {objet['y']})")

# Trouver un objet par son nom
def trouver_objet(nom_objet):
    for objet in objets:
        if objet["nom"] == nom_objet:
            return objet
    return None

# Utilisation
porte = trouver_objet("porte")
if porte["verrouille"]:
    print("La porte est verrouillée")
```

### 3.4. Détecter un clic sur un objet

```python
def verifier_clic_objet(x_souris, y_souris):
    """Vérifie si le clic touche un objet"""
    for objet in objets:
        # Vérifier si le clic est dans les limites de l'objet
        if (objet["x"] <= x_souris <= objet["x"] + objet["largeur"] and
            objet["y"] <= y_souris <= objet["y"] + objet["hauteur"]):
            return objet
    return None

# Dans la boucle d'événements
if event.type == pygame.MOUSEBUTTONDOWN:
    x, y = event.pos
    objet_clique = verifier_clic_objet(x, y)
    
    if objet_clique:
        print(f"Vous avez cliqué sur : {objet_clique['nom']}")
        print(objet_clique["description"])
```

### 3.5. Gérer l'inventaire

```python
# L'inventaire est une liste de dictionnaires
inventaire = []

def ramasser_objet(objet):
    """Ajoute un objet à l'inventaire"""
    if not objet.get("ramassee", False):
        objet["ramassee"] = True
        inventaire.append(objet)
        return f"Vous ramassez : {objet['nom']}"
    else:
        return "Cet objet a déjà été ramassé"

def afficher_inventaire():
    """Affiche le contenu de l'inventaire"""
    if len(inventaire) == 0:
        print("Votre inventaire est vide")
    else:
        print("Inventaire :")
        for objet in inventaire:
            print(f"  - {objet['nom']}")

def objet_dans_inventaire(nom_objet):
    """Vérifie si un objet est dans l'inventaire"""
    for objet in inventaire:
        if objet["nom"] == nom_objet:
            return True
    return False
```

### 3.6. Gérer les interactions entre objets

```python
def utiliser_cle_sur_porte():
    """Tente d'ouvrir la porte avec la clé"""
    porte = trouver_objet("porte")
    
    if objet_dans_inventaire("clé"):
        if porte["verrouille"]:
            porte["verrouille"] = False
            return "Vous utilisez la clé. La porte s'ouvre !"
        else:
            return "La porte est déjà ouverte"
    else:
        return "Vous n'avez pas de clé"

def examiner_objet(objet):
    """Examine un objet en détail"""
    if objet["nom"] == "tableau" and not objet.get("examine", False):
        objet["examine"] = True
        return objet.get("description_detaillee", objet["description"])
    else:
        return objet["description"]
```

---

## 4. Exemple complet : Mini escape game avec dictionnaires (10 min)

Voici un exemple fonctionnel simplifié qui montre comment tout s'assemble :

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

# Définition des objets avec des dictionnaires
objets = [
    {
        "nom": "clé",
        "x": 100,
        "y": 400,
        "largeur": 40,
        "hauteur": 20,
        "couleur": (255, 215, 0),  # Doré
        "ramassee": False,
        "description": "Une clé dorée"
    },
    {
        "nom": "porte",
        "x": 650,
        "y": 200,
        "largeur": 100,
        "hauteur": 200,
        "couleur": (139, 69, 19),  # Marron
        "verrouille": True,
        "description": "Une porte en bois"
    }
]

# État du jeu
inventaire = []
message = "Trouvez la clé et ouvrez la porte !"
victoire = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and not victoire:
            x_souris, y_souris = event.pos
            
            # Vérifier les clics sur les objets
            for objet in objets:
                if (objet["x"] <= x_souris <= objet["x"] + objet["largeur"] and
                    objet["y"] <= y_souris <= objet["y"] + objet["hauteur"]):
                    
                    # Clic sur la clé
                    if objet["nom"] == "clé" and not objet["ramassee"]:
                        objet["ramassee"] = True
                        inventaire.append(objet)
                        message = "Vous ramassez la clé !"
                    
                    # Clic sur la porte
                    elif objet["nom"] == "porte":
                        # Vérifier si on a la clé
                        a_la_cle = any(obj["nom"] == "clé" for obj in inventaire)
                        
                        if a_la_cle and objet["verrouille"]:
                            objet["verrouille"] = False
                            message = "Vous ouvrez la porte ! VICTOIRE !"
                            victoire = True
                        elif objet["verrouille"]:
                            message = "La porte est verrouillée. Il faut une clé."
                        else:
                            message = "La porte est déjà ouverte !"
    
    # Affichage
    screen.fill((50, 50, 50))  # Fond gris
    
    # Dessiner les objets
    for objet in objets:
        # Ne pas dessiner la clé si elle est ramassée
        if objet["nom"] == "clé" and objet["ramassee"]:
            continue
        
        pygame.draw.rect(screen, objet["couleur"], 
                        (objet["x"], objet["y"], objet["largeur"], objet["hauteur"]))
    
    # Afficher le message
    texte = font.render(message, True, (255, 255, 255))
    screen.blit(texte, (50, 550))
    
    # Afficher l'inventaire
    inv_text = "Inventaire : " + ", ".join([obj["nom"] for obj in inventaire])
    if len(inventaire) == 0:
        inv_text = "Inventaire : vide"
    inv_surface = font.render(inv_text, True, (200, 200, 200))
    screen.blit(inv_surface, (50, 20))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

**Ce que fait ce programme** :
1. Définit une clé et une porte comme dictionnaires
2. Permet de cliquer sur la clé pour la ramasser
3. La clé disparaît et va dans l'inventaire
4. On peut cliquer sur la porte pour tenter de l'ouvrir
5. La porte s'ouvre seulement si on a la clé

---

## 5. Dictionnaires avancés pour le jeu (10 min)

### 5.1. Dictionnaires imbriqués

On peut mettre des dictionnaires dans des dictionnaires :

```python
objet_complexe = {
    "nom": "coffre",
    "position": {
        "x": 100,
        "y": 200
    },
    "dimensions": {
        "largeur": 80,
        "hauteur": 60
    },
    "contenu": {
        "or": 50,
        "gemmes": 3,
        "objet_special": "amulette"
    },
    "ouvert": False
}

# Accès aux valeurs imbriquées
print(objet_complexe["position"]["x"])  # 100
print(objet_complexe["contenu"]["or"])   # 50
```

### 5.2. État global du jeu

Un dictionnaire peut représenter l'état complet du jeu :

```python
etat_jeu = {
    "niveau_actuel": 1,
    "temps_ecoule": 0,
    "enigmes_resolues": ["enigme1", "enigme3"],
    "inventaire": [],
    "score": 1500,
    "indices_trouves": {
        "code_coffre": True,
        "message_secret": False
    },
    "pieces_visitees": ["salon", "cuisine"],
    "drapeaux": {
        "porte_ouverte": False,
        "alarme_declenchee": False,
        "a_parle_au_gardien": True
    }
}

# Vérifications faciles
if "code_coffre" in etat_jeu["indices_trouves"]:
    print("Vous connaissez le code du coffre")

if etat_jeu["drapeaux"]["a_parle_au_gardien"]:
    print("Le gardien vous a donné un indice")
```

### 5.3. Actions et interactions

On peut même stocker des fonctions ou des messages dans les dictionnaires :

```python
objets_interactifs = [
    {
        "nom": "levier",
        "x": 300,
        "y": 250,
        "actif": False,
        "description_initial": "Un levier rouillé",
        "description_active": "Le levier a été activé. Un passage secret s'ouvre.",
        "action": "ouvrir_passage"
    },
    {
        "nom": "livre",
        "x": 150,
        "y": 180,
        "lu": False,
        "description": "Un vieux grimoire",
        "texte": "Les pages révèlent : 'Le code est 4-2-7-9'",
        "action": "donner_indice"
    }
]

def interagir_avec_objet(objet):
    """Gère l'interaction avec un objet selon son type d'action"""
    if objet["action"] == "ouvrir_passage":
        objet["actif"] = True
        return objet["description_active"]
    
    elif objet["action"] == "donner_indice":
        if not objet["lu"]:
            objet["lu"] = True
            return objet["texte"]
        else:
            return "Vous avez déjà lu ce livre"
    
    return objet["description"]
```

### 5.4. Système de quêtes

```python
quetes = [
    {
        "id": "trouver_cle",
        "titre": "Trouver la clé",
        "description": "Cherchez la clé pour ouvrir la porte",
        "terminee": False,
        "objectifs": {
            "cle_trouvee": False
        }
    },
    {
        "id": "resoudre_enigme",
        "titre": "Résoudre l'énigme du tableau",
        "description": "Déchiffrez le message caché dans le tableau",
        "terminee": False,
        "objectifs": {
            "tableau_examine": False,
            "code_trouve": False
        }
    }
]

def verifier_quetes():
    """Vérifie si les quêtes sont terminées"""
    for quete in quetes:
        if not quete["terminee"]:
            # Vérifier si tous les objectifs sont remplis
            tous_objectifs = all(quete["objectifs"].values())
            if tous_objectifs:
                quete["terminee"] = True
                return f"Quête terminée : {quete['titre']}"
    return None
```

---

## 6. Comparaison finale et bonnes pratiques (5 min)

### Pourquoi les dictionnaires sont parfaits pour les jeux

| Critère | Listes | Dictionnaires |
|---------|--------|---------------|
| Lisibilité | ❌ `objet[3]` | ✅ `objet["verrouille"]` |
| Flexibilité | ❌ Ordre fixe | ✅ Propriétés variables |
| Maintenance | ❌ Changer l'ordre casse tout | ✅ Ajouter/retirer facilement |
| Clarté du code | ❌ Besoin de commentaires | ✅ Auto-documenté |
| Gestion d'objets complexes | ❌ Très difficile | ✅ Naturel |

### Bonnes pratiques avec les dictionnaires

✅ **Utilisez des noms de clés descriptifs**
```python
# Bien
joueur = {"points_de_vie": 100, "niveau": 5}

# Moins bien
joueur = {"pv": 100, "niv": 5}
```

✅ **Soyez cohérents dans la structure**
```python
# Tous les objets ont les mêmes clés de base
objet1 = {"nom": "...", "x": 0, "y": 0, "description": "..."}
objet2 = {"nom": "...", "x": 0, "y": 0, "description": "..."}
```

✅ **Utilisez `.get()` pour éviter les erreurs**
```python
# Risqué - erreur si la clé n'existe pas
vie = joueur["vie"]

# Sûr - retourne 100 par défaut
vie = joueur.get("vie", 100)
```

✅ **Documentez la structure de vos dictionnaires**
```python
# Structure d'un objet du jeu :
# {
#     "nom": str,           # Nom de l'objet
#     "x": int,             # Position X
#     "y": int,             # Position Y
#     "ramassable": bool,   # Peut-on le ramasser ?
#     "description": str    # Description affichée
# }
```

### Quand utiliser listes vs dictionnaires ?

**Utilisez une liste quand** :
- L'ordre est important
- Vous avez une série d'éléments similaires et simples
- Exemple : `scores = [100, 95, 87, 82]`

**Utilisez un dictionnaire quand** :
- Vous avez des propriétés nommées
- Vous voulez accéder aux données par leur signification
- Vous gérez des objets complexes
- Exemple : `joueur = {"nom": "Alice", "score": 100, "niveau": 3}`

---

## Récapitulatif

🎯 **Les dictionnaires** permettent d'accéder aux données par **nom** (clé) plutôt que par position

🎯 **Syntaxe** : `{"clé": valeur, "clé2": valeur2}`

🎯 **Parfaits pour** : Représenter des objets de jeu avec de multiples propriétés

🎯 **Avantages** : Code lisible, flexible, maintenable, auto-documenté

🎯 **Pour votre escape game** :
- Chaque objet est un dictionnaire
- L'inventaire est une liste de dictionnaires
- L'état du jeu est un dictionnaire
- Les quêtes sont des dictionnaires dans une liste

---

## Exercices pratiques

### Exercice 1 : Créer vos objets
Créez 3 dictionnaires représentant des objets pour votre escape game. Chaque objet doit avoir au minimum : nom, position (x, y), dimensions, et une description.

### Exercice 2 : Fonction de recherche
Écrivez une fonction `trouver_objet_par_nom(nom, liste_objets)` qui cherche un objet dans une liste de dictionnaires et le retourne.

### Exercice 3 : Système d'inventaire
Créez un système d'inventaire avec les fonctions :
- `ajouter_a_inventaire(objet)`
- `retirer_de_inventaire(nom_objet)`
- `afficher_inventaire()`

### Exercice 4 : Interaction complexe
Créez une fonction qui vérifie si le joueur peut ouvrir un coffre :
- Le coffre doit être fermé
- Le joueur doit avoir la clé dans son inventaire
- Si oui, le coffre s'ouvre et donne son contenu

---

## Pour aller plus loin dans votre projet

Maintenant que vous connaissez les dictionnaires, vous pouvez :

1. **Créer un fichier JSON** pour stocker vos objets (JSON est basé sur les dictionnaires)
2. **Gérer plusieurs salles** avec un dictionnaire de salles
3. **Créer un système de sauvegarde** en enregistrant l'état du jeu
4. **Ajouter des dialogues** avec des personnages (PNJ)
5. **Implémenter des énigmes complexes** avec plusieurs étapes

**Bon courage pour votre escape game !** 🗝️🚪