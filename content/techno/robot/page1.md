---
Title: Robotique
description: microbit et robot maqueen
weight: 16
---


# Robot maqueen
## Prise en main du robot


![logo](../images//marq10.png)

*Programmer un robot a pour but de lui faire réaliser des tâches autonomes, répétitives. Il va prendre des décisions en fonction de son environnement grâce à un algorithme.*

La programmation se fera sur l'editeur [Vittascience.com](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom&toolbox=vittascience)

Selon la tâche à executer, il faudra bien distinguer les instructions que le robot n'execute qu'une seule fois, et celles qu'il devra répéter indéfiniment.

{{< img src="../images/marq12.png" caption="disposer les instruction dans le bon bloc de code" >}}

## Défi n°1: S'arrêter au parking
Le robot peut être prévu pour circuler selon une couleur marquée au sol.

{{< img src="../images/marq13.png" >}}




* les différentes fonctions d'**actions des moteurs** sont dans le menu *Robots* de la page de l'editeur [Vittascience.com](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom&toolbox=vittascience)

Le menu *Robots* propose les instructions de plusieurs robots. Le votre s'appelle **Maqueen**.

{{< img src="../images/selection.GIF" >}}



* **[Maqueen]** Contrôler le robot *avancer* vitesse *50*

{{< img src="../images/marq11.png" caption="la valeur de vitesse est un paramètre ajustable. Mettre 50" >}}

* **[Maqueen]** Arrêter le robot

{{< img src="../images/marq2.png" >}}

Dans le menu Entrees/Sorties, choisir le bloc *attendre 1 seconde-s*, et réaliser le programme suivant:


{{< img src="../images/marq17.png" >}}

> Tester ce premier programme avec le robot maqueen. Puis démarrer un nouveau projet pour stopper le robot dans une zone *noire*.

Pour ce défi: 

* Votre programme utilise une structure conditionnelle: retrouvez celle-ci dans le menu **logique**.

{{< img src="../images/marq14.png" >}}




Le robot dispose de 2 capteurs d'intensité lumineuse, sous le chassis. 

La mesure de l'**état du capteur de ligne**, sous le robot se fait grâce à la fonction:

* **[Maqueen]** Etat du capteur ligne *droit / gauche*

{{< img src="../images/marq8.png" >}}

Cette instruction renvoie un booléen (`True`, `False`), qui sera affectée à une variable. Créez 2 nouvelles variables, **G** et **D**.
{{< img src="../images/marq15.png" >}}

* Affecter les instructions des capteurs de ligne à chacune de ces variables:

{{< img src="../images/marq7.png" >}}

On place alors ces variables dans une structure conditionnelle (si G ET D faire...):

{{< img src="../images/marq6.png" caption="Si le capteur G vaut True et le capteur D vaut True: avancer" >}}



> à vous de jouer: Créez un programme qui fait avancer le robot tant qu'il est sur une piste **blanche**. Et qui s'arrête lorsqu'il est sur son *parking*, **noir**.

Vous avez reussi? 

* Sauvegardez le programme dans vos *documents*. 
* Et recopier le script sur votre cahier.

{{< img src="../images/marq16.png" >}}

## Défi n°2: Suivi de ligne
Le robot peut circuler en suivant une courbe peinte au sol.

{{< img src="../images/marq9.png" >}}

Une différence de clarté sous le robot (bord du chemin) permet de programmer un virage du robot.

Il faudra alors placer les instructions de commande du moteur Droit et Gauche dans une sequence d'intructions conditionnelles.

```
if
...
elif
...
else
```

Pour faire pivoter le robot, il faudra contrôler différement chaque moteur (Droit / Gauche). Utiliser: 

* **[Maqueen]** Contrôler le moteur *gauche* direction *...* vitesse *50*

{{< img src="../images/marq3.png" >}}


> à vous de jouer: Créer un deuxième programme qui fera:

> * tourner le robot vers la droite lorsqu'il se trouve dans la situation suivante:

{{< img src="../images/marq1.png" caption="blanc/noir => virage a droite" >}}

>* tourner vers la gauche dans la situation inverse
>* sinon: avancer tout droit lorsque les 2 capteurs mesurent la même couleur noire, ou blanche.

*Tester alors votre programme sur une piste circulaire.*

Votre robot fait le tour entierement? Vous avez relevé le **premier défi**!

> **Travail:** Recopier le script python dans un fichier `.txt`

*Aide*: [detection de la ligne noire](https://fr.vittascience.com/learn/tutorial.php?id=42/maqueen-part-3-suiveur-de-ligne-avec-micro-bit)

## Avant le défi n°3: Programmer en python
D'autres fonctions du robot peuvent être exploitées pour réaliser d'autres tâches. Par exemple:

* [Maqueen] Pivoter à *droite*

{{< img src="../images/marq41.png" >}}

* [Maqueen] Avancer d'une case

{{< img src="../images/marq51.png" >}}

Pour la suite, il sera utile de partir du programme réalisé avec les *blocs* (Vittascience), puis d'adapter, modifier certains paramètre *à la main*, directement dans le script python.

Vous devrez vous familiariser avec les instructions en python spécifiques au robot marqueen.

> Editeur [Vittascience.com](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom&toolbox=vittascience). Placer l'une des commandes du robot dans le bloc "Au demarrage". Et lire le script python généré.

> **Travail:** Copiez le contenu du document [maqueen.py](/scripts/robot/marqueen.py). Coller les instructions dans votre fichier `.txt`. Et complétez le avec les instructions python des différents blocs.

*Certaines commandes necessitent la declaration de fonctions, et occupent plusieurs lignes d'instructions.*

## Défi n°3: Avancer d'une case
Pour programmer les deplacements du robot indépendemment du marquage au sol, il sera necessaire de **calibrer** la longueur de ses deplacements.

{{< img src="../images/quadrillage.png" >}}

> Ouvrir un nouveau projet et mettre dans le bloc "Au demarrage", l'instruction "avancer d'une case". La longueur parcourue correspond-elle à la dimension d'une case sur le support? 

Les paramètres doivent être ajustés dans le script python (blocs inopérants pour ajustements). 

La longueur du deplacement dépend de la durée d'attente  `utime.sleep_ms(int(15e-2/speed_mps*1000))` dans la fonction `maqueen_moveWithSquare`.

> Passer en mode programmation python. Ne plus revenir sur l'interface avec les blocs. Modifier le script python et tester avec le robot. Quelle(s) modification(s) lui permet(ent) d'avancer d'une case sur le support?

De la même manière, il sera utile de calibrer l'angle de rotation lors de la commande de pivot à droite ou à gauche.

> **Travail:** Créer le programme qui permet au robot de suivre un chemin proposé, comme sur l'image plus haut. Utiliser une LISTE python comme structure de données pour placer les consignes de parcours (ex: `chemin = [1,1,1,2,1,1,2,1,1,3,1]`). Ce parcours doit utiliser les cases du support.

> Recopier le script dans votre fichier `.txt`

## Défi 4:  Enregister des données
L'enregistrement de données peut être utile pour calibrer les capteurs du robot.

{{< img src="../images/marq_us.png" >}}

Le programme suivant peut être chargé dans l'interface [Vittascience.com](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom&toolbox=vittascience). Télécharger le [fichier](/scripts/robot/robot_marquenn_us__202419_12120.py). Puis l'ouvrir  depuis l'interface.

* La fonction `getUltrasonicData` permet de mesurer une distance/un temps selon le paramètre `data`.
* Pour écrire des données sur la carte, ce sont les fonctions:
	* `log.set_labels`: definition des colonnes du tableau de mesure
	* `log.add` pour ajouter une entrée dans le tableau

On utilisera alors l'explorateur (windows) pour ouvrir et visualiser les données, dans un fichier d'extension `.html`

{{< img src="../images/data.png" >}}

```python
from microbit import *
import log
import utime
from machine import time_pulse_us

""" Maqueen robot """

# Ultrasonic TRIG on pin1
# Ultrasonic ECHO on pin2

def getUltrasonicData(trig, echo, data='distance', timeout_us=30000):
  trig.write_digital(0)
  utime.sleep_us(2)
  trig.write_digital(1)
  utime.sleep_us(10)
  trig.write_digital(0)
  echo.read_digital()
  duration = time_pulse_us(echo, 1, timeout_us)/1e6 # t_echo in seconds
  if duration > 0:
    if data == 'distance':
      #sound speed, round-trip/2, get in cm
      return 343 * duration/2 * 100
    elif data == 'duration':
      return duration
    else:
      raise ValueError("Data option '" + data + "' is not valid")
  else:
    return -1

log.set_labels('distance', timestamp=log.MILLISECONDS)
log.set_labels('temps', timestamp=log.MILLISECONDS)
i = 0

while True:
  if button_a.is_pressed():
    log.delete(full=True)
    i = 0
  utime.sleep(1)
  d = getUltrasonicData(pin1, pin2, 'distance')
  if d > 0:
    log.add(distance = d,temps = i)
    i = i + 1
  display.scroll(str(d), delay=150, wait=True)
```

Le format des données dans le fichier de *log* permet un traitement comme on le ferait pour un ficher *txt* ou *csv*.

## Suggestion de projets
* Piloter le robot à l'aide d'une telecommande: on utilisera une 2e carte microbit pour telecommande. Les données seront transmises grâce à la fonction [radio](/docs/techno/pages/MB_radio2/)
* Conduite autonome: le robot est capable d'avancer, et de s'arrêter seul lorsqu'il detecte un obstacle.
* Course déclenchée par un *clap*
* Evolution dans un labyrinthe
* Programme d'exploration type robot aspirateur
* Detection de formes (la forme de l'arêne dans laquelle est le robot)

Avec quelques extensions, les actions du robot peuvent être complexifiées (detection de couleur, ramassage d'objets, ...).


# Supports de tracés pour le robot
* Documents pdf pour le robot suiveur de ligne: [Lien vers pdf](/pdf/techno/suiveur_ligne.pdf)
* Exemple de courbe à imprimer en format [pdf](../images/courbe.pdf)
* Exemple de courbe en format photoshop [eps](../images/courbe.eps)

# Exemple de programmes sur Vittasciences.com
* Partie 1: [Présentation générale](https://fr.vittascience.com/learn/tutorial.php?id=40/maqueen-part-1-un-robot-motorise-avec-micro-bit)
* Partie 2: [Eviter les obstacles](https://fr.vittascience.com/learn/tutorial.php?id=41/maqueen-part-2-eviter-des-obstacles-avec-micro-bit)
* Partie 3: [detection de la ligne noire](https://fr.vittascience.com/learn/tutorial.php?id=42/maqueen-part-3-suiveur-de-ligne-avec-micro-bit)

# Liens 
* Editeur [Vittascience.com](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom&toolbox=vittascience)
* Detecteur d'obstacles [TP niveau entrée en 1ere NSI](http://michel.roemhild.free.fr/?Robot-Maqueen-detecteur-d-obstacle)
* Explorer, enregistrer des données sur la carte microbit: [Lien](https://microbit.org/fr/projects/make-it-code-it/environment-data-logger/)
* Course, tour de piste [site ac-nantes.fr](https://www.pedagogie.ac-nantes.fr/medias/fichier/challenge-robotmaqueen_1656062635314-pdf?ID_FICHE=1424110252680&INLINE=FALSE)
* Documentation [site ac-normandie.fr](https://nsi-snt.ac-normandie.fr/IMG/pdf/le_robot_maqueen.pdf)
* Documentation du robot Marqueen sur le site de l'[ac-normandie.fr](https://nsi-snt.ac-normandie.fr/IMG/pdf/le_robot_maqueen.pdf) 
* Le [programme suivant](/scripts/robot/robot_marqueen_5.py) montre un exemple de script pour *avancer d'une case*, et réaliser une mesure de distance (capteur US).




