---
Title : codage exercices
hidden: true
---

# Exercices sur le codage des valeurs

### Flash card 1



<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 13px">
      <h1>Binaire</h1>
      <p>Convertir de decimal à binaire ou binaire à decimal:</p>
      <ol>
        <li>Convertir 15 en binaire</li>
        <li>Convertir 21 en binaire</li>
        <li>Convertir 129 en binaire</li>
        <li>Convertir 1110 en decimal</li>
        <li>Convertir 1100 1100 en decimal</li>
     
      </ol>
    </div>
    <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol>
        
        <li>1111</li>
        <li>10101</li>
        <li>1000 0001</li>
        <li>14</li>
        <li>204</li>
      </ol>
    </div>
  </div>
</div>

### Flash card 2

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 13px">
<h1>Addition binaire</h1>
<p>Ajouter les nombres binaires suivants :</p>
<ol>
<li>0010 0101 + 1</li>
<li>111 + 1</li>
<li>0010 1111 + 1</li>
<li>0111 1111 + 1</li>

</ol>
</div>
<div class="flip-card-back">
<h1>Réponses</h1>
<ol>
<li>0010 0110</li>
<li>1000</li>
<li>0011 0000</li>
<li>1000 0000</li>
</ol>
    </div>
  </div>
</div>

### Flash card 3
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 13px">
<h1>Conversions binaires</h1>
      <p>Convertir en octets (<b>valeurs approchées</b>):</p>
      <ol>
      <li>500 bits</li>
      <li>100 Mb</li>
      <li>125 ko</li>
      <li>1 Go</li>


      </ol>
    </div>
      <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol>
        <li>500/8 = 62.5</li>
        <li>100*10<sup>6</sup>/8 = 1.25*10<sup>7</sup></li>
        <li>125*10<sup>3</sup></li>
        <li>10<sup>9</sup></li>
      </ol>
    </div>
  </div>
</div>

### Flash card 4

On peut vouloir convertir les données avec des valeurs **exactes** et non approchées. Pour eviter les confusions avec le kilobit, on utilise un autre nom pour l'unité : le **Kibibit (Kibit)**, qui vaut **1024 bits** (soit 2<sup>10</sup>). 

Les multiples de l'octet deviennent: Kibioctet (Kio), Mébioctet (Mio), Gibioctet (Gio), Tébioctet (Tio), Pébioctet (Pio).

Le tableau de convertion est alors le suivant : 

| unité | valeur exacte, en octets |
|--- | --- |
| Kibioctets (Kio) | 2<sup>10</sup> |
| Mébioctet (Mio) | 2<sup>20</sup> |
| Gibioctet (Gio) | 2<sup>30</sup> |
| Tébioctet (Tio) | 2<sup>40</sup> |
| Pébioctet (Pio) | 2<sup>50</sup> |

<br>

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 13px">
<h1>Conversions binaires</h1>
      <p>Convertir en octets (<b>valeurs exactes</b>)</p>
      <ol>
      <li>10 Kibibits</li>
      <li>100 Mebibits</li>
      <li>125 Kibioctets</li>
      <li>1 Gibioctet</li>


      </ol>
    </div>
      <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol>
        <li>10 * 1024 /8 = 1280</li>
        <li>100*1024*1024/8 = 1.31*10<sup>7</sup></li>
        <li>125*1024 = 1.28*10<sup>5</sup></li>
        <li>2<sup>30</sup> = 1.07*10<sup>9</sup></li>
      </ol>
    </div>
  </div>
</div>

### Flash card 5
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front" style="font-size: 13px">
<h1>mot-binaire</h1>
      <p>Combien de valeurs peuvent être codées en :...</p>
      <ol>
      <li>4 bits</li>
      <li>8 bits</li>
      <li>32 bits</li>
      <li>64 bits</li>



      </ol>
    </div>
      <div class="flip-card-back">
      <h1>Réponses</h1>
      <ol>
        <li>2<sup>4</sup> = 16</li>
        <li>2<sup>8</sup> = 256</li>
        <li>2<sup>32</sup> = 4.29*10<sup>9</sup></li>
        <li>2<sup>64</sup> = 1.84*10<sup>19</sup></li>
      </ol>
    </div>
  </div>
</div>


# Relire le cours
Lien vers la page [Données: du comptage au calcul mécanique](/docs/NSI_1/donnees/page1)

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