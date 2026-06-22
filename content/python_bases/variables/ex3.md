+++
title = "Exercices séquences 2"
hidden = true
+++

# Exercices sur les séquences et boucles

# Révisions : flash cards
1. Lire la question
2. Chercher la réponse
3. Cliquer sur la carte pour vérifier la reponse.

### Flash card 1
Soit le programme 1 suivant:

```python
L = ['a','b','c']
for i in L:
  print(i)
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>Questions 1 (QCM)</h1>
      Quelles valeurs successives prend le variant de boucle <b>i</b> ? (une seule bonne reponse)
      <ol><li>0, 1, 2</li>
        <li>1, 2, 3 </li>
        <li>'a', 'b', 'c'</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponse</h1>
      <ul><li>3: 'a', 'b', 'c'</li>
      </ul>
    </div>
  </div>
</div>

### Flash card 2
Soit le programme 2 suivant:

```python
L = ['a','b','c']
for i in range(len(L)):
  print(i)
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>Questions 2 (QCM)</h1>
      Quelles valeurs successives prend le variant de boucle <b>i</b> ? (une seule bonne reponse)
      <ol><li>0, 1, 2</li>
        <li>1, 2, 3 </li>
        <li>'a', 'b', 'c'</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponse</h1>
      <ul><li>1: 0, 1, 2</li>
      </ul>
    </div>
  </div>
</div>

### Flash card 3

Soit le programme 3 suivant:

```python
L = ['a','b','c']
for i in range(len(L)):
  print(L[i])
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>Questions 3 (QCM)</h1>
      Qu'est ce qui est affiché dans la console python ? (une seule bonne reponse)
      <ol><li>0, puis 1, et 2</li>
        <li>1, puis 2, et 3 </li>
        <li>'a', puis 'b', et 'c'</li>
        <li>'c', puis 'b', et 'a'</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponse</h1>
      <ul><li>3: 'a', 'b', 'c'</li>
      </ul>
    </div>
  </div>
</div>

### Flash card 4

Soit le programme 4 suivant:

```python
L = ['a','b','c']
for i in range(len(L)):
  print(L[len(L)-1-i])
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>Questions 4 (QCM)</h1>
      Qu'est ce qui est affiché dans la console python ? (une seule bonne reponse)
      <ol><li>0, 1, 2</li>
        <li>1, 2, 3 </li>
        <li>2, 1, 0</li>
        <li>'a', 'b', 'c'</li>
        <li>'c', 'b', 'a'</li>
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponse</h1>
      <ul><li>5: 'c', 'b', 'a'</li>
      </ul>
      <p>En effet le variant de boucle <b>i</b> prend les valeurs 0, 1, 2<br>
        Alors len(L) vaut 3, et len(L)-1-i prend les valeurs:<br>
        3-1-0 = 2, puis 3-1-1 = 1, et 3-1-2 = 0<br>
      Et L[len(L)-1-i] prend alors les valeurs 'c', 'b', 'a'</p>
    </div>
  </div>
</div>

### Flash card 5

Soit le programme 5 suivant qui construit une liste par compréhension:

```python
L = [i * 3 for i in range(6)]
```

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h1>Questions 5 </h1>
      Que vaut la liste L?
    </div>
    <div class="flip-card-back">
      <h1>Réponse</h1>
      <ul><li>[0, 3, 6, 9, 12, 15]</li>
      </ul>
      Car <b>i</b> prend les valeurs 0 à 5 (compris).<br>
      Et la liste est construite à partir des éléments 3*i
    </div>
  </div>
</div>


### Flash card 6

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 14px">
      <h1>Questions 6</h1>
      Quel est l&lsquo;affichage dans la console au fur et à mesure des instructions suvantes ?
      <ol><li>voyelles = ['a','e','i','o']<br>
      voyelles[1]
      </li>
        <li>voyelles[-2]</li>
        <li>voyelles.pop()<br>voyelles</li>
        <li>voyelles.append('u')<br>voyelles</li>
        
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol><li>'e'</li>
        <li>'i'</li>
        <li>'o'<br>['a','e','i']</li>
        <li>['a','e','i','u']</li>
        
      </ol>
    </div>
  </div>
</div>

### Flash card 7

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 12px">
      <h1>Questions 7</h1>
      Quel est l&lsquo;affichage dans la console au fur et à mesure des instructions suvantes ?
      <ol><li>capitales = {'France':'Paris',\<br>'Italie':'Rome',\<br>'Angleterre':'Londres'}
<br>list(capitales.keys())</li>
        <li>capitales['France']</li>
        <li>list(capitales.values())</li>
        <li>capitales['Espagne']='Madrid'<br>list(capitales.items())</li>

      </ol>
    </div>
    <div class="flip-card-back" style="font-size: 12px">
      <h1>Réponses</h1>
      <ol><li>['France', 'Italie', 'Angleterre']</li>
        <li>'Paris'</li>
        <li>['Paris', 'Rome', 'Londres']</li>
        <li>[('France', 'Paris'),<br>
 ('Italie', 'Rome'),<br>
 ('Angleterre', 'Londres'),<br>
 ('Espagne', 'Madrid')]</li>
      </ol>
    </div>
  </div>
</div>

# Relire le cours
Lien vers la page :{{< a link="/docs/python/pages/variables/page1/" caption="Variables" >}}

<script type="text/javascript" src="/scripts/flash_cards.js"></script>