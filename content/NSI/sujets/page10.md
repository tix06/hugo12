---
Title: Arbres
description: arbre, parcours
weight: 77
---

# Arbres, parcours BFS (extrait 2024 centres etrangers J2, Ex 3)
{{% badge icon="star" %}}arbre{{% /badge %}} {{% badge icon="star" %}}parcours{{% /badge %}} 

## Partie B
On considère l’arborescence de fichiers de la figure suivante:


{{< img src="../images/page7_2.png" caption="arborescence fichiers" >}}
on propose
l’implémentation suivante. L’attribut fils est une variable de type list contenant tous
les dossiers fils. Cette liste est vide dans le cas où le dossier est vide.

```python
class Dossier:
	def __init__(self, nom, liste):
		self.nom = nom
		self.fils = liste # liste d'objets de la classe Dossier
```

1. Écrire le code Python d’une méthode `est_vide` qui renvoie `True` lorsque le
dossier est vide et `False` sinon.
2. Écrire le code Python permettant d’instancier une variable `var_multimedia` de
la classe Dossier représentant le dossier multimedia de la figure précédente. Attention :
cela nécessite d’instancier tous les nœuds du sous-arbre de racine multimedia.
3. Recopier et compléter sur votre copie le code Python de la méthode parcours
suivante qui affiche les noms de tous les descendants d’un dossier en utilisant l’ordre préfixe.

```python
def parcours(self):
	print(...)
	for f in ...:
		...
```

4. Justifier que cette méthode parcours termine toujours sur une arborescence
de fichiers.
5. Proposer une modification de la méthode parcours pour que celle-ci effectue
plutôt un parcours suffixe (ou postfixe).
6. Expliquer la différence de comportement entre un appel à la méthode `parcours`
de la classe Dossier et une exécution de la commande UNIX `ls`

On considère la variable `var_videos` de type Dossier représentant le dossier
videos de la figure précédente. On souhaite que le code Python
`var_videos.mkdir("documentaires")` crée un dossier documentaires vide
dans le dossier `var_videos`.

7. Écrire le code Python de la méthode `mkdir`.
8. Écrire en Python une méthode `contient(self, nom_dossier)` qui renvoie
`True` si l’arborescence de racine `self` contient au moins un dossier de nom
`nom_dossier` et `False` sinon.
9. Avec l’implémentation de la classe Dossier de cette partie, expliquer comment
il serait possible de déterminer le dossier parent d’un dossier donné dans une
arborescence donnée. On attend ici l’idée principale de l’algorithme décrite en
français. On ne demande pas d’implémenter cet algorithme en Python.
10. Proposer une modification dans la méthode `__init__` de la classe Dossier qui
permettrait de répondre à la question précédente beaucoup plus efficacement
et expliquer votre choix.