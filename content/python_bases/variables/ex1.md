+++
title = "Exercices variables"
hidden = true
+++

# Exercices sur les variables et opérations

# Révisions : flash cards
1. Lire la question
2. Chercher la réponse
3. Cliquer sur la carte pour vérifier la reponse.

### Flash card 1
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>Questions 1</h1>
      <ol><li>Quels sont les principaux types élementaires de variables en informatique ?</li>
        <li>Comment fait-on pour affecter la valeur 3 à une variable a? </li>
        <li>Comment fait-on l'affectation multiple de la valeur 3 à la variable
        a et 55 à la variable b?</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol><li>Nombres (Integer et Float), Caractères (et chaines de caractères), Booléens (True, False)</li>
        <li><code style="color:black">a = 3</code></li>
        <li><code style="color:black">a, b = 3, 55</code></li>
      </ol>
    </div>
  </div>
</div>

### Flash card 2
<p>Soit le nombre N entier constitué de 3 chiffres A (centaines), B (dizaines), C (unités), s'écrivant ABC</p>

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>Questions 2</h1>
      <p style="font-size: 12px">Traduire chacune des propositions sous la forme d’une opération, en langage mathématique. </p>
      <ol style="font-size: 12px"><li>Le nombre doit être inférieur à 500</li>
        <li>son chiffre des dizaines est égal à la moitié du chiffre des centaines</li>
        <li>Le chiffre des unités est égal à la moitié du chiffre des dizaines</li>
        <li>La somme des 3 chiffres (centaines, dizaines, unités) est égal à 7</li>
      </ol>
      <p>Puis trouver le résultat</p>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol><li><code style="color:black">N < 500</code></li>
        <li><code style="color:black">B = A/2</code></li>
         <li><code style="color:black">C = B/2</code></li>
          <li><code style="color:black">A + B + C = 7</code></li>
      </ol>
      <p>Après résolution, il vient N = 421</p>
    </div>
  </div>
</div>

### Flash card 3


<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>Questions 3</h1>
      <ol><li>classer les nombres binaires constitués de 2 bits du plus petit au plus grand : 11  01  00  10</li>
        <li>Ecrire 19 (dix-neuf) en numération binaire</li>
        <li>Trouver combien fait  11111 (binaire) en base 10</li>
        <li>Convertir en Gbits le nombre : 400Mo</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol><li>00, 01, 10, 11</li>
        <li>10011</li>
        <li>31</li>
        <li>3,2 Gb (avec 1Go = 1000Mo) ou 3,1 Gb (1Go = 1024 Mo)</li>
      </ol>
    </div>
  </div>
</div>

### Flash card 4

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>Questions 4</h1>
      Que valent chacune des expressions suivantes ?
      <ol><li>3.12e-3</li>
        <li>3 / 4</li>
        <li>2**3</li>
        <li>5 // 4</li>
        <li>6 % 4</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol><li>0.00312 (l'evaluation du nombre renvoie un flottant)</li>
        <li>0.75</li>
        <li>8 (** est le symbôle pour exposant)</li>
        <li>1 (valeur entiere de la division)</li>
        <li>2 (module = reste de la division)</li>
      </ol>
    </div>
  </div>
</div>

### Flash card 5

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>Opérations sur les variables</h1>
      Que valent chacune des expressions suivantes ?
      <ol><li>("Pa"+"La") * 2</li>
        <li>str(4) * int("3") </li>
        <li>int("3") + float("3.2")</li>
        <li>True == False or not True == False</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol><li>'PaLaPaLa'</li>
        <li>l'expression vaut '4' * 3 donc affiche: 444'</li>
        <li>vaut 3 + 3.2 donc affiche 6.2</li>
        <li>True</li>
      </ol>
    </div>
  </div>
</div>

### Flash card 6

```
L = ['lundi', 'mardi',  'mercredi']
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>Listes</h1>
      Que valent chacune des expressions suivantes ?
      <ol><li>L[0]</li>
        <li>L[-1]</li>
        <li>L[1]</li>
        <li>L[-2]</li>
        <li>L[1 :]</li>
        <li>['lundi', 'mardi'] + ['mercredi', 'jeudi']</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol><li>'lundi'</li>
        <li>'mercredi'</li>
        <li>'mardi'</li>
        <li>'mardi'</li>
        <li>['mardi',  'mercredi']</li>
        <li>['lundi', 'mardi', 'mercredi', 'jeudi']</li>
      </ol>
    </div>
  </div>
</div>

### Flash card 7

```
L = ['lundi', 'mardi',  'mercredi']
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>Opérations sur les Listes</h1>
      Que vaut L après chacune des expressions suivantes ?
      <ol><li>L.append('jeudi')</li>
        <li>L.pop()</li>
        <li>L.insert(0, 'dimanche')</li>
        <li>L = L[1:]</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol><li>['lundi', 'mardi',  'mercredi', 'jeudi']</li>
        <li><p style="font-size: 12px">A partir de la liste précédente, on retire le dernier élément: ['lundi', 'mardi',  'mercredi']</p></li>
        <li>['dimanche', lundi', 'mardi',  'mercredi']</li>
        <li><p style="font-size: 12px">A partir de la liste précédente, on créé une nouvelle liste de l'élément d'indice 1 jusqu'au dernier: ['lundi', 'mardi',  'mercredi']</p></li>
      </ol>
    </div>
  </div>
</div>

### Flash card 8
```
L = [['a', 'b'], ['c', 'd'], ['e', 'f']]
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>Listes 2D</h1>
      Que valent chacune des expressions suivantes ?
      <ol><li>len(L)</li>
        <li>len(L[0])</li>
        <li>L[1]</li>
        <li>L[1][0]</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol><li>3 car la liste L comporte 3 éléments (des sous listes)</li>
        <li>2 car la liste L[0] comporte 2 éléments ('a' et 'b')</li>
        <li>['c', 'd']</li>
        <li>'c'</li>
      </ol>
    </div>
  </div>
</div>

### Flash card 9
```
tictactoe = [['X', 'O',  'O'],
             ['O', 'O',  'O'],
             ['O', 'O',  'X']]
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>Listes 2D</h1>
      Modifier la liste ?
      <ol><li>Quelle expression permet d'obtenir une diagonale de 'X'?</li>
        <li>Quelle expression permet d'obtenir une ligne de 'X' sur la premiere ligne?</li>
        <li>Quelle expression permet d'obtenir une ligne de 'X' sur la dernière ligne?</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol><li>L[1][1] = 'X'</li>
        <li>L[0] = ['X', 'X',  'X']</li>
        <li>L[-1] = ['X', 'X',  'X']</li>
      </ol>
    </div>
  </div>
</div>


# Relire le cours
Lien vers la page :{{< a link="/docs/python/pages/variables/page1/" caption="Variables" >}}

<script type="text/javascript" src="/scripts/flash_cards.js"></script>