---
Title: somme et moyenne sur Excel
weight: 17
---

**Tableur Excel**

# Construire une formule de calcul de moyenne

## Fonction somme
Pour programmer la fonction *SOMME* sur les valeurs d'une colonne du tableau

Voici un lien vers le [tuto de microsoft office.](https://support.microsoft.com/fr-fr/office/somme-somme-fonction-043e1c7d-7726-4e80-8f32-07b23e057f89)

> * cliquer dans la cellule juste sous la dernière valeur de la colonne. 
* Ecrire debut de la formule (*bien commencer la ligne par le signe `=`*): `= SOMME(` 
* puis faire une **sélection étendue** de toutes les valeurs de la colonne. (*voir image ci-dessous*)
* Valider avec la touche *Entrer*


{{< img src="../images/gimp4.png" >}}

## Compter le nombre de cellules
Pour compter le nombre de valeurs dans le tableau, utiliser la fonction `NOMBRE`

Voir ici la [liste de fonctions excel possibles](https://support.microsoft.com/fr-fr/office/m%C3%A9thodes-de-comptage-des-cellules-dans-une-plage-de-donn%C3%A9es-dans-excel-3e0b3b7a-e0e4-478a-a940-889400120072#:~:text=S%C3%A9lectionnez%20la%20cellule%20dans%20laquelle,les%20cellules%20contenant%20des%20nombres.)

> * cliquer dans une cellule vide de la colonne. 
* Ecrire debut de la formule (*bien commencer la ligne par le signe `=`*): `= NOMBRE(` 
* puis faire une **sélection étendue** de toutes les valeurs de la colonne.
* Valider avec la touche *Entrer*

## Calculer la moyenne
La moyenne des valeurs se calcule en divisant le résultat de SOMME par celui de NOMBRE. 

Supposons que la somme se trouve dans la cellule D18, et le nombre dans D19, alors il faudra calculer avec la formule:

`=D18/D19`

Placer cette formule dans une cellule libre de la feuille de calcul, si possible sous les autres valeurs

{{< img src="../images/excel_moy.png" >}}

*Cette formule est DYNAMIQUE: si vous modifiez une valeur dans le tableau, tout est recalculé. Vous avez créé une tâche AUTOMATISEE.*