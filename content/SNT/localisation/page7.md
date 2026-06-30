---
Title : TP trame NMEA
description: utiliser une app de geolocalisation sur smartphone pour telecharger la trame NMEA et l'analyser en langage python
hidden: true
weight: 18
---

# La trame NMEA
## Objectifs
Comprendre ce qu’est une trame NMEA : une **suite de caractères** mis dans un format particulier (normalisé) pour permettre un échange entre systèmes et logiciels. Exploiter la trame obtenue pour réaliser une carte personnalisée.
Manipuler une chaine de caractères. Extraire des informations.

## Principe 
Lorsqu’un récepteur GPS reçoit une information, il la transmet (au smartphone, à l’ordinateur auquel il est connecté, à l’interface gps de voiture) à l’aide d’une « phrase » dont la forme est strictement codifiée. On appelle cette « phrase » une trame.


{{< img src="../images/satellites.png" alt="satellites" caption="emission de signaux GPS" >}}
## Recuperez votre propre trame NMEA (partie qui ne sera pas traitée pendant la séance)
Travail personnel en amont : Si possible, installer l’application NMEA Tools sur votre smartphone sur Androïd ou NMEAGps sur iOS.
Selon le mobile utilisé, pour enregistrer une série de trames GPS, il faut faire : 
- Sur Android : *enregistrement* pour démarrer > attendre quelques secondes que le signal se stabilise > *enregistrement* pour arrêter > Choisir *Enregistrer* puis nommer le fichier votre_nom.txt
- Sur IOS iphone : attendre que la barre de détection de la position passe au vert puis > Bouton *log* en position *ON* pour démarrer > attendre quelques secondes que le signal soit enregistré > *log* pour arrêter > L’application propose alors de récupérer un fichier nmea.log dans une application (notes, ...) ou de le *partager*.

{{< img src="../images/tools.png" alt="appli NMEA-tools" caption="application NMEA-tools" >}}

## Que contient la trame NMEA ?
Parmi les différentes lignes constituant la trame, l'une d'entre elles débute par les symboles $GPGGA

Les données sont mises dans un format particulier expliqué ici : 

{{< img src="../images/exemple_trame.png" alt="exemple de trame" caption="extrait de trame NMEA" >}}
La valeur numérique recherchée est celle de la latitude et de la longitude du lieu : 


{{< img src="../images/detailNMEA.png" alt="extrait de trame" caption="detail de trame NMEA" >}}
Ces valeurs sont mises sous la forme **DDMM.MMMM** : 

lorsque l'on lit 4836.5375, la valeur doit être comprise comme  : 48°36,5375'

c'est à dire : 

- 48°
- 36,5375 minutes d'arc



# Travail
Ajoutez votre fichier nmea.log au dossier courant de votre fichier *python*. Ou bien, utilisez celle capturée par votre professeur, présente dans ce dossier.

### lecture du fichier nmea.log
Executer le script suivant


```python
fichier = open('images/nmea.log','r')

lignes = fichier.readlines() 
     
for i,ligne in enumerate(lignes):
                  
    if ligne !='\n':  #  tester si la ligne est non vide
        print('lignes['+ str(i)+'] \n'+ ligne)             
                 
fichier.close()                    

```

### Repérer la première ligne qui commence par `$GPGGA` 
- noter le numéro de ligne
- créer une variable `i` qui contiendra le numéro de la ligne


```python
i = 
```

- afficher la ligne extraite de la trame NMEA : `print(lignes[i])` 
- affecter `lignes[i]` à la variable `trame`


```python
print(lignes[..
trame = lignes[..
```

### sélectionner des caractères 
Une chaine de caractère peut être manipulée comme une liste en python. Ainsi, chaque caractère occupe un rang. Le premier caractère est le rang zero 0.

Pour extraire une série de caractères d'une variable, on ajoute [rang debut : rang fin+1] à la suite du nom de cette variable.

Par exemple : Pour extraire le nom 'boby' de la chaine `titre = 'boby joe roi des mers'`, on fait : 

```
titre = 'boby joe roi des mers'
titre[0:4]
```

Testez le : 
- executez la cellule suivante
- puis extraire 'joe' de la chaine `titre` en écrivant `print(titre[rang debut : rang fin+1]` (remplacer rang debut : rang fin+1 par des valeurs numériques)


```python
titre = 'boby joe roi des mers'
print(titre[..
```

### sélectionner les caractères de positionnement
**Selection de l'heure :**
On souhaite afficher les caractères relatifs à l'heure : 
On rappelle que le premier caractère `$` a le rang zero 0, le suivant `G` le rang 1, etc...



pour extraire l\'heure de la variable `trame` , on fait : `trame[7:16]` si les caractères relatifs à l'heure occupent les rangs 7 à 15. 
- afficher la variable `trame`
- Puis afficher `trame[7:16]` (ajuster eventuellement les bornes)


```python
print(trame)
trame[7:
```

### Selection de la latitude 
- dans la variable trame, calculer le rang des caractères que vous souhaitez extraire pour la latitude (N) :  
Procéder de la même manière que pour l'heure pour extraire cette fois les 9 caractères de la latitude contenus dans cette trame qui commencent par 43... : 


```python
trame[17:
```

- affecter alors ce resultat à la variable `latitude` 


```python
latitude = 
```


### longitude
Vous allez refaire le même travail pour la longitude. Dans la même cellule : 

* extraire les caractères de longitude de la variable `trame` à partir de leurs rangs, puis l'affecter à la variable `longitude` : faire `longitude = trame[debut:fin]` 
* afficher `longitude`

### marquer la position sur une carte
Pour ouvrir la carte du site openstreetmap, avec des coordonnées latitude (-25.175342) et longitude (31.563275), taper dans la barre URL du navigateur : 

```html
http://www.openstreetmap.org/?mlat=-25.175342&mlon=31.563275&zoom=15
```

> Il vous faudra modifier le format des valeurs numériques passées en paramètre. Les valeurs numériques doivent être exprimées en valeurs décimales.


# Liens 
document dont est extrait ce TP : [https://disciplines.ac-toulouse.fr/informatique/sites/informatique/files/fichiers/localisation/tramenmea_final_avecios.pdf](https://disciplines.ac-toulouse.fr/informatique/sites/informatique/files/fichiers/localisation/tramenmea_final_avecios.pdf)



