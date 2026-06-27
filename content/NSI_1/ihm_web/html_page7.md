---
Title: Projet Falsk
hidden: true
---

* TP python-Flask pas à pas: [Lien](../html_page6)
* projet utilisant python-Flask: [Lien](../html_page7)


Les projets suivants utilisent le module **Flask**.
Vous travaillerez en groupe de 2, ou de 3 élèves. Vous choisirez l'un de ces 3 projets.

Pour **rendre votre projet**, vous pourrez, au choix:

* créer un **fichier** *zip* avec tous les dossiers et fichiers du projet et le mettre dans les *Documents* de votre session.
* le **publier** en ligne (Pythonanywhere.com)

Vous rendrez également un **fichier readme.txt** qui servira de compte-rendu de projet. Vous y préciserez les étapes de votre projet, ainsi que le rôle pour chacun des participants. Vous pourrez eventuellement utiliser la syntaxe markdown pour mettre le texte en forme.


# Projet 1: Boîte à secret
On veut créer une application web qui permette d'enregistrer des secrets protégés par des mots de passe.

{{< img src="../images/projet1.jpeg" >}}

1. Créer un *template* (un patron) appelé *index.html* contenant un formulaire permettant de spécifier un mot de passe et un message secret à enregistrer.
2. Créer une *vue* dans le fichier *main.py* qui servira la page *index.html* lorsque l'on se connecte au serveur (route `/`).
3. Créer un *template* *succes.html* qui affiche un message de reussite (voir plus loin), ainsi que le contenu d'une variable *message*.
4. Créer une *vue* dans le fichier *main.py* qui servira cette page *succes.html* lorsqu'on la demande. (route '/succes.html').
  * Cette vue servira la page *succes.html* qui affichera un message de succès, ainsi que le *message* si le mot de passe est correct. 
  * Sinon, la *vue* servira la page *echec.html*, qui affichera un message d'echec, ainsi qu'un bouton pour recommencer. 
  * Si le message est laissé vide par l'utilisateur, mais que le mot de passe est correct, la page *succes.html* affichera l'ancien message secret.


*Aide:*

Le programme utilise une variable globale qu'il faudra ajouter à la *vue* `succes`:

```python
@app.route('/succes',methods = ['POST'])
def result():
  global secret
  result = request.form
  ...
```


<!--

*Aide:*
On peut ajouter une classe Boite qui permet de stocker les variables de manière globale:

```python
class Boite:
    def __init__(self):
        self.nom = "admin"
        self.mdp = "1234"
        self.msg = "premier message"
```

Dans le programme principal, on ajoutera la ligne:

```python
a = Boite()
```

Le programme utilise alors 2 variables globales. Ces variables utilisent une notation pointée:

* **a.mdp** qui contient le mot de passe (celui-ci est 1234)
* **a.msg** qui contient le message dans la boite à secrets.

Pour comparer le mot de passe (dans la variable *motdepasse*) saisi par l'utilisateur avec celui de la boite à secret, on fait:

```python
if motdepasse == a.mdp:
  # instructions
```

Pour modifier le message *a.msg* de la boite à secret par un nouveau message (de la variable *message*), on fait:

```python
a.msg = message
```

4. *Pour aller plus loin (difficile):* on peut ajouter un nom de *login* en plus du mot de passe. Le serveur devra alors répondre:

  * **enregister le nom** si le nom n'existe pas, le mot de passe et le secret, et retourner la page *succes.py*
  * **message d'erreur** si le nom existe et que le mot de passe est incorrect.
  * **afficher le message** dans les autres cas.
-->



# Projet 2: Panier d'achat sans session
L'application que vous allez developper servira à gérer un panier d'achats sur un site de e-commerce.

{{< img src="../images/projet2.png" >}}
L'application utilise deux patrons (*templates*): `article.html` et `panier.html`.

Le premier, *article.html*, affiche la liste des articles. Un champs de formulaire permet de choisir, ou non, un (ou plusieurs) exemplaire(s) de chaque article.

Le deuxieme, *panier.html*, affichera le contenu du panier.

# Projet 3: Interroge un dictionnaire
Le site [https://dictionaryapi.dev/](https://dictionaryapi.dev/) permet d'acceder à un dictionnaire en ligne. Les requetes sont de la forme `https://api.dictionaryapi.dev/api/v2/entries/en/hello` si l'on souhaite par exemple consulter la definition du mot *hello* en langue anglaise.

{{< img src="../images/projet3.png" >}}
Pour utiliser l'API, il faut d'abord importer la librairie *[requests](https://fr.python-requests.org/en/latest/)*:

```python
import requests
```

Puis, utiliser les instructions:

```python
l = 'fr'
m = 'école'
url = 'https://api.dictionaryapi.dev/api/v2/entries/' + l + '/' + m
reponse = requests.get(url)
```

Le contenu de la reponse contient:

* un *header*, que l'on peut consulter avec: 

```
reponse.headers
```

* un status code que l'on peut consulter avec:

```
reponse.status_code
```

* la reponse en format json, que l'on peut consulter de la manière suivante:

```
definition = reponse.json()
print(definition)
```

Votre application Flask sera constituée de 2 patrons (*templates*): *index.html* et *definition.html*.

* Le premier fichier, *index.html*, contiendra un formulaire qui permettra de choisir la langue et le mot.
* Le deuxième fichier, *definition.html*, présentera le contenu de la definition, si la reponse du serveur *dictionaryapi.dev* retourne un `status_code` de 200.

## Que faire si le module `requests` ne fonctionne pas?
Il se peut que le module ne fonctionne pas avec l'installation du lycée.

Dans ce cas, vous pouvez ajouter la classe *dictionnaire* qui contiendra un unique mot, *bonjour*. 

**1.** Ajouter les lignes suivantes, juste après `app = Flask(__name__)`:

```python
app = Flask(__name__)

class dictionnaire:
    def __init__(self):
        self.headers = {'Server': 'nginx/1.18.0', 'Date': 'Mon, 06 Dec 2021 16:27:31 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '216', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'X-RateLimit-Limit': '450', 'X-RateLimit-Remaining': '449', 'X-RateLimit-Reset': '1638808183', 'Access-Control-Allow-Origin': '*', 'ETag': 'W/"d8-MHRbRl1KWQW5GmjcbqbJ8KqZwY4"', 'Vary': 'Accept-Encoding', 'Strict-Transport-Security': 'â\x80\x9cmax-age=15768000â\x80\x9d'}
        self.status_code = 200
        self.json = [{'word': 'bonjour', 'phonetics': [{}], 'meanings': [{'partOfSpeech': 'nom masculin', 'definitions': [{'definition': 'Souhait de bonne journée (adressé en arrivant, en rencontrant).', 'synonyms': ['salut'], 'antonyms': []}]}]}]
```

**2.** Ajouter la ligne `requete = dictionnaire()` juste avant `app.run(debug=True)`

**3.** Remplacer alors les 2 lignes 

```python
reponse = requests.get(url)
definition = reponse.json()
```

par : `reponse = requete.json`

**4.** Programmez enfin la vue dont la route est `/definition` afin de servir la page de la definition du mot *bonjour*, à condition que ce soit bien le mot demandé par le formulaire. Retourner *Page introuvable* sinon.






