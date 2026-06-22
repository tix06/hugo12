+++
title = "Exercices séquences"
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
        <li>'444'</li>
        <li>6.2</li>
        <li>True</li>
      </ol>
    </div>
  </div>
</div>

### Flash card 2
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

### Flash card 3
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

### Flash card 4
Soit la liste **T** suivante:

```python
T = [('A',1),('B',2),('C',3)]
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>méthodes de listes</h1>
      Que vaut la liste T après chacune des instructions suivantes, réalisées l'une après l'autre?
      <ol><li><code>T.append(('D',4))</code></li>
        <li><code>T.insert(1,('E',5))</code></li>
        <li><code>T.pop()</code></li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol><li>[('A', 1), ('B', 2), ('C', 3), ('D', 4)]</li>
        <li>[('A', 1), ('E', 5), ('B', 2), ('C', 3), ('D', 4)]</li>
        <li>[('A', 1), ('E', 5), ('B', 2), ('C', 3)]</li>
      </ol>
    </div>
  </div>
</div>

### Flash card 5
Script 1

```python
a = 4
b = a
b = b +4
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>copie d'une variable nom mutable</h1>
      <p>
      A la fin du script 1:</p>
      <ol><li>quelle est la valeur de b?</li>
        <li>quelle est la valeur de a?</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol>
        <li>b vaut 8</li>
        <li>a vaut 4 car b est une copie par valeur. Modifier b ne change pas la valeur de a</li>
      </ol>
    </div>
  </div>
</div>

Script 2

```python
L1 = [1,2,3]
L2 = # ... à compléter
L2.append(4)
# L2 vaut [1,2,3,4]
# L1 n'est pas modifiée
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>copie d'une liste</h1>
      <p>
      Comment compléter la ligne 2 du script 2 pour copier la liste L1 dans L2 par valeur?</p>
      <ol><li><code>L2 = list(L1)</code></li>
        <li><code>L2 = L1[:]</code></li>
        <li><code>L2 = L1</code></li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol>
        <li>VRAI</li>
        <li>VRAI</li>
        <li>FAUX: copie par reference</li>
      </ol>
    </div>
  </div>
</div>

### Flash card 6
Soit la liste L suivante:

```python
L = [9, 5, 1, 3, 4]
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>trier une liste</h1>
      Pour trier la liste L, quelle instruction faut-il écrire?
      <ol><li><code>L.sort()</code></li>
        <li><code>L.sorted()</code></li>
        <li><code>choice(L)</code></li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol><li>VRAI</li>
        <li>FAUX. sorted(L) est la bonne syntaxe et va retrourner une liste triée à partir des valeurs de L, mais ne modifie pas L</li>
        <li>FAUX. Cette instruction permet de choisir une valeur parmi celles de L</li>
      </ol>
    </div>
  </div>
</div>




### Flash card 7
Soit le dictionnaire D suivant:

```python
D = {'nom':'Nicaise', 'prenom': 'Martine'}
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>methodes de Dictionnaire</h1>
      Que font chacune des instructions suivantes?
      <ol><li><code>list(D.keys())</code></li>
        <li><code>list(D.values())</code></li>
        <li><code>list(D.items())</code></li>
        <li><code>D['age'] = 12</code></li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol><li>['nom', 'prenom']</li>
        <li>['Nicaise', 'Martine']</li>
        <li>[('nom', 'Nicaise'), ('prenom', 'Martine')]</li>
        <li>créé un nouvel élément dans D:<br>
          {'nom': 'Nicaise', 'prenom': 'Martine', 'age': 12}
        </li>
      </ol>
    </div>
  </div>
</div>


### Flash card 8
Script 3

```python
[i**2 for i in range(5) if i**2 %2 ==0]
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>comprehension de listes</h1>
      <p>
      Quelle liste obtient-on avec l'instruction du script 3?</p>
      <ol><li><code>[0, 2, 4, 6, 8, 10]</code></li>
        <li><code>[0, 4, 16, 32, 64]</code></li>
        <li><code>[0, 4, 16]</code></li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      3. [0, 4, 16]
    </div>
  </div>
</div>


# Relire le cours
Lien vers les pages : 

*{{< a link="/docs/python/pages/variables/page1/" caption="Variables" >}}* [methodes associées aux sequences: list, dict](/docs/python/pages/variables/page2/)


<script type="text/javascript" src="/scripts/flash_cards.js"></script>