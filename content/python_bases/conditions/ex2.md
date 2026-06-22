---
Title : Exercices conditions
hidden : true
---

# Exercices sur les conditions

# Flash cards

## Flash card 1

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>tests conditionnels</h1>
      <p>On donne a = 10, b = 20, c = 30 : que retournent les opérations logiques en python :</p>
      <ol><li><code style="color:black">a + b >= c</code></li>
        <li><code style="color:black">b – a > c</code></li>
        <li><code style="color:black">(a < b) and (a < c)</code></li>
        <li><code style="color:black">(a < b) or (c < a)</code></li>
        <li><code style="color:black">not (a < b)</code></li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol><li><code style="color:black">True</code></li>
        <li><code style="color:black">False</code></li>
        <li><code style="color:black">True</code></li>
        <li><code style="color:black">True</code></li>
        <li><code style="color:black">False</code></li>
      </ol>
    </div>
  </div>
</div>

## Flash card 2

```python
voyelles = ['a','e','i','o','u','y']
laby = {'1':{'2':{'3':'9','5':'6'},'7':'8'}}
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>listes et dictionnaires</h1>
      <p>On dispose des 2 variables suivantes : <br>
        voyelles = ['a','e','i','o','u','y']<br>
        laby = {'1':{'2':{'3':'9','5':'6'},'7':'8'}}<br>
      Que retournent les opérations logiques en python :</p>
      <ol><li>a in voyelles</li>
        <li>type(voyelles) == list</li>
       <li>type(laby) == dict</li>
       <li>'1' in laby</li>
       <li>list(laby.keys()) == ['1','7']</li>
       <li>int(laby['1']['2']['5']) == 6
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol>
        <li>False</li>
        <li>True</li>
        <li>True</li>
        <li>True</li>
        <li>False # list(laby.keys()) vaut ['1']. laby ne contient qu'une seule clé et la valeur est {'2':{'3':'9','5':'6'},'7':'8'}</li>
        <li>False # c'est int(laby['1']['2']['5']) == 6 qui vaut True</li>
      </ol>
    </div>
  </div>
</div>

## Flash card 3

Script A : 

```python
if age < 18:
    print('entrée interdite en discotheque')
else : 
    print('entrez')
```

Script B : 

```python
if taille < 180:
    print('joueur de ping pong')
elif taille < 190:
    print('joueur de tennis')
else : 
    print('joueur de basket')
```

Script C : 
```python
if bouton_pressed :
  print('BOUM !')
else : 
  print('Rien')
```


<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>if - else</h1>
      <p>Quelle valeur est affichée par chacun des scripts suivants:</p>
      <ol>
        <li>script A avec <code style="color:black">age = 19</code></li>
        <li>script B avec <code style="color:black">taille = 195</code></li>
        <li>script C avec <code style="color:black">bouton_pressed = False</code></li>

      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol><li>entrez</li>
        <li>joueur de basket</li>
        <li>Rien</li>
      </ol>
    </div>
  </div>
</div>

# Relire le cours
Lien vers la page [structures conditionnelles](/docs/python/pages/conditions/page1/index.html)

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