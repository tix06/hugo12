---
Title : Exercices fonctions
hidden: true
---

# Exercices sur les fonctions

### Flash card 1

Voici le script d'une fonction avec paramètres : 

```python
def servir_sucre(client,nombre=0):
  """servir le nombre de sucre dans le café du client"""
  return '{} veut son café avec {} sucre(s)'.format(client,nombre)
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 14px">
      <h1>Passage d'arguments</h1>
      Que retourne la fonction dans les cas suivants?

      <ol>
      <li>servir_sucre('James')</li>
      <li>servir_sucre('Johanna',3)</li>
      </ol>
    </div>
    <div class="flip-card-back" style="font-size: 14px">
      <h1>Réponses</h1>
      <ol>
        <li>James veut son café avec 0 sucre(s)</li>
        <li>Johanna veut son café avec 3 sucre(s)</li>
      </ol>
    </div>
  </div>
</div>

### Flash card 2

```python
def calculeP(s, p):
  """calculer le pourcentage p d'une somme s"""
  return s * p / 100
```


<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>paramètres d'une fonction</h1>
      <p>Pour la fonction <i>calculeP</i> comment doivent être placés les arguments pour calculer 33% de la somme 500 euros?</p>
      <ol>
      <li>calculeP(500, 30)</li>
      <li>calculeP(500, 30)</li>
      <li>calculeP(500, 0.30)</li>
      <li>calculeP(0.30, 500)</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <p>Reponse 2.</p>
      <p>calcule_P(500, 30)</p>
    </div>
  </div>
</div>

### Flash card 3

Soit la liste L:

```python
L = [['Deuf', 'John', 'Vezuvio', '8']
    ['Fassol', 'Rémi', 'fruits de mer', '6']
    ['Niole', 'Guy', 'spéciale', '15']]
```

Et la fonction *cherche*:

```python
def cherche(m):
    for i in client:
        if i[3] == m:
            return i
    return "aucun élément trouvé"
        

```



<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>for et parcours de listes</h1>
      <p>On appelle la fonction <i>cherche</i> de la manière suivante:<br>
        cherche('6')
      </p>
Que retourne la fonction?
</p>
  <ol>
    <li>['Fassol', 'Rémi', 'fruits de mer', '6']</li>
    <li>6</li>
    <li>1</li>
    <li>'fuits de mer'</li>
    <li>"aucun élément trouvé"</li>
  </ol> 
    </div>
    <div class="flip-card-back">
      <h1>Réponse</h1>
['Fassol', 'Rémi', 'fruits de mer', '6']
    </div>
  </div>
</div>

### Flash card 4

La fonction ajoute(n,p) codée ci-dessous en Python doit calculer la somme de tous les entiers compris entre n et p (n et p compris).

Par exemple, ajoute(2,4) doit renvoyer 2+3+4 = 9

```python
def ajoute(n,p):
  somme = 0
  for i in range(.........):   # ligne à modifier
    somme = somme + i
  return somme
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 14px">
      <h1>Completer</h1>
      Que doit-on écrire dans la ligne marquée à modifier ?


    </div>
    <div class="flip-card-back" style="font-size: 14px">
      <h1>Réponses</h1>
      <code style="color:black">for i in range(n,p+1):</code><br>
      Lorsque <em>range</em> prend 2 arguments, l'itération se fait entre la premiere valeur, et la 2<sup>e</sup> valeur - 1
    </div>
  </div>
</div>

### Flash card 5
On souhaite utiliser la fonction `sin` du module `math`.

L'appel de la fonction diffère selon la méthode d'import du module. 







<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 14px">
      <h1>Importer des modules</h1>
      Dans chacun des cas suivants, quelle instruction faut-il écrire pour utiliser la fonction `sin` avec l'argument 3.14 ?

      <ol>
      <li>import math</li>
      <li>from math import sin</li>
      <li>import math as m</li>
      </ol>
    </div>
    <div class="flip-card-back" style="font-size: 14px">
      <h1>Réponses</h1>
      <ol>
      <li>math.sin(3.14)</li>
      <li>sin(3.14)</li>
      <li>m.sin(3.14)</li>
      </ol>
    </div>
  </div>
</div>




# Relire le cours
Lien vers la page :{{< a link="/docs/python/pages/fonctions/page1/" caption="fonctions" >}}

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
