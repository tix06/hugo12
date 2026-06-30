# Write your code here :-)
# Programme communication avec auteur authentifié POO
from microbit import *
import radio
import utime


class Communication_radio:
  def __init__(self, ch=7,gpe=0,messages=['LIKE','Publi'],numero='A', reseau = {'A':['B'],'B':['A']}):
    self.channel = ch
    self.group = gpe
    self.messages = messages
    self.img = [Image.DIAMOND,Image.DIAMOND_SMALL]
    self.numero = numero
    self.reseau = reseau
    self.compteur = 0

  def select_message(self):
    message_complet = str(self.numero) + "_" + self.messages[1]
    return message_complet

  def img_send(self):
    display.show(self.img,delay=100)
    utime.sleep(0.015)
    display.clear()

  def parse(self,stringData):
    """retourne:
    - etat du compteur +1 si n == self.numero ET texte == 'LIKE'
    - 'LIKE' si n est le numero d'un compte suivi ET texte == 'Publi'. Et emission radio avec radio.send('n_LIKE')
    - '', string vide, si n ne correspond a aucun des 2 cas precedents
    """
    try:
      n, texte = stringData.split('_')
    except:
      # reception d'un message sans caractere '_'
      n= 0
      texte = ""
      # on n'affiche rien
    if n == self.numero and texte == self.messages[0]:
        # le message nous est adresse, et c'est un LIKE
        # on incremente le compteur de LIKE
        self.compteur += 1
        display.show(Image.HEART)
        utime.sleep(0.4)
        display.clear()
        return self.compteur
    elif n in self.reseau[self.numero] and texte == self.messages[1]:
        # le message est une 'Publi' vient d'un compte que l'on suit
        # on retourne un LIKE
        message = n + '_' + self.messages[0]
        # envoi automatique
        radio.send(message)
        return self.messages[0]
    else:
        return ""




# Attention a changer le 4e argument par la lettre attribuee a votre carte ('A', 'B', ...)
com = Communication_radio(7,0,['LIKE','Publi'],'B',{'A':['B'],'B':['A']})
radio.on()
radio.config(channel = com.channel, power = 6, length = 32, group=com.group)

while True:
  if button_a.is_pressed():
    radio.send(com.select_message())
    com.img_send() # affiche l'animation lors de l'envoi du message
    stringData = "" # RAZ du buffer

  stringData = radio.receive()
  if stringData:
    texte = com.parse(stringData)
    if texte == 'LIKE':
      display.show(Image.HAPPY)
      utime.sleep(0.4)
      display.clear()
    else:
        display.scroll(texte)
        utime.sleep(0.4)
        display.clear()
    stringData = "" # RAZ du buffer
