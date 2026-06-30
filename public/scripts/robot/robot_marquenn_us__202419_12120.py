"""


Auteur: anonyme

Interface: microbit

Nom du projet: Nouveau projet

Description: undefined

Toolbox: vittascience

Mode: blocks

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><variables><variable id="tSsMNY6IJ.vKdW8Av3i{">i</variable><variable id="!e9%ly89}viDE;u~V*AH">d</variable></variables><block type="on_start" id="G[=T#8yqB70`NFgYq}GP" deletable="false" x="0" y="0"><statement name="DO"><block type="io_log_setLabel" id="t`wnrOD7D%x|x;YvV}s6"><mutation items="1"></mutation><field name="TIMESTAMP">MILLISECONDS</field><value name="ADD0"><block type="text" id="*G^s]J-jme5*tx[g/xmA"><field name="TEXT">distance</field></block></value><next><block type="io_log_setLabel" id="orEHxc4ZnbLjSWU5W*,_"><mutation items="1"></mutation><field name="TIMESTAMP">MILLISECONDS</field><value name="ADD0"><block type="text" id="z]aWj)+u|ELf7K+CU7Jb"><field name="TEXT">temps</field></block></value><next><block type="variables_set" id="H9{R{igO:gx/Hnjq1#GZ"><field name="VAR" id="tSsMNY6IJ.vKdW8Av3i{">i</field><value name="VALUE"><shadow type="math_number" id="r_H!YL]t{?#nkTeSNv9."><field name="NUM">0</field></shadow></value></block></next></block></next></block></statement></block><block type="forever" id="o[WN]+eeF.OUxGch67@8" x="-13" y="337"><statement name="DO"><block type="io_onButtonPressed" id="N@O-{v?dG_z($./1A(yS"><field name="BUTTON">a</field><field name="STATE">is_</field><statement name="DO"><block type="io_log_deleteLogs" id="_?7[uE0B(c1}gvWPX-gA"><next><block type="variables_set" id="l]8XN]=8b1iR#h1nR/}N"><field name="VAR" id="tSsMNY6IJ.vKdW8Av3i{">i</field><value name="VALUE"><shadow type="math_number" id="Vm}ms(2voW3DTO0Dzr+L"><field name="NUM">0</field></shadow></value></block></next></block></statement><next><block type="io_pause" id="^Xc,84EZ;y3~k=Q[I6@V"><field name="UNIT">SECOND</field><value name="TIME"><shadow type="math_number" id="N@=018,sWW6105^0KQ.b"><field name="NUM">1</field></shadow></value><next><block type="variables_set" id="/P;zQMiF:c[QxB!j%u_4"><field name="VAR" id="!e9%ly89}viDE;u~V*AH">d</field><value name="VALUE"><shadow type="math_number" id="ZauFZMCM0_?F168C~/]s"><field name="NUM">0</field></shadow><block type="robots_getMaqueenUltrasonicRanger" id="!-6ATX.MQth(3TQHm0hN"><field name="DATA">distance</field></block></value><next><block type="controls_if" id="(eT]C?/G(r.PDlJ#fDXV"><value name="IF0"><block type="logic_compare" id="uU:I]f?q^u0~n0UZq#*0"><field name="OP">GT</field><value name="A"><block type="variables_get" id="%jI[eS1.YQWtwqRvU7eo"><field name="VAR" id="!e9%ly89}viDE;u~V*AH">d</field></block></value><value name="B"><shadow type="math_number" id="7vgS_%t^9?oT~^Q.v`p+"><field name="NUM">0</field></shadow></value></block></value><statement name="DO0"><block type="io_log_addData" id="MFUPlD[UoD5g0;W`Q+[`"><mutation items="2"></mutation><value name="ADD0"><block type="io_log_data" id="NXIDvue?66eI}m$=s~hT"><value name="LABEL"><shadow type="text" id="6-I@;D,4TU{IHYE7;F=P"><field name="TEXT">distance</field></shadow></value><value name="DATA"><shadow type="math_number" id="Im~nM:pJlc=OmS?m5d;-"><field name="NUM">0</field></shadow><block type="variables_get" id="#/Rkc6DCm5?6TLk01lQK"><field name="VAR" id="!e9%ly89}viDE;u~V*AH">d</field></block></value></block></value><value name="ADD1"><block type="io_log_data" id="{5:P/4|~P6x%f+H3/NvD"><value name="LABEL"><shadow type="text" id="G:a6UwfU.hA@gEZq47M,"><field name="TEXT">temps</field></shadow></value><value name="DATA"><shadow type="math_number" id="slQJwtr1LDfxRNg.j3:~"><field name="NUM">0</field></shadow><block type="variables_get" id="{S5@9nXvoA*?Fj]V8)i$"><field name="VAR" id="tSsMNY6IJ.vKdW8Av3i{">i</field></block></value></block></value><next><block type="variables_increment" id="D;Q4kGupBl4X@nQ|Lubx"><field name="VAR" id="tSsMNY6IJ.vKdW8Av3i{">i</field><value name="DELTA"><shadow type="math_number" id="!_PQ161!2];@iEAIk~Jz"><field name="NUM">1</field></shadow></value></block></next></block></statement><next><block type="show_string" id="rJSTd2=8^?g780RFY.rl"><mutation speed="false"></mutation><value name="TEXT"><shadow type="text" id="~*=8}lX~`wgh=+m?t):h"><field name="TEXT">1024</field></shadow><block type="variables_get" id="YKr@c5X3E}l(axu-5QQH"><field name="VAR" id="!e9%ly89}viDE;u~V*AH">d</field></block></value></block></next></block></next></block></next></block></next></block></statement></block></xml>

Projet généré par Vittascience.

Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau

sur l'interface http://vittascience.com/microbit


"""

from microbit import *
import log
import utime
from machine import time_pulse_us

""" Maqueen robot """

# Ultrasonic TRIG on pin1
# Ultrasonic ECHO on pin2

def getUltrasonicData(trig, echo, data='distance', timeout_us=30000):
  trig.write_digital(0)
  utime.sleep_us(2)
  trig.write_digital(1)
  utime.sleep_us(10)
  trig.write_digital(0)
  echo.read_digital()
  duration = time_pulse_us(echo, 1, timeout_us)/1e6 # t_echo in seconds
  if duration > 0:
    if data == 'distance':
      #sound speed, round-trip/2, get in cm
      return 343 * duration/2 * 100
    elif data == 'duration':
      return duration
    else:
      raise ValueError("Data option '" + data + "' is not valid")
  else:
    return -1

log.set_labels('distance', timestamp=log.MILLISECONDS)
log.set_labels('temps', timestamp=log.MILLISECONDS)
i = 0

while True:
  if button_a.is_pressed():
    log.delete(full=True)
    i = 0
  utime.sleep(1)
  d = getUltrasonicData(pin1, pin2, 'distance')
  if d > 0:
    log.add(distance = d,temps = i)
    i = i + 1
  display.scroll(str(d), delay=150, wait=True)
