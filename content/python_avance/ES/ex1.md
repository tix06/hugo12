---
Title : Exercices Entrées Sorties
hidden: true
---

# Exercices sur les Entrées et Sorties

### Flash card 1

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>Print</h1>
      Comment compléter l'instruction suivante:<br>
      <code sytle="color:black">print('J\'ai {} freres et {} grande soeur qui a {} ans'.format(....))</code><br>
      <p>Pour afficher:</p>
      <p style="font-size: 14px">
      J'ai 2 freres et une grande soeur qui a 21 ans
    </p>
    </div>
    <div class="flip-card-back" style="font-size: 12px">
      <h1>Réponse</h1>
      <code style="color:black">print('J\'ai {} freres et {} grande soeur qui a {} ans'.format(2, 'une', 21)</code>
    </div>
  </div>
</div>

### Flash card 2

Soit le script suivant : 

```python
def somme(a,b):
  """ajoute 2 valeurs a et b"""
  return a + b

x = input('entrer un nombre : ')
y = input('entrer un 2e nombre : ')

print(somme(x,y))
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 14px">
      <h1>Input</h1>
      On lance le programme et on répond :<br>
      entrer un nombre : <b>12</b><br>
      entrer un 2e nombre : <b>13</b><br>
      <p>Qu'est ce qui est affiché après la saisie par l'utilisateur ?</p>
      <p>
        A- 25<br>
        B- '1213'
      </p>
    </div>
    <div class="flip-card-back" style="font-size: 12px">
      <h1>Réponse</h1>
      B- '1213'
      <p>les valeurs de x et y saisies par l'utilisateur seront de type <em>str</em><br>
        la fonction <em>somme</em> fait alors la concaténation des deux chaines.</p>
    </div>
  </div>
</div>

### Flash card 3
Le fichier `liste_francais.txt` contient des mots classés par ordre alphabetique, à raison d'un mot par ligne.

*Extrait :* 
```
abaisse
abaissement
abaisser
abandon
abandonnant
abandonne
...
```

Le script suivant permet de lire les données d'un fichier : 

```python
# initialisation de la liste vide
mots = []

# Lecture du fichier txt et remplissage de la liste
with open('liste_francais.txt', encoding='iso-8859-1') as f:
    for mot in f.read().splitlines():
        mots.append(mot)
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 14px">
      <h1>Lecture d'un fichier</h1> 
      <ol>
       <li>Que contient la variable mot ?</li> 
       <li>Que contient la variable mots ?</li> 
      </ol>
    </div>
    <div class="flip-card-back" style="font-size: 12px">
      <h1>Réponses</h1>
      <ol>
        <li>mot contient une ligne du fichier, c'est à dire l'un des mots</li>
        <li>mots est une liste où chaque élément est l'une des lignes du fichier, c'est à dire, chaque élément = un mot</li>
      </ol>
    </div>
  </div>
</div>

### Flash card 4
Le script suivant permet d'écrire dans un fichier et d'y mettre la liste `animaux2`:

```python
animaux2 = ["poisson", "abeille", "chat"]
with open("zoo2.txt", "w") as filout:
    for animal in animaux2:
         filout.write(animal)
```

Le problème est que, lorsquel'on ouvre le fichier, celui-ci contient: 

`poissonabeillechat`

et non : 

```
poisson
abeille
chat
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>Ecriture dans un fichier</h1> 
      <p>Quelle instruction faut il mettre à la place de la dernière ligne du script pour écrire les noms à la ligne, l'un sous l'autre, dans le fichier?
      </p>
      <p>
        A- filout.write("{}\n".format(animaux2))<br>
        B- filout.write("{}\n".format(animal))<br>
        C- filout.write("animal \n")<br></p>
    </div>
    <div class="flip-card-back" style="font-size: 12px">
      <h1>Réponse</h1>
      B- filout.write("{}\n".format(animal))<br>

    </div>
  </div>
</div>


### Flash card 5
On souhaite écrire la table de multiplication par 7 dans un fichier. Le contenu du fichier devrait ressembler à ceci : 

```
 1  7 
 2 14 
 3 21 
 4 28 
 5 35 
 6 42 
 7 49 
 8 56 
 9 63 
10 70 
```

Le debut du script qui doit permettre d'ecrire dans le fichier:

```python
with open("table_7.txt", "w") as filout:
    for y in range(1,11):
         filout.write(...a compléter...)
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>Ecriture dans un fichier</h1> 
      <p>Quelle instruction faut il mettre à la place de la dernière ligne du script pour écrire les valeur à la ligne, l'une sous l'autre, comme voulu?
      </p>
      
    </div>
    <div class="flip-card-back" style="font-size: 12px">
      <h1>Réponse</h1>
      <code style="color:black">filout.write('{:2} {:2} \n'.format(y,y*7))</code>

    </div>
  </div>
</div>

# Relire le cours
Lien vers la page :{{< a link="/docs/python/pages/ES/page1/" caption="Entrées/Sorties" >}}

<script>
let selector, cards, makeActive;
let elems = [];
var check = false;

selector = '.flip-card';

cards = document.querySelectorAll(selector);


makeActive = function () {
    /* attention petite erreur de script
    pour que ca fonctionne il faut un nombre impair de cartes
    */ 
    for (let i = 0; i < cards.length; i++){
      check=!check;
      //console.log(cards[i].childNodes[1].classList);
      elems[i] = cards[i].childNodes[1];
      elems[i].classList.remove('active');
      }
    if (check) {
    this.childNodes[1].classList.add('active');}
};

for (let i = 0; i < cards.length; i++)
    cards[i].addEventListener('mousedown', makeActive);
</script>