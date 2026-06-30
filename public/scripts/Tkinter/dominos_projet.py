from tkinter import *


class Game(Tk):
    def __init__(self,partie):
        Tk.__init__(self)
        # création des widgets "esclaves" :
        self.can1 = Canvas(self, bg='dark grey', height=400, width=600)
        self.can1.pack(side=LEFT, padx=40, pady=5)
        self.partie = partie # stocke l'objet partie de la classe Partie
        self.X = 40     # position X coin sup gauche du domino à venir
        self.Y = 100    # position Y
        self.dir = 'E'  # direction du prochain domino à placer
        self.create()   # fonction de creation des objets Tkinter
        self.replay()   # appelée pour RAZ du jeu ET de la partie

    def affiche_debut(self):
        self.text_affichage.set("Entrer la valeur\ndu \nDomino suivant\n puis VALIDER")

    def replay(self):
        """
        Remise à zero de la partie: de la liste chainée (partie)
        et des affichages
        """
        # RAZ de l'objet self.partie
        self.partie.RAZ()
        print(self.partie)
        # RAZ de la textBox
        self.textBox.delete('1.0',"end")
        self.textBox.insert('1.0', '{},{}'.format(self.partie.first.val1,self.partie.first.val2))
        # RAZ des affichages et du canvas
        self.affiche_debut()
        self.can1.delete("all")
        # Demarrage des dominos dans la partie gauche du canvas
        self.X = 40
        self.Y = 100
        # Par defaut, direction vers la droite
        self.dir = 'E'
        # puis dessiner le domino
        self.dessine()

    def readtext(self):
            """
            fonction appelée lorsque l'on valide avec le bouton VALIDER
            - lecture du contenu de la textBox avec le format de données
            2,4,[E O S N]
            soit valeur1,valeur2,direction
            alors valeur1 -> self.val1 et valeur2 -> self.val2
            direction -> self.dir
            - ou bien
            2,4
            soit valeur1,valeur2
            alors seuls les attributs self.val1 et self.val2 sont modifés
            self.dir n'est pas modifiée (E au debut)
            exemples:
            ---------
            - la textBox est validée avec: 4,2,S
            alors s vaut [4,2,S\n] et on ajoute le domino 4,2 à la partie
            dans la direction S (Sud)
    		- la textBox est validée avec: 4,2
    		alors s vaut [4,2] et on ajoute le domino 4,2 à la partie sans
    		changer de direction
            """
            # lecture de la textBox
            result = self.textBox.get("1.0", "end")
            # decoupage de la chaine de caracteres selon les virgules
            s = str(result).split(',')

            # AJOUTER condition avec self.partie.pose_correcte(s[1])
            # tout le reste est declenché par condition == True
            # sinon: message d'erreur sur text_affichage qui demande de corriger
            self.text_affichage.set('DOMINO joué\n {},{}'.format(s[0], s[1]))

            self.partie.ajouter_fin()  # a completer (1)

            print(self.partie)

            if len(s) > 2:
                self.dir =  '?' # à completer (2) remplacer le '?'

            self.dessine()

    def dessine(self):
        r = 40
        # mise a jour self.X,self.Y selon direction
        if self.dir == 'E':
            self.X += r + 2
        elif self.dir == 'O':
            self.X -= r + 2
        elif self.dir == 'N':
            self.Y -= r + 2
        else:
            self.Y += r + 2
        # premier carre
        self.can1.create_rectangle(self.X,self.Y,
                              self.X + r, self.Y + r,
                              outline='black', fill='grey')
        self.can1.create_text(self.X + r//2,self.Y + r//2, text = self.partie.end.val1)
        # changer position pour 2e carre
        if self.dir == 'E':
            self.X += r
        elif self.dir == 'O':
            self.X -= r
        elif self.dir == 'N':
            self.Y -= r
        else:
            # self.dir == 'S'
            self.Y += r
        # dessin 2e carre
        self.can1.create_rectangle(self.X, self.Y,
                                   self.X + r, self.Y + r,
                                   outline='black', fill='grey')
        self.can1.create_text(self.X + r // 2, self.Y + r // 2, text=self.partie.end.val2)

    def create(self):
        self.bou1 = Button(self, text='Quitter', command=self.quit)
        self.bou1.pack(side=BOTTOM)
        self.bou2 = Button(self, text='(Re)Jouer', command=self.replay)
        self.bou2.pack()

        # Une textBox
        self.textBox = Text(self, height=1, width=15)
        self.textBox.pack()
        # Bouton pour valider la saisie
        self.bou3 = Button(self, text='Valider', command=self.readtext)
        self.bou3.pack()

        self.text_affichage = StringVar()
        self.txt1 = Label(self, textvariable= self.text_affichage, justify=LEFT, font='TkFixedFont')
        self.txt1.pack()
        self.text_affichage.set("Cliquer sur \n le bouton \n pour demarrer")

        self.affichage = Label(self, text='')
        self.affichage.pack()


class Domino:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
        self.suiv = None


class Partie:
    def __init__(self, first):
        self.first = first
        self.end = first

    def ajouter_fin(self,D):
        """
        ajoute l'objet domino D à la fin de la chaine:
        ajoute d'abord D à self.end.suiv
        puis D à self.end
        :param D: instance de Domino
        """
        pass

    def RAZ(self):
        """
        Détache le premier élement du reste de la chaine:
        met d'abord self.first.suiv à None
        puis self.end prend la valeur de self.first
        """
        pass

    def pose_correcte(self,val):
        """
        teste si le nouveau domino à poser est compatible avec le dernier de la chaine
        comparer alors val (équivaut à val1 0..6) du domino à poser avec val2 du dernier
        domino de la partie
        :param val: int
        :return: bool, True si les valeurs sont identiques
        """
        pass

    def __repr__(self):
        M = self.first
        s = '{}:{} '.format(M.val1, M.val2)
        while not M.suiv is None:
            M = M.suiv
            s += ' => {}:{}'.format(M.val1, M.val2)
        return s


if __name__ == '__main__':
    D1 = Domino(2,4)
    partie1 = Partie(D1)
    app = Game(partie1)
    app.mainloop()