from tkinter import *
from PIL import Image, ImageTk


def get_age(event):
    """
    fonction appelée lorsque l'on appuie sur ENTER
    """
    age = saisie.get()
    texte = "Vous avez       \n" + age + " ans      "
    txt1 = Label(fen1, text=texte, justify=LEFT, font='TkFixedFont')
    txt1.place(relx=1.0,
               rely=0.2,
               anchor='e')


def entrer(event):
    """
    fonction appelée lorsque l'on clique sur l'image
    """
    texte = "Ouah ça a l\'air \n sympa ici!"
    txt1 = Label(fen1, text=texte, justify=LEFT, font='TkFixedFont')
    txt1.place(relx=1.0,
               rely=0.2,
               anchor='e')


def replay():
    """
    fonction appelée lorsque l'on clique sur le bouton
    """
    texte = "Entrer     \n votre age        "
    txt1 = Label(fen1, text=texte, justify=LEFT, font='TkFixedFont')
    txt1.place(relx=1.0,
               rely=0.2,
               anchor='e')


# fenetre principale
fen1 = Tk()

# création des widgets:
#### le canvas: fenêtre de dessin #####
can1 = Canvas(fen1, bg='dark grey', height=400, width=600)
can1.pack(side=LEFT, padx=5, pady=5)
####### un bouton pour quitter #######
bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)
#### Un autre bouton pour commander autre chose #####
bou2 = Button(fen1, text='(Re)Tenter ma chance', command=replay)
bou2.pack()
#### Un champ de saisie ####
saisie = Entry(fen1,textvariable="votre age", width=10)
saisie.place(relx=0.95,
               rely=0.5,
               anchor='e')
# gestionnaire d'evenement sur le champ de saisie
saisie.bind("<Return>", get_age)

# image discotheque
image = Image.open("images/disco.png")
image = image.resize((image.size[0] // 2, image.size[1] // 2), Image.ANTIALIAS)
photo_disco = ImageTk.PhotoImage(image)

disco = can1.create_image(0,0, anchor = "nw", image=photo_disco)
# gestionnaore d'evenement sur l'image
can1.tag_bind(disco, "<ButtonRelease>", entrer)

# Affichage des instructions initiales
replay()


# mainloop
fen1.mainloop()
