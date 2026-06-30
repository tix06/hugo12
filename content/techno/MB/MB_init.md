---
Title : informatique des objets
description: presentation de la carte microbit
weight: 14
---



# Prise en main de la carte micro:bit: présentation
La carte microbit est un nano-ordinateur créé pour la promotion de la programmation dans l'éducation. Elle est très simple d'utilisation, mais peut également s'intégrer dans des applications complexes.

<blockquote class="twitter-tweet"><p lang="fr" dir="ltr">Gipsy est prête.{{< a link="https://twitter.com/hashtag/microbit?src=hash&amp;ref_src=twsrc%5Etfw" caption="" >}}
Elle possède dans sa version 2:

* un capteur de luminosité
* un acceleromètre/gyroscope
* un capteur de champ magnétique
* 2 boutons a/b
* un écran LED `5*5` 
* un mini haut-parleur
* un microphone
* antenne radio 2,4 GHz et bluetooth pour une communication entre cartes
* 3 entrées/sorties analogiques ou numeriques(0-3,3V), avec un courant de sortie limité à 200mA. Par défaut les broches sont configurées en sortie.

La programmation se fait depuis un navigateur web en Block Editor pour les débutants ou en langage MicroPython pour les utilisateurs plus expérimentés.
Le programme se télécharge depuis l'IDE en ligne et se copie simplement dans la micro:bit comme dans une clé USB (cordon USB vers micro-USB non inclus).

# Utiliser l'editeur en ligne python.microbit.org
Aller sur l'editeur à l'adresse suivante : [https://python.microbit.org/v/2.0](https://python.microbit.org/v/2.0)

{{< img src="../images/editoronline.png" >}}
1. Saisir le script dans la fenêtre d'edition.
2. Lui donner un nom (champ en haut à droite : *script name*).
3. Charger le programme sur le disque dur de l'ordinateur : *Download* (l'extension est .hex)
4. Deplacer le programme sur la carte microbit à l'aide de l'explorateur de fichiers.

# Utiliser l'editeur Mu
{{< img src="../images/helloworld.png" >}}
* Bouton **Mode** : <img src="../images/mu_mode.png" width="50px"> choisir l'editeur BBC microbit <img src="../images/mu_microbit.png" width="200px">
* Saisir le script dans la fenêtre de script.
* Faites une copie de votre script : <img src="../images/mu_save.png" width="50px">
* Une fois le microcontrôleur relié à l'ordinateur par le cable USB : bouton **Flasher** pour transferer le script. <img src="../images/mu_flash.png" width="50px">

L'editeur aide à la saisie grâce à l'autocompletion. Selectionner le mot en python et valider avec la touche *Enter* du clavier.

{{< img src="../images/autocompletion1.png" >}}
{{< img src="../images/autocompletion2.png" >}}
Lorsque l'on tape le nom d'une fonction qui est documentée, l'aide apparait à l'écran. C'est très utile pour savoir si la fonction prend des paramètres : 

{{< img src="../images/documentation.png" >}}
## gestion des erreurs de syntaxe
Une fois le programme chargé, il peut y avoir une erreur de syntaxe qui empêche son fonctionnement. Le message s'affiche sur l'écran de la carte microbit. Mais il peut être plus facile de lire ce message sur l'écran de l'ordinateur. Le bouton **REPL** fournit une console python avec affichage des messages à l'execution.

{{< img src="../images/repl.png" >}}
# Un premier programme `Hello World`
**Entrées/Sorties :**

La carte dispose d'un petit écran de LED qui peut servir de sortie et d'affichage. Elle est équipée de 2 boutons A et B pour intéragir.
Pour que le programme détecte l'appui sur les boutons, il faut surveiller l'état des boutons en permanence, avec une boucle non bornée `while True:`

On demarrera toujours le script avec l'import des librairies spécifiques à la carte micro:bit : `from microbit import *`, qui s'ajouteront aux librairies standart Python : 

```python
from microbit import *
# On cree une boucle infinie 
while True:
  if button_a.is_pressed(): 
    display.show(Image.HAPPY)
  else: 
    display.show(Image.SAD)
```

Ici, le programme affiche l'un ou l'autre des smileys, selon si le bouton A est pressé ou relâché.

{{< img src="../images/mu_happy.png" caption="smiley HAPPY" >}}
> Liste des images : [https://microbit-micropython.readthedocs.io/fr/latest/tutorials/images.html](https://microbit-micropython.readthedocs.io/fr/latest/tutorials/images.html)

<br>

## Affichage d'un texte
Si l'on veut afficher un texte, il sera préférable d'utiliser la fonction `scroll` à la place de `show`, afin de faire défiler les caractères sur l'écran de LED. 

*Exemple avec un texte :* ```display.scroll("Hello World")``` 

*Exemple avec la valeur d'une variable dt :* ```display.scroll(dt)``` 

## Affichage de formes
Ce script met en oeuvre une boucle bornée qui permet de parcourir les pixels (selon x ou y):

```python
# trace un trait horizontal (-)
from microbit import *
y=2
b=9
for x in range(5):
  display.set_pixel(x,y,b)
```
x,y : int, valeur de 0 à 4<br>
b : int, 0 à 9 (intensité lumineuse de la diode en x,y)

# Application: *Dessine ton LOGO* (SNT)
Lien vers {{< a link="/SNT/img_num/page3/" caption="l'énoncé en ligne" >}}

Lien vers le{{< a link="/pdf/SNT/TP_intro_MB.pdf" caption="Document pdf à rendre" >}}
{{< img src="../images/TP.png" >}}

# Application: *Capteur de luminosité* (1ere NSI)
Lien vers {{< a link="../MB_lumi/" caption="l'énoncé en ligne" >}}
# Application: *niveau à bulle 2D* (Term NSI)
Lien vers {{< a link="../MB_bulles/" caption="l'énoncé en ligne" >}}


# Liens
* Documentation micro:bit [microbit-micropython.readthedocs](https://microbit-micropython.readthedocs.io/en/v1.0.1/)
* Travaux pratiques: [microbit.org/make-it-code-it](https://microbit.org/projects/make-it-code-it/)
* Prise en main de la micro:bit avec des exemples [DANE Normandie ac-Caen](https://numerique-sciences-informatiques.discip.ac-caen.fr/IMG/pdf/initiation-mu-microbit.pdf)
* TP Reseaux : comment faire communiquer [deux cartes microbit par ondes radio](../MB_radio)
* Une autre approche de la communication reseau entre microbits : [l'exemple de la luciole](https://microbit-micropython.readthedocs.io/en/v1.0.1/tutorials/radio.html)