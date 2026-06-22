---
Title: multi-threading
hidden: true
---

# TP sur le parallélisme en Python
## Premier exemple: Execution séquentielle
Executer le programme suivant dans une cellule d'un notebook:

```python
def f1():
    for _ in range(5):
         print("Bonjour !")

def f2():
    for _ in range(5):
        print("Ca va ?")

if __name__ == "__main__" :
    f1()
    f2()
```

> Q1. Repérer l'ordre dans lequel les fonctions f1 et f2 sont executées. Décrire cet ordre.

## Création de threads
Un thread est un élément d'un processus qui va partager avec un programme l'espace des données et va s'exécuter de façon simultané avec d'autres thread. On parle aussi de processus légers. Ils peuvent aussi causer de multiples problèmes (interblocage).

Plusieurs threads peuvent exister dans le même processus. Ces threads partagent la mémoire et l’état du processus. En d’autres termes: ils partagent le code ou les instructions et les valeurs de ses variables.

```python
from threading import Thread
from time import sleep

def f1():
    for _ in range(5):
        print("Bonjour !")
        sleep(0.01)

def f2():
    for _ in range(5):
        print("Ca va ?")
        sleep(0.01)

if __name__ == "__main__" :
    p1 = Thread(target=f1)
    p2 = Thread(target=f2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
```

> Q2. Exécutez plusieurs fois ce nouveau code. Quelle différence constatez vous avec le code précédent ?

> Q3. Faire une recherche documentaire pour trouver la signification des instructions suivantes:

```
p1 = Thread(target=f1)
p1.start()
p1.join()
```

## Application au calcul parallèle
### Exemple simple
Le programme suivant, n'utilisant pas la notion de multi-tâches, permet d'incrementer un compteur de manière plutôt *originale*.

```python
from time import sleep

# Variable globale
compteur = 0 
limite = 100

def calcul():
    """Une fonction qui fait un calcul"""
    global compteur
    for c in range(limite):
        temp = compteur
        # simule un traitement nécessitant des calculs
        sleep(0.000000001)
        compteur = temp + 1

compteur = 0
calcul()
print(compteur)
```

> Q4. Quelle est la valeur affichée à la fin du programme. Expliquer son fonctionnement.

### Multi-threading
Les machines du Lycée peuvent supporter plusieurs *threads* (tâches) diférent-e-s, essayons alors avec le code suivant, pour gagner un facteur 4 dans notre temps de calcul :

```python
from threading import Thread
from time import sleep

# Variable globale
compteur = 0 
limite = 400

def calcul():
    """Une fonction qui fait un calcul"""
    global compteur
    for c in range(limite):
        temp = compteur
        # simule un traitement nécessitant des calculs
        sleep(0.000000001)
        compteur = temp + 1

compteur = 0
mesThreads = []
for i in range(4): # Lance en parallèle 4 exécutions de calcul
    p = Thread(target = calcul)
    p.start()      # Lance calcul dans un processus léger à part.
    mesThreads.append(p)

# On attend la fin de l'exécution des threads.
for p in mesThreads :
        p.join()

print(compteur)
print(mesThreads)
```

> Q5. Executer plusieurs fois le programme. Que constatez-vous? Quelle peut-être la raison? S'aider de l'image ci-dessous:

{{< img src="../images/thread1.png" caption="ressources partagées" >}}

## Fiabiliser l'algorithme Une solution : le verrou

Il est possible d'éviter que nos threads interfèrent les uns avec les autres : il suffit de s'assurer que la partie centrale qui incrémente notre compteur ne soit pas exécutée par 2 threads à la fois. Pour ce faire, on introduit la notion de verrou: un verrou peut être vu comme un témoin qui passe de thread en thread. Seul celui qui possède ce témoin peut exécuter l'incrémentation du compteur, les autres doivent attendre leur tour.

Ce verrou sera une variable globale du programme principal qui sera partagé entre les threads. Notre programme devient alors le suivant :

```python
from threading import Thread,Lock
from time import sleep

# Variable globale
compteur = 0 
limite = 100
verrou = Lock()

def calcul():
    """Une fonction qui fait un calcul"""
    global compteur
    for c in range(limite):
        # Début de la section critique
        verrou.acquire()
        temp = compteur
        # simule un traitement nécessitant des calculs
        sleep(0.000000001)
        compteur = temp + 1
        # fin de la section critique
        verrou.release()

compteur = 0
mesThreads = []
for i in range(4): # Lance en parallèle 4 exécutions de calcul
    p = Thread(target = calcul)
    p.start()      # Lance calcul dans un processus léger à part.
    mesThreads.append(p)

# On attend la fin de l'exécution des threads.
for p in mesThreads :
        p.join()

print(compteur)
```

> Q6. Tester ce nouveau programme. Conclure. Puis rechercher le rôle des instructions suivantes:

```
verrou.acquire()
verrou.release()
```

# Interblocage
## Premier exemple
Nous avons vu dans la partie précédente que les threads peuvent être une solution pour accélérer le traitement de données. Cependant cette pratique n'est pas sans risque, en particulier nous risquons un interblocage (deadlock en anglais):

```python
import threading, time
from random import randint

verrou1 = threading.Lock()
verrou2 = threading.Lock()

def f1() :
    time.sleep(randint(0,100)/100)
    verrou1.acquire()
    print("Zone risquée f1.1")
    verrou2.acquire()
    print("Zone risquée f1.2")
    verrou2.release()
    verrou1.release()

def f2() :
    verrou2.acquire()
    time.sleep(randint(0,100)/100)
    print("Zone risquée f2.1")
    verrou1.acquire()

    print("Zone risquée f2.2")
    verrou1.release()
    verrou2.release()


t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)

t1.start()
t2.start()
t1.join()
t2.join()
```

> Q7. Executer plusieurs fois le programme jusqu'à obtenir un *interblocage*. Expliquez alors, à partir des renseignements fournis par le programme ce qui a pu provoquer cet *interblocage*. Comment sort-on de ce *blocage*?

## Robot autonome?
{{< img src="../images/robot_mars.jpeg" caption="Le rover de la mission pathfinder" >}}


Le document suivant traite d'un *bug* informatique célèbre, du à un *interblocage*. Il s'agit ici de processus concurents et non de *threads*. Expliquer ce qu'il s'est produit à l'aide d'un diagramme que vous commenterez.

Le robot de la mission [Mars PathFinder](http://lycee.educinfo.org/index.php?page=interblocage&activite=processus)


# Liens
* TP issu de la page: [lycee educinfo](http://lycee.educinfo.org/index.php?page=creation_thread&activite=processus)



