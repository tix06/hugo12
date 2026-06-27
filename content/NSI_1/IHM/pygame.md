---
Title: projet Pygame
description: projet pygame
weight: 12
---

*Prérequis:*

* Cours sur l'IHM: [Lien](../pygameCours)

# Escape Game en langage python-pygame
## Script initial
Un Escape Game est un jeu vidéo où il est question de s’échapper d’une pièce dans laquelle un joueur est enfermé. Pour cela, il fallait découvrir des éléments cachés dans le décor afin de trouver une clé qui permettrait au joueur de s’échapper de la pièce. 

Vous allez créer votre jeu à l'aide du module [Pygame](../pygameCours), en langage python.

Voici un exemple de ce qu'il est possile de réaliser:

{{< img src="../images/pg11.png" >}}

Les **images** qui servent à l'exemple sont à **télécharger** depuis le dossier [source](../images/images_datas.zip).

Nous partirons du script initial suivant:

```python
# Script mini pour le jeu
import pygame

# ============================================
# INITIALISATION
# ============================================
pygame.init()

# ==== Création de la fenêtre 
# ==== et chargement des ressources: ZONE 1
LARGEUR = 700
HAUTEUR = 400
# --- image fond
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Escape Game")
fond = pygame.image.load("salon.png").convert()
screen.blit(fond, (0,0))
# --- objets interactifs (porte, ...)
door1 = pygame.image.load("door3.png").convert_alpha()
rect1 = door1.get_rect()
rect1.center = LARGEUR//2+10, (HAUTEUR-100)//2
screen.blit(door1,rect1)
# --- texte
font = pygame.font.Font(None, 36)  
texte = "Bienvenue dans la salle mystérieuse"
texte_surface = font.render(texte, True, (255,255,255))  
screen.blit(texte_surface, (0, 300))

# ==== Variables de contrôle de la boucle et du jeu: ZONE 2
running = True

# ============================================
# BOUCLE PRINCIPALE
# ============================================
while running:
    # GESTION DES ÉVÉNEMENTS: ZONE 3
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == "h": 
                print('HELP')
        elif event.type == pygame.MOUSEBUTTONDOWN:
                if rect1.collidepoint(event.pos):
                    print("Vous essayez d'ouvrir la porte")
    
    # LOGIQUE DU JEU: ZONE 4
    # (mise à jour des variables du jeu, calculs, etc.)
    
    # AFFICHAGE: ZONE 5
    
    
    # Met à jour l'affichage
    pygame.display.flip()  
    

# ============================================
# FERMETURE PROPRE
# ============================================
pygame.quit()
```

## Ajouter d'autres objets
Vous pouvez aussi laisser cours à votre imagination, et dessiner vos propres images.

Par exemple, si vous voulez ajouter une clé, voici l'image en format *png* (transparence du fond):

{{< img src="../images/cle.png" link="../images/cle.png" >}}

Ajouter alors les instructions pour créer une surface et reduire sa taille (ZONE 1)

```python
cle = pygame.image.load("datas/images/cle.png")
cle = pygame.transform.scale(cle, (60,27))
```

Pour créer un calque sur l'objet:

```python
rect2 = cle.get_rect()
rect2.center = 80,115
```

Pour afficher l'image:

```python
screen.blit(cle,rect2)
```

## Conseils pour votre projet de TP

### Architecture recommandée pour votre escape game

Votre jeu devrait comporter ces éléments :

1. **Image de fond** : Un décor de salle (chambre, bureau, etc.)
2. **Objets interactifs** : Zones cliquables sur l'image (porte, livres, tableau, bouton de la télévision, etc.)
3. **Zone de texte** : Affichage des descriptions et dialogues en bas de l'écran
4. **Touches de commande ou clic sur un objet** : Actions possibles (examiner, utiliser, inventaire, obtenir de l'aide, etc.)
5. **Système d'état** : Gérer ce qui a été fait ou trouvé: utiliser un dictionnaire pour chacun des objets (voir plus bas). Et modifier, lorsque l'on clique sur l'objet, les variables d'état de l'objet. Par exemple: `cle["ramasse"] = True`, ou `cle["visible"] = False` *(voir plus bas)*



### Conseils de programmation

**Organisez votre code avec des fonctions**

```python
def afficher_fond():
    screen.fill((0,0,0))
    screen.blit(fond, (0, 0))

def afficher_texte(message):
    texte = font.render(message, True, (255, 255, 255))
    screen.blit(texte, (0, 300))
```

<!--
Pour les élèves de term:

```python
def verifier_clic_objets(pos_souris):
    for objet in objets:
        if objet["rect"].collidepoint(pos_souris):
            return objet
    return None
```
-->


**Utilisez des dictionnaires pour vos objets**. 

Vous limiterez ainsi l'emploi de trop nombreuses variables:

```python
porte = {
        "nom": "porte",
        "image": door1,
        "x": 650,
        "y": 150,
        "largeur": 100,
        "hauteur": 200,
        "rect": rect1,
        "visible": True,
        "verrouille": True,
        "description": "Une porte en bois"
        }
cle =   {
        "nom": "clé",
        "image": cle,
        "x": rect3.center[0],
        "y": rect3.center[1],
        "largeur": 60,
        "hauteur": 27,
        "rect": rect3,
        "visible": False,
        "ramasse": False,
        "description": "Une clé dorée"
        }
...
```

**Définir un scénario à l'aide de diagrammes**

Dans les zones 1 et 2, placer les variables utiles au jeu. Placer les différents textes à afficher.

{{< img src="../images/zone3.png" >}}

Dans la zone 3, prevoir les interactions avec les différents objets, ainsi que la modification des variables:

{{< img src="../images/zone1.png" caption="Prévoir diagramme par objet ou par touche appuyée" >}}

Dans la zone 5, prévoir l'affichage du texte, ou le nouveau placement des objets/images.

Si vous utilisez un dictionnaire vous pouvez remplacer les variables `L`, `P`, `M` par exemple par `lampe["actionner"] = True/False`, `porte["verouille"] = True/False`, et `miroir["regarder"] = True/False`. Ce qui presente l'avantage d'être plus clair.


## Questions à se poser avant de commencer le TP

1. Quel est le scénario de mon escape game ?
2. Quels objets ou quelles zones de l'image seront cliquables ?
3. Quelles actions le joueur pourra-t-il faire ?
4. Comment savoir si le joueur a gagné ?
5. De quelles images ai-je besoin ?

**Bon courage pour votre projet !** 🎮

## Ressources utiles

- Documentation officielle Pygame : https://www.pygame.org/docs/
- Tutoriels vidéo : recherchez "Pygame tutorial" sur YouTube
- Exemples de code : https://github.com/pygame/pygame/tree/main/examples
- Chargement des images, format et transparence: [https://zestedesavoir.com](https://zestedesavoir.com/tutoriels/846/pygame-pour-les-zesteurs/1381_a-la-decouverte-de-pygame/5505_afficher-des-images/)

---
