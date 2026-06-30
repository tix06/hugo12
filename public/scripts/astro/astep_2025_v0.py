import os
import csv
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor


def lister_le_dossier(D):
	"""D est une liste de dossiers
	le dossier au rang 0 est le parent"""
	for i in range(1,len(D)):
		print(i,'. ',D[i])

def lister_les_fichiers(D):
	"""D est une liste de fichiers
	on commence la numerotation par 1"""
	for i in range(len(D)):
		print(i+1,'. ',D[i])

def changer_de_dossier(D,i):
	if i >= 1:
		os.chdir(D[i])
		D = [D[i]]
	else:
		# i = 0
		# on reconstruit D avec le parent pour i=0
		os.chdir(D[0])
		D = [os.path.dirname(D[0])]

def importer_datas(fichier):
    table = []
    with open(fichier, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            try:
                line_values = []
                for val in row:
                    val = float(val)
                    line_values.append(val)
            except:
                line_values = row
            table.append(line_values)
    
    x = []
    y = []
    for i in range(len(table[1:])-1):
        x.append(table[i+1][0])
        y.append(table[i+1][1])
    return x,y


dir_path = os.path.dirname(os.path.abspath(__file__))

os.chdir(dir_path)

choix = 0
while True:
	# liste des sous-dossiers
	liste_dossiers = [dir_path]
	
	#print(os.listdir())

	for f in os.listdir(os.getcwd()):
	    if os.path.isdir(f):
	        liste_dossiers.append(f)

	
	if len(liste_dossiers) > 1:
		lister_le_dossier(liste_dossiers)
		nmax = len(liste_dossiers)
		choix = int(input('choisir un dossier (0 pour remonter, > {} pour FIN) : '.format(nmax-1)))
		if choix >= len(liste_dossiers):
			break
		else:
			#print(len(liste_dossiers),choix)
			changer_de_dossier(liste_dossiers,choix)
	else:
		liste = list(os.listdir())
		liste_fichiers = []
		#print(liste_fichiers)
		for f in liste:
			#print(f.split('.'))
			if f.split('.')[1] == 'csv':
				liste_fichiers.append(f)
		lister_les_fichiers(liste_fichiers)
		nmax = len(liste_fichiers)
		choix = int(input('choisir un fichier (0 pour remonter, > {} pour FIN) : '.format(nmax)))
		if choix == 0:
			changer_de_dossier(liste_dossiers,choix)
		elif choix > len(liste_fichiers):
			break
		else:
			print('Ouverture de ',liste_fichiers[choix-1])
			x,y = importer_datas(liste_fichiers[choix-1])
			
print('FIN')
