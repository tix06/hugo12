########################################
# controler le robot avancer vitesse 125
########################################
i2c.write(0x10, bytearray([0x00, 0x0, int(255)]))
i2c.write(0x10, bytearray([0x02, 0x0, int(255)]))

########################################
# controler le moteur droit direction x vitesse 125
########################################
i2c.write(0x10, bytearray([0x02, 0x0, int(125)]))

########################################
# avancer d'une case
########################################
def convertSpeed_mps(speed, max_speed, max_rpm, wheels_diameter):
  # 2π * wheels_diameter / 2 * speed_rpm / 60
  return 2*math.pi*wheels_diameter/2*1e-2*(speed/max_speed*max_rpm)/60

def maqueen_moveWithSquare(x, direction, speed=255):
  speed_mps = convertSpeed_mps(speed, 255, 133, 4.3)
  for i in range(int(x)):
    i2c.write(0x10, bytearray([0x00, direction, speed]))
    i2c.write(0x10, bytearray([0x02, direction, speed]))
    utime.sleep_ms(int(15e-2/speed_mps*1000))
    i2c.write(0x10, bytearray([0x00, 0, 0]))
    i2c.write(0x10, bytearray([0x02, 0, 0]))

maqueen_moveWithSquare(1, 0x0, 100)

########################################
# distance ultra sons
########################################
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

getUltrasonicData(pin1, pin2, 'distance')

########################################
# arreter le robot
########################################
# completer



########################################
# controler le moteur gauche direction x vitesse 125
########################################
# completer

########################################
# pivoter a gauche
########################################
# completer

########################################
# pivoter a droite
########################################
# completer

########################################
# etat du capteur de ligne droit 
########################################
# completer

########################################
# etat du capteur de ligne gauche
########################################
# completer


########################################
# E/S micro:bit log
# effacer le log sur la microbit
########################################
# a completer

########################################
# ajouter un nouveau label avec un Timer milisecond label1
########################################
# a completer

########################################
# ajouter les donnees a un label label1 donnee 0
########################################



