"""


Auteur: Eric Tixidor

Interface: microbit

Nom du projet: robot_marqueen_5

Description: avancer cases

Toolbox: vittascience

Mode: code

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="on_start" id="G[=T#8yqB70`NFgYq}GP" deletable="false" x="13" y="-13"><statement name="DO"><block type="io_log_deleteLogs" id="A(WGfrAkb6GQw.sUg@v%"><next><block type="io_log_setLabel" id="B@nKJ8E#Ckp/M+Rd_gTi"><mutation items="1"></mutation><field name="TIMESTAMP">MILLISECONDS</field><value name="ADD0"><block type="text" id="h8~hE5fqX[,S+!Bbo9qT"><field name="TEXT">capteur</field></block></value><next><block type="io_log_addData" id=":*_i?E]sV`d+]u[T]kym"><mutation items="1"></mutation><value name="ADD0"><block type="io_log_data" id="E(oAhhi.(|Hun3-,%=y}"><value name="LABEL"><shadow type="text" id="l,OI/K^lvCDyv0YG%6S/"><field name="TEXT">capteur</field></shadow></value><value name="DATA"><shadow type="math_number" id=".suOd[lk(n~%-STSZ_!1"><field name="NUM">0</field></shadow><block type="variables_force_type" id="sx^u{@j-rVI4]NafRV.?"><field name="TYPE">int</field><value name="VALUE"><shadow type="math_number" id="#/ZS]nMCx.C~c9s:8Elu"><field name="NUM">0</field></shadow><block type="robots_readMaqueenPatrol" id=";PT})33ilM_1U4vw_[%N"><field name="PIN">pin14</field></block></value></block></value></block></value><next><block type="robots_moveOneSquareForward" id=";,$zKGOc_Z9WEM.gmj!X"><next><block type="io_pause" id="fyL649@wJbkm)gwO0:/T"><field name="UNIT">SECOND</field><value name="TIME"><shadow type="math_number" id="|UPi=+fVwpC6=aI(i~/r"><field name="NUM">1</field></shadow></value><next><block type="io_log_addData" id="m#n88;g)lSc$Z=#[?Vfi"><mutation items="1"></mutation><value name="ADD0"><block type="io_log_data" id="+01rc[jS~uH%4A0olOA7"><value name="LABEL"><shadow type="text" id="!DNW`JL8eCJ=oEixgW-`"><field name="TEXT">capteur</field></shadow></value><value name="DATA"><shadow type="math_number"><field name="NUM">0</field></shadow><block type="variables_force_type" id="5=Wr2h_uuo8GG.p`LTKN"><field name="TYPE">int</field><value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow><block type="robots_readMaqueenPatrol" id="iHt}[xDeyP|]Ed(6#X}6"><field name="PIN">pin14</field></block></value></block></value></block></value><next><block type="robots_turnRight" id="]y8_Jtp(NV~`[ib.t!`]"><next><block type="robots_moveOneSquareForward" id="dJEBTzw8XAD5UI=V_P5."><next><block type="io_log_addData" id="A)c2wHm#L]j^H{ZcPtU+"><mutation items="1"></mutation><value name="ADD0"><block type="io_log_data" id="P}V+iBl.nN.jhRlW{We9"><value name="LABEL"><shadow type="text" id="#:h*Ib4Y-SIx#TUW*iT0"><field name="TEXT">capteur</field></shadow></value><value name="DATA"><shadow type="math_number"><field name="NUM">0</field></shadow><block type="variables_force_type" id="!E6$bF#G/VTxE`hHIeyX"><field name="TYPE">int</field><value name="VALUE"><shadow type="math_number"><field name="NUM">0</field></shadow><block type="robots_readMaqueenPatrol" id="kaEJ~ege23|Fn3C`DJh$"><field name="PIN">pin14</field></block></value></block></value></block></value></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></statement></block><block type="forever" id="o[WN]+eeF.OUxGch67@8" x="62" y="562"></block></xml>

Projet généré par Vittascience.

Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau

sur l'interface http://vittascience.com/microbit


"""

from microbit import *
import log
import math
import utime

""" Maqueen robot """

def convertSpeed_mps(speed, max_speed, max_rpm, wheels_diameter):
  # 2π * wheels_diameter / 2 * speed_rpm / 60
  return 2*math.pi*wheels_diameter/2*1e-2*(speed/max_speed*max_rpm)/60

def maqueen_moveWithSquare(x, direction, speed=255):
  speed_mps = convertSpeed_mps(speed, 255, 133, 4.3)
  for i in range(int(x)):
    i2c.write(0x10, bytearray([0x00, direction, speed]))
    i2c.write(0x10, bytearray([0x02, direction, speed]))
    utime.sleep_ms(int(15e-2/speed_mps*1000)//4) 
    # reduire ou augmenter utime.sleep pour gerer la longueur du deplacement
    i2c.write(0x10, bytearray([0x00, 0, 0]))
    i2c.write(0x10, bytearray([0x02, 0, 0]))

def maqueen_turnAngle(angle, speed=255):
  speed_mps = convertSpeed_mps(speed, 255, 133, 4.3)
  # wheels_center_radius * degToRad(angle)
  angularDistance = 3.5*1e-2*angle/180*math.pi
  motorLeftDir = 0x0 if angularDistance < 0 else 0x1
  motorRightDir = 0x1 if angularDistance < 0 else 0x0
  i2c.write(0x10, bytearray([0x00, motorLeftDir, speed]))
  i2c.write(0x10, bytearray([0x02, motorRightDir, speed]))
  utime.sleep_ms(int(math.fabs(angularDistance)/speed_mps*1000))
  i2c.write(0x10, bytearray([0x00, 0, 0]))
  i2c.write(0x10, bytearray([0x02, 0, 0]))

log.delete(full=True)
log.set_labels('capteur', timestamp=log.MILLISECONDS)
log.add(capteur = int(pin14.read_digital()))
maqueen_moveWithSquare(1, 0x0, 100)
utime.sleep(1)
log.add(capteur = int(pin14.read_digital()))
maqueen_turnAngle(-45, 50)
utime.sleep(1)
#maqueen_moveWithSquare(1, 0x0, 200)
log.add(capteur = int(pin14.read_digital()))

while True:
  pass
