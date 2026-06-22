---
Title: solution tp chiffrement
hidden: true
---

*Solution pour le [TP chiffrement](../page54)*

```python
# dechiffrement
with open('texte_chiffre.txt','r') as f:
    texte = f.read()
    
fileout = open('texte_dechiffre.txt','w')
for c in texte:
    if c != "\\":
        rang = ord(c)
        fileout.write(chr(rang-1))
    else:
        fileout.write("\n")
fileout.close()

# en option
with open('texte_dechiffre.txt','r') as f3:
    texte = f3.read()
#texte
```

*Si vous rencontrez un problème avec l'encodage des caractères, utilisez cette version:*

*Solution pour le TP chiffrement*

```python
# dechiffrement
with open('texte_chiffre.txt','r') as f:
    texte = f.read()
    
fileout = open('texte_dechiffre.txt','w')
for c in texte:
    if c != "\\":
        try:
            rang = ord(c)
            fileout.write(chr(rang-1))
        except:
            # on ne parvient pas a encoder c
            # on l'ecrit sans decalage
            fileout.write(c)
    else:
        # on ecrit le retour a la ligne \n 
        # comme c'etait le cas
        fileout.write("\n")
fileout.close()

# en option
with open('texte_dechiffre.txt','r') as f3:
    texte = f3.read()
#texte
```