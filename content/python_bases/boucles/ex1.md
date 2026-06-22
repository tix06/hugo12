---
Title : Exercices boucles
hidden: true
---

# Exercices sur les boucles et listes
### Flash card 1

Script A

```python
for i in L : 
    print(i)
```

Script B 

```python
for i in range(len(L)) : 
    print(i)
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>for</h1>
      <p>La liste L est definie ainsi : <br>L = [‘P’,’I’,’Z’,’Z’,’A’]<br>
      Qu'affichent chacun des programmes suivants:</p>
      <ol>
        <li>script A</code></li>
        <li>script B</li>
     
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol>
        
        <li>P I Z Z A</li>
        <li>0 1 2 3 4</li>

       
      </ol>
    </div>
  </div>
</div>


### Flash card 2

Script A : 

```python
i = 0
popu = [100, 90, 81, 74, 67, 60, 54, 49, 45, 40, 36, 33]
while popu[i] > 50:
  i += 1
print(i)
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>while</h1>
      <p></p>
      <ol>
        <li>Que fait le script A?</li>
        <li>Quelle valeur est affichée par le script A?</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol>
        <li>Le variant de boucle i augmente tant que popu[i] est supérieur à 50. Lorsque i vaut 7, popu[7] vaut 49, on sort de la boucle
        <li>affiche: 7</li>
      </ol>
    </div>
  </div>
</div>

### Flash card 3

Script B : 

```python
devoirs = ['math','physique','philo']
i = 0
while i < 3:
    print('le devoir de {} est fait'.format(devoirs[i]))
    i = i + 1
```


<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>while</h1>
      <p></p>
      <ol>
        <li>Que fait le script B?</li>
        <li>Qu'est-ce qui est affichée par le script B?</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol>
        <li>Ici le variant de boucle i prend successivement les valeurs 0, 1, 2. le programme continue: il affiche une phrase formatée avec l'élément devoirs[i]. Puis lorsque i vaut 3, on sort de la boucle.</li>
        <li>le devoir de philo est fait<br>
le devoir de physique est fait<br>
le devoir de math est fait<br></li>       
      </ol>
    </div>
  </div>
</div>

### Flash card 4

Script C : 

```python
i = 10
while i >= 1:
    i -= 1
print(i)
```




<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>while</h1>
      <p></p>
      <ol>
        <li>Que fait le script C?</li>
        <li>Qu'est-ce qui est affichée par le script C?</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol>
        <li>La condition d'arrêt de la boucle while est réalisée lorsque i est inférieur (strict) à 1. Dans la boucle, on soustrait 1 à i, ce qui fait sortir de la boucle lorsque i vaut 0.</li>
        <li>affiche 0</li>       
      </ol>
    </div>
  </div>
</div>

### Flash card 5

Script D : 

```python
i = 10
while True:
    i -= 1
    if i < 1 : 
        break
print(i)
```




<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>while</h1>
      <p></p>
      <ol>
        <li>Que fait le script D?</li>
        <li>Qu'est-ce qui est affichée par le script D?</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol>
        <li>La condition d'arrêt de la boucle while n'est jamais réalisée, puisque celle-ci ne vaut jamais False. (while True). Cependant, dans la boucle, si i est inférieur à 1, l'instruction break fait sortir de la boucle.</li>
        <li>affiche 0</li>       
      </ol>
    </div>
  </div>
</div>


### Flash card 6


<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>while</h1>
      <p>Quelle est la valeur de la variable n à la fin de l'exécution du script ci-dessous ?:<br>
        n = 1<br>
while n != 20:<br>
... n += 2<br></p>
<p>
Choisir parmi les reponses : <br>
A- 1<br>
B- 20<br>
C- 22<br>
D- le programme ne termine pas, la boucle tourne indéfiniment
</p>
     
    </div>
    <div class="flip-card-back">
      <h1>Réponse</h1>
Reponse D : la variable n n'est jamais egale à 20, qui est la condition d'arrêt
    </div>
  </div>
</div>

### Flash card 7

On définit une liste L de 12 nombres entiers, de 1 à 12, mélangés : <br>


```
L = [12,4,5,1,3,2,6,7,8,11,10,9]
```


<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>algorithmes sur les listes</h1>
      <ol>
        <li>Quelle est la valeur de la variable m à la fin de l'exécution du script ci-dessous ?<br>
        m = L[0]<br>
        for j in range(len(L)):<br>
        ... if m < L[j]:<br>
        ...... m = L[j]<br>
        </li>
        <li>Que vaut alors la variable `j`?</li>
        <li>Quelle est l'étendue des valeurs prises par j, du debut à la fin de la boucle bornée ?</li>
        <li>Que vaut len(L)?</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
        <ol>
          <li>1 : la valeur minimum de la liste</li>
          <li>3 : la valeur min se trouve au rang 3</li>
          <li>j va de 0 à 11</li>
          <li>12</li>
    </div>
  </div>
</div>






# Relire le cours
Lien vers la page [boucles for et while](/docs/python/pages/boucles/page1/index.html)

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