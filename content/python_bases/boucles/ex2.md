---
Title : Exercices boucles
hidden: true
---

# Exercices sur les boucles
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

Script A 

```python
L1 = [1, 6, 9, 2, 10]

def cherche(L2, m):
    for i in range(len(L2)):
        if L2[i] == m:
            return i
    return "aucun élément trouvé"
        
cherche(L1, 6)
```



<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>for et parcours de listes</h1>
      <p>On execute la script A. Que retourne la fonction <i>cherche</i>?</p>
      <ol>
        <li>6</li>
        <li>1</li>
        <li>2</li>
        <li>"aucun élément trouvé"</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponse</h1>
      retourne 1, le rang de l'élément dont la valeur est 6. La fonction cherche va rechercher dans une liste L2 le rang de la valeur cherchée m.
      Si l'élément n'y est pas, la fonction retourne "aucun élément trouvé"
    </div>
  </div>
</div>


### Flash card 3

Script A : 

```python
i = 0
popu = [100, 90, 81, 74, 67, 60, 54, 49, 45, 40, 36, 33]
while popu[i] > 50:
  i += 1
print(i, popu[i])
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
        <li>affiche: 7 49</li>
      </ol>
    </div>
  </div>
</div>


### Flash card 4

Script B : 

```python
devoirs = ['math','physique','philo']
while devoirs != []:
    print('le devoir de {} est fait'.format(devoirs.pop()))
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
        <li>Ici le variant de boucle est la liste devoirs. Tant que celle-ci n'est pas vide, le programme continue: il affiche une phrase formatée avec le dernier élément. Celui-ci est aussitôt retiré de la liste.</li>
        <li>le devoir de philo est fait<br>
le devoir de physique est fait<br>
le devoir de math est fait<br></li>       
      </ol>
    </div>
  </div>
</div>

### Flash card 5

Script C : 

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
        <li>Que fait le script C?</li>
        <li>Qu'est-ce qui est affichée par le script C?</li>
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

### Flash card 8



<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>comprehension de listes</h1>
      
      <ol>
        <li>Que vaut u à la fin du script suivant ?<br>
        t = [1, 6, 8, 3, 21]<br>
        u = [x-2 for x in t]</li>
        <li>Que vaut v à la fin du script suivant ?<br>
t = [1, 2, 3, 4, 5]<br>
v = {x: x*3 for x in t}</li>
        <li>Que vaut w à la fin du script suivant ?<br>
t = [1,2,3,4,5,6,7,8,9]<br>
w = [c for c in t if c%3 == 0]</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol><li>[-1, 4, 6, 1, 19]</li>
        <li>{1: 3, 2: 6, 3: 9, 4: 12, 5: 15}</li>
        <li>[3, 6, 9]</li>
      </ol>
    </div>
  </div>
</div>

### Flash card 9


<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>comprehension de liste - suite</h1>
      <p><code>tab = [ ('Léa', 14), ('Guillaume', 12), ('Anthony', 16), ('Anne', 15) ]</code><br>
Quelle est la valeur de l'expression <br>[x[0] for x in tab if x[1]>=15] ?<br>
</p>
<p>
Choisir parmi les reponses : <br>
A- [('Anthony', 16), ('Anne', 15)]<br>

B- ['Anthony', 'Anne']<br>

C- [16, 15]<br>

D- TypeError : 'tuple' object is not callable<br>
</p>
     
    </div>
    <div class="flip-card-back">
      <h1>Réponse</h1>
Reponse B 
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