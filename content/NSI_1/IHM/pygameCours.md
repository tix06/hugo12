---
Title: IHM python Cours
description: Du séquentiel à l'événementiel, pygame, fenetre graphique, calques
weight: 10
---

# Interface Homme-Machine en Python avec Pygame

**Durée** : 1 heure  
**Objectif** : Comprendre les bases des interfaces graphiques et du paradigme événementiel pour préparer la création d'un jeu type escape game/RPG

---

## Introduction aux Interfaces Homme-Machine (lecture 10 min)

### Qu'est-ce qu'une Interface Homme-Machine (IHM) ?

Une Interface Homme-Machine est le **moyen de communication** entre un utilisateur et un programme informatique. C'est tout ce qui permet à l'utilisateur d'interagir avec le logiciel et de recevoir des informations en retour.

**Exemples du quotidien :**
- Les applications sur smartphone (boutons, gestes tactiles)
- Les sites web (menus, formulaires, boutons)
- Les jeux vidéo (interfaces de jeu, menus)
- Les logiciels de bureautique (barres d'outils, fenêtres)

### Les deux grands types d'interfaces

#### CLI - Command Line Interface (Interface en ligne de commande)
- L'utilisateur tape des commandes textuelles
- Le programme répond avec du texte
- Exemple : le terminal, les programmes Python simples avec `input()`

```python
# Exemple CLI classique
nom = input("Quel est votre nom ? ")
print(f"Bonjour {nom} !")
```

**Avantages** : Simple à programmer, précis, rapide pour les utilisateurs expérimentés  
**Inconvénients** : Peu intuitif, courbe d'apprentissage élevée

#### GUI - Graphical User Interface (Interface graphique)
- L'utilisateur interagit avec des éléments visuels (boutons, images, icônes)
- Le programme répond visuellement
- Exemple : les jeux vidéo, les applications modernes

**Avantages** : Intuitif, accessible, visuellement attractif  
**Inconvénients** : Plus complexe à programmer

---

## Le paradigme événementiel (lecture 15 min)

### Du séquentiel à l'événementiel

#### Programmation séquentielle (ce que vous connaissez)
Le programme s'exécute **ligne par ligne**, de haut en bas, de manière prévisible.

```python
# Exemple séquentiel
print("Début du programme")
x = 5
y = 10
resultat = x + y
print(f"Résultat : {resultat}")
print("Fin du programme")
```

Le programme se termine après la dernière ligne.

#### Programmation événementielle (nouveau paradigme)
Le programme reste **en attente** et **réagit aux actions de l'utilisateur**.

```python
# Pseudo-code événementiel
while programme_actif:
    evenement = attendre_action_utilisateur()
    
    if evenement == "clic_souris":
        traiter_clic()
    elif evenement == "touche_clavier":
        traiter_touche()
    elif evenement == "fermeture_fenetre":
        programme_actif = False
```

Le programme ne se termine que lorsque l'utilisateur décide de le fermer.

### Les événements

Un **événement** est une action effectuée par l'utilisateur (ou par le système) que le programme peut détecter et traiter.

**Types d'événements courants :**
- `MOUSEBUTTONDOWN` : L'utilisateur clique avec la souris
- `MOUSEBUTTONUP` : L'utilisateur relâche le bouton de la souris
- `MOUSEMOTION` : L'utilisateur déplace la souris
- `KEYDOWN` : L'utilisateur appuie sur une touche du clavier
- `KEYUP` : L'utilisateur relâche une touche
- `QUIT` : L'utilisateur ferme la fenêtre

### Schéma de la boucle événementielle

```
┌─────────────────────────────────┐
│   Initialisation du programme   │
└────────────┬────────────────────┘
             │
             ▼
┌────────────────────────────────┐
│    BOUCLE PRINCIPALE (infinie) │◄───┐
├────────────────────────────────┤    │
│  1. Récupérer les événements   │    │
│  2. Traiter chaque événement   │    │
│  3. Mettre à jour la logique   │    │
│  4. Dessiner à l'écran         │    │
│  5. Rafraîchir l'affichage     │────┘
└────────────┬───────────────────┘
             │
             ▼ (si événement QUIT)
┌────────────────────────────────┐
│      Fermeture propre          │
└────────────────────────────────┘
```

---

## Introduction à Pygame (lecture 20 min)

### Pourquoi Pygame ?

**Pygame** est une bibliothèque Python spécialement conçue pour créer des jeux 2D et des applications graphiques interactives.

**Avantages :**
- Facile à apprendre pour les débutants
- Gestion simplifiée des graphismes, sons et événements
- Grande communauté et nombreux tutoriels
- Idéal pour des jeux 2D, prototypes et projets éducatifs

**Installation :**
```bash
pip install pygame
```

### Structure minimale d'un programme Pygame

Voici le squelette de base que vous utiliserez pour tous vos projets Pygame :

```python
import pygame

# ============================================
# INITIALISATION
# ============================================
pygame.init()

# Création de la fenêtre
LARGEUR = 600
HAUTEUR = 600
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Mon premier programme Pygame")

# Horloge pour contrôler les FPS (images par seconde)
clock = pygame.time.Clock()

# Variable de contrôle de la boucle
running = True

# ============================================
# BOUCLE PRINCIPALE
# ============================================
while running:
    # 1. GESTION DES ÉVÉNEMENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 2. LOGIQUE DU JEU: 
    # (mise à jour des positions, calculs, etc.)
    
    # 3. AFFICHAGE: 
    screen.fill((0, 0, 0))  # Efface l'écran avec du noir
    
    # Dessiner vos éléments ici
    
    pygame.display.flip()  # Met à jour l'affichage
    
    # 4. CONTRÔLE DU FRAMERATE
    clock.tick(60)  # 60 images par seconde

# ============================================
# FERMETURE PROPRE
# ============================================
pygame.quit()
```

## Explication détaillée des éléments clés

### Initialisation de Pygame
```python
pygame.init()
```
Cette ligne initialise tous les modules de Pygame. Elle doit toujours être appelée au début.

### Création de la fenêtre
```python
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
```
Crée une fenêtre de dimensions LARGEUR × HAUTEUR pixels. L'objet `screen` représente la surface d'affichage principale.

{{< img src="../images/pg0.png" caption="exemple: pygame.display.set_mode((600, 600))" >}}

### L'horloge
```python
clock = pygame.time.Clock()
# ... plus tard dans la boucle
clock.tick(60)
```
L'horloge contrôle la vitesse du jeu. `clock.tick(60)` limite le programme à 60 images par seconde (FPS), rendant le jeu fluide et cohérent sur différentes machines.

### La boucle de jeu
```python
while running:
```
C'est le cœur du programme. Tant que `running` est `True`, le programme continue. Cette boucle s'exécute environ 60 fois par seconde.

### Gestion des événements

```python
import pygame

(...)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
```

`pygame.event.get()` récupère tous les événements qui se sont produits depuis la dernière itération. On parcourt cette liste et on réagit selon le type d'événement.

D'autres evenements utiles:

```python
# retourne True si le bouton souris est appuyé
event.type == pygame.MOUSEBUTTONDOWN
```

```python
# True si le bouton est relaché
event.type == pygame.MOUSEBUTTONUP
```

### Remplissage de l'écran

```python
screen.fill((0, 0, 0))
```

Efface l'écran en le remplissant d'une couleur. Les couleurs en Pygame sont des tuples RGB : `(Rouge, Vert, Bleu)` avec des valeurs de 0 à 255.

Exemples :

- `(0, 0, 0)` = noir
- `(255, 255, 255)` = blanc
- `(255, 0, 0)` = rouge
- `(0, 255, 0)` = vert
- `(0, 0, 255)` = bleu

### Rafraîchissement de l'affichage
```python
pygame.display.flip()
```
Met à jour tout l'écran avec ce qui a été dessiné. Sans cette ligne, rien ne s'affichera !

### Exemple complet n°1: Fenêtre avec changement de couleur au clic

```python
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Changer la couleur au clic")
clock = pygame.time.Clock()

# Couleur de fond initiale
couleur_fond = (50, 50, 100)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Détecter un clic de souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Changer la couleur aléatoirement
            couleur_fond = (random.randint(0, 255),
                           random.randint(0, 255),
                           random.randint(0, 255))
    
    # Remplir l'écran avec la couleur actuelle
    screen.fill(couleur_fond)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

{{< img src="../images/pg5.png" >}}

**Exercice mental** : Que se passe-t-il si vous cliquez plusieurs fois?

{{< img src="../images/pg6.png" >}}

---

## Éléments pour votre projet (lecture 10 min)

Pour créer votre escape game/RPG, vous aurez besoin de maîtriser ces éléments :

### Afficher une image de fond

```python
# Chargement d'une image
image_fond = pygame.image.load("fond_salle.png")

# Dans la boucle, affichage de l'image
screen.blit(image_fond, (0, 0))  # (0, 0) = position en haut à gauche
```

**Note importante** : Le système de coordonnées dans Pygame :

```
(0, 0) ──────► X (largeur)
  │
  │
  │
  ▼
  Y (hauteur)
```

Le point (0, 0) est en **haut à gauche** de l'écran !

### Afficher une image à une certaine position

* **placer une figure rectangle**

La fonction `pygame.draw.rect(screen, color, (x, y, width, height))` dessine un rectangle. `(x, y, width, height)` est un tuple Python. 

`x` et `y` sont les coordonnées du coin supérieur gauche. `width` et `height` sont la largeur et la hauteur du rectangle:

```python
RED = (255,0,0)
# Dessiner
pygame.draw.rect(screen, RED, (170, 140, 60, 120))
```



**Exemple complet* n°2*

```python
import pygame
 
RED = (255, 0, 0)
pygame.init()
h,w = 400,400
screen = pygame.display.set_mode((w, h))
stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    pygame.draw.rect(screen, RED, (170, 140, 60, 120))
    pygame.display.flip()
 
pygame.quit()
```

{{< img src="../images/pg1.png" >}}

* **placer une image rectangle (porte)**

Pour cet exemple, télécharger les images:

* [door1.png](../images/door1.png)
* [door2.png](../images/door2.png)

```python
# Chargement image
door = pygame.image.load("door1.png")
# Dessiner
screen.blit(door, (170, 140))
```

{{< img src="../images/pg3.png" >}}

**Exemple complet n°3**

```python
import pygame

pygame.init()
h,w = 400,400
screen = pygame.display.set_mode((w, h))
# Chargement image
door = pygame.image.load("door1.png")
# Dessiner
screen.blit(door, (170, 140))
stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    pygame.display.flip()
 
pygame.quit()
quit()
```

### Détecter un clic sur une zone précise
**cliquer:**

```python
# Dans la boucle d'événements
if event.type == pygame.MOUSEBUTTONDOWN:
    x, y = event.pos  # Position du clic
    
    # Vérifier si le clic est dans une zone rectangulaire
    # Zone de l'objet : x entre 100 et 200, y entre 150 et 250
    if 100 <= x <= 200 and 150 <= y <= 250:
        print("Vous avez cliqué sur l'objet !")
```

**relacher:**

```python
# Dans la boucle d'événements
if event.type == pygame.MOUSEBUTTONUP:
    x, y = event.pos  # Position du clic
    
    # Vérifier si le clic est dans une zone rectangulaire
    # Zone de l'objet : x entre 100 et 200, y entre 150 et 250
    if 100 <= x <= 200 and 150 <= y <= 250:
        print("Vous avez relaché le bouton !")
```

**Exemple complet n°4**

```python
import pygame
 
RED = (255, 0, 0)
BLUE =(0,0,255)
pygame.init()
h,w = 400,400
screen = pygame.display.set_mode((w, h))
pygame.draw.rect(screen, RED, (170, 140, 60, 120))
stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 170 <= x <= 230 and 140 <= y <= 260:
                print("Vous avez cliqué sur l'objet !")
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            if 170 <= x <= 230 and 140 <= y <= 260:
                print("Vous avez relaché le bouton !")      
    pygame.display.flip()
 
pygame.quit()
```

**Exercice 1:** Créer un programme complet qui permet de changer la couleur de la porte lorsque l'on clique sur celle-ci (et que l'on maintient appuyé), mais qui remet la première couleur lorsque l'on relâche le bouton:

{{< img src="../images/pg8.png" >}}

**Exercice 2:** Créer un programme qui permet de changer la couleur de la porte lorsque l'on clique sur celle-ci. Il faudra à nouveau cliquer sur la porte pour retrouver la couleur d'origine.

### Detecter un clic sur un objet
**Méthode** : Utilisez `pygame.Rect` pour créer un calque rectangle:

```python
# Définir un rectangle pour l'objet
objet_rect = pygame.Rect(100, 150, 100, 100)  # x, y, largeur, hauteur

# Dans la boucle d'événements
if event.type == pygame.MOUSEBUTTONDOWN:
    if objet_rect.collidepoint(event.pos):
        print("Objet cliqué !")
```

* **Utiliser ce calque sur une image**
Il faut appliquer le calque sur l'image, qui aura les mêmes dimensions que celle-ci:

```python
# charger l'image
door = pygame.image.load("datas/images/door1.png")
# creation d'une surface rectangle 
# que l'on nomme rect
# de meme dimension que l'image door
rect = door.get_rect()
# Position de rect dans la fenetre graphique (centré)
rect.center = w//2, h//2
# Dessiner l'objet à la même position que le calque
screen.blit(door, rect)
```

Ce calque est alors *cliquable:*

```python
if event.type == pygame.MOUSEBUTTONDOWN:
	if rect.collidepoint(event.pos):
		print("l'objet a ete cliqué")
```

**Exemple complet n°5:**

```python
import pygame

pygame.init()
door = pygame.image.load("datas/images/door1.png")

h,w = 400,400
screen = pygame.display.set_mode((w, h))
rect = door.get_rect()
rect.center = w//2, h//2
stop = False
while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
         
        elif event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    print('on tape à la porte')
            
    screen.fill(0) # On efface tout l'écran
    screen.blit(door, rect)
    pygame.display.flip()
 
pygame.quit()
```

**Exercice 1:** On dispose de 2 images d'une même porte, aux contours différents. Créer un programme complet qui permet de changer l'image de la porte lorsque l'on clique sur celle-ci (et que l'on maintient appuyé), mais qui remet la première image lorsque l'on relâche le bouton:

{{< img src="../images/pg7.png" >}}

**Exercice 2:** Créer un programme qui permet de changer l'image de la porte lorsque l'on clique sur celle-ci. Il faudra à nouveau cliquer sur la porte pour retrouver l'image d'origine.

### Afficher du texte
* Première étape: utiliser le [module font](https://www.pygame.org/docs/ref/font.html#pygame.font.init). On créé un objet `pygame.font`, pour lequel on choisit une police de caractères (par defaut, laisser `None`) et une taille pour cette police:

```python
my_font = pygame.font.SysFont('Comic Sans MS', 30)
```

* il faut créer une surface sur laquelle on écrit, à l'aide de la fonction `render`:

```
render(text, antialias, color, background=None) -> Surface
```

*Exemple:* 

```python
couleur = (255, 255, 255)
texte = "Hello World"
texte_surface = my_font.render(texte, True, couleur)
```

L'[anticrénelage](https://fr.wikipedia.org/wiki/Anticr%C3%A9nelage) ou anti-aliasing, ou lissage des obliques ou encore lissage de police, est une méthode permettant d'éviter le crénelage.

* Troisième étape: Afficher et positionner la surface avec la fonction `blit`:

```python
screen.blit(texte_surface, (0,0))  # Position du texte 
								   # en haut à gauche
```

*au final:*

```python
screen.fill(255,255,255)
font = pygame.font.Font(None, 36)  # None = police par défaut, 36 = taille
texte = "Bienvenue dans la salle mystérieuse"
texte_surface = font.render(texte, True, (0,0,0))  # True = antialiasing
screen.blit(texte_surface, (50, 500))  # Position du texte
```

**Exemple complet n°6:**

```python
import pygame

pygame.init()
h,w = 400,400
screen = pygame.display.set_mode((w, h))
screen.fill(255,255,255)
font = pygame.font.Font(None, 36) 
texte = "Bienvenue dans la salle mystérieuse"
texte_surface = font.render(texte, True, (0,0,0)) 
screen.blit(texte_surface, (50, 500)) 
stop = False

while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
            
    pygame.display.flip()
 
pygame.quit()
```

{{< img src="../images/pg9.png" >}}

*Remarques:*

* Chaque fois que le texte change, il faudra créer une nouvelle surface à placer sur l'ancienne.
* Pour changer de ligne, on ne pourra pas utiliser le symbole "`\n`". Il faudra créer une nouvelle surface pour chaque ligne, et la positionner de manière correcte. 

{{< img src="../images/pg10.png" >}}

**Exercice:** Ecrire un programme qui affiche les 2 lignes comme ci-dessus.

### Detecter l'appui sur une touche du clavier
Pour detecter l'appui sur la touche `"h"` du clavier, on utilisera la séquence d'instruction suivantes:

```python
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == "h": 
                print('HELP')
```

*(à placer dans la zone de gestion des évènements)*

<!--
### Créer un bouton interactif

```python
# Définir le bouton
bouton_rect = pygame.Rect(50, 50, 150, 50)  # x, y, largeur, hauteur
bouton_texte = "Examiner"
bouton_couleur = (100, 100, 200)
bouton_couleur_hover = (150, 150, 255)

# Dans la boucle
# Vérifier si la souris survole le bouton
souris_pos = pygame.mouse.get_pos()
if bouton_rect.collidepoint(souris_pos):
    couleur_actuelle = bouton_couleur_hover
else:
    couleur_actuelle = bouton_couleur

# Dessiner le bouton
pygame.draw.rect(screen, couleur_actuelle, bouton_rect)

# Dessiner le texte du bouton
font = pygame.font.Font(None, 30)
texte_surface = font.render(bouton_texte, True, (255, 255, 255))
# Centrer le texte dans le bouton
texte_rect = texte_surface.get_rect(center=bouton_rect.center)
screen.blit(texte_surface, texte_rect)

# Détecter le clic
if event.type == pygame.MOUSEBUTTONDOWN:
    if bouton_rect.collidepoint(event.pos):
        print("Bouton cliqué !")
```

### Exemple complet : Image avec objet cliquable

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Charger l'image de fond
fond = pygame.image.load("salle.png")

# Zone cliquable pour un objet (par exemple une porte)
porte_rect = pygame.Rect(300, 200, 150, 300)

# Texte affiché
message = "Cliquez sur la porte"
font = pygame.font.Font(None, 32)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if porte_rect.collidepoint(event.pos):
                message = "La porte est verrouillée !"
    
    # Affichage
    screen.blit(fond, (0, 0))
    
    # Dessiner un rectangle semi-transparent sur la zone cliquable (debug)
    s = pygame.Surface((porte_rect.width, porte_rect.height))
    s.set_alpha(50)  # Transparence
    s.fill((255, 0, 0))
    screen.blit(s, (porte_rect.x, porte_rect.y))
    
    # Afficher le message
    texte_surface = font.render(message, True, (255, 255, 255))
    screen.blit(texte_surface, (50, 500))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit() # utile sur jupyter notebook
```
-->

---


**3. Testez progressivement**
- D'abord : affichez juste la fenêtre et l'image de fond
- Ensuite : ajoutez la détection de clic sur une zone
- Puis : ajoutez l'affichage de texte
- Enfin : ajoutez les boutons et la logique du jeu

**4. Utilisez des commentaires et des constantes**
```python
# Constantes
LARGEUR = 800
HAUTEUR = 600
COULEUR_FOND = (0, 0, 0)
FPS = 60

# États du jeu
ETAT_DEBUT = 0
ETAT_JEU = 1
ETAT_VICTOIRE = 2
```

### Structure de base pour votre TP

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Chargement des ressources
fond = pygame.image.load("salle.png")
font = pygame.font.Font(None, 28)

# Définition des objets interactifs
objets = [
    # À compléter
]

# Variables de jeu
message_actuel = "Explorez la salle..."
inventaire = []

running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier les clics sur les objets
            # Vérifier les clics sur les boutons
            pass
    
    # Affichage
    screen.blit(fond, (0, 0))
    
    # Afficher les boutons
    
    # Afficher le message
    texte = font.render(message_actuel, True, (255, 255, 255))
    screen.blit(texte, (50, 550))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()
```

---

## Récapitulatif des concepts clés

✅ **IHM** : Moyen de communication entre l'utilisateur et le programme  
✅ **Paradigme événementiel** : Le programme attend et réagit aux actions  
✅ **Boucle de jeu** : Cœur du programme, s'exécute en continu  
✅ **Événements** : Actions détectables (clics, touches, etc.)  
✅ **Pygame** : Bibliothèque pour créer des jeux 2D en Python  
✅ **Structure** : Init → Boucle (événements → logique → affichage) → Quit

---

## Ressources utiles

- Documentation officielle Pygame : https://www.pygame.org/docs/
- Tutoriels vidéo : recherchez "Pygame tutorial" sur YouTube
- Exemples de code : https://github.com/pygame/pygame/tree/main/examples
- Chargement des images, format et transparence: [https://zestedesavoir.com](https://zestedesavoir.com/tutoriels/846/pygame-pour-les-zesteurs/1381_a-la-decouverte-de-pygame/5505_afficher-des-images/)

---

# Suite
* Le TP Escape Game: [Lien](../pygame)
* Les dictionnaires python et leur application pour le projet Escape Game: [Lien](../pygame_dict)