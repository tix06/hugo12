---
Title: tuto requests
description: application des connaissances sur le protocole HTTP, données open source, creer une app en python utilisant des requetes en temps reel
weight: 13
---

# Module request
Le module `requests` de python permet de recuperer les données d'une requete HTTP dans un format exploitable (dict,list).

La communication avec le serveur demande d'utiliser une clé, que vous devrez générer en [créant un compte](https://home.openweathermap.org/users/sign_up). (API key). 

## Données météo open source
L'exemple suivant traite de l'exploitation d'une requete sur le site [OpenWeatherMap](https://home.openweathermap.org/users/sign_up). Le compte gratuit permet de realiser quelques requetes, en nombre raisonnable, et sera suffisant pour developper un petit projet NSI. 

*Voici le script minimal*

```python
import requests,json,sys

APPID ='-- a remplacer par votre cle API et placer entre les guillemets--'
#location = 'London,GB'
location = 'Nice,FR'

#Download the JSON data from OpenWeatherMap.org's API.

url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={APPID}'
response = requests.get(url)
response.raise_for_status()

#Uncomment to see the raw JSON text:
#print(response.text)

#Load JSON data into a Python variable.
weatherData = json.loads(response.text)

#Print weather descriptions

w = weatherData
print(f'Current weather in {location}')
print(w['weather'][0]['main'],'-',w['weather'][0]['description'])
print()
```



*Prolongement:* Pour obtenir les prévisions sur plusieurs jours, utiliser la requete:

```python
url=f'https://api.openweathermap.org/data/2.5/forecast?q={location}&cnt=3&appid={APPID}'
```

Le traitement va alors différer, car la météo des différents jours sera placée dans la clé `list` du dictionnaire `weatherData`.

## En-tête HTTP
Avec l'architecture reseau d'un lycée, le logiciel proxy va filtrer les requêtes, et empêcher de lancer celles-ci depuis un script python. Cela peut constituer une *faille de sécurité*.

L'en-tête HTTP va comporter une signature du client, et le proxy va distinguer un navigateur d'un IDE python.

On peut vouloir modifier l'en-tête HTTP pour imiter le comportement d'un navigateur. 

| Paramètre |	Valeur par défaut  (requests)| Valeur "Navigateur" (à imiter) |
|--- |--- |--- |
| User-Agent |	python-requests/x.x	| Mozilla/5.0 ... Chrome/... |
| Accept|	`*/*` 	|text/html, ... |
| Accept-Language	| (Absent)	| fr-FR, fr;q=0.9 |
| Signature TLS	| Bibliothèque Python |	Moteur Blink/WebKit (Chrome/Firefox) |

Voici adaptation du script que l'on peut alors utiliser depuis le lycée.

```python
import requests,json,sys

# 1. Définir les en-têtes pour imiter Chrome (Windows 10/11)

headers={
'accept':
'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'accept-encoding':'gzip, deflate, br, zstd',
'accept-language':'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'connection':'keep-alive',
'host':'api.openweathermap.org',
'sec-ch-ua':'"Chromium";v="148", "Microsoft Edge";v="148", "Not/A)Brand";v="99"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'document',
'sec-fetch-mode':'navigate',
'sec-fetch-site':'none',
'sec-fetch-user':'?1',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0'
}

# 2. Ajouter les adresses de connexion au proxies (completer les champs)
# id = votre identifiant IACA
# password = votre password IACA

proxies = {
    "http": "http://id:password@ip_proxy:port",
    "https": "http://id:password@ip_proxy:port",
}

try:
    # 3. Envoyer la requête avec les en-têtes "masqués"
    APPID ='02cbe3cb547ddf63a866b3b9679daffe'
    #location = 'London,GB'
    location = 'Nice,FR'

    #Download the JSON data from OpenWeatherMap.org's API.

    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={APPID}'
    response = requests.get(url,headers=headers,proxies=proxies,timeout=10)
    response.raise_for_status()



    #Uncomment to see the raw JSON text:
    #print(response.text)

    #Load JSON data into a Python variable.
    weatherData = json.loads(response.text)

    #Print weather descriptions

    w = weatherData
    print(f'Current weather in {location}')
    print(w['weather'][0]['main'],'-',w['weather'][0]['description'])
    print()


except Exception as e:
    print(f"Erreur : {e}")
```

<!--
Un exemple de clé APPID que vous pouvez utiliser *provisoirement*, avant de créer la votre: `02cbe3cb547ddf63a866b3b9679daffe`
et d'adresse proxy:
"http://id_IACA:password_IACA@10.66.91.4:3128"
-->

