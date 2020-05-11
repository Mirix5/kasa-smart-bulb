import random
import time
import os

lamp_ip = '192.168.42.3'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

while (True):
  hue = random.randrange(1, 360)
  saturation = 100
  brightness = 100

  print("Changing color to: %d" % (hue))
  command = "tplight hsb -t 3000 %s %d %d %d" % (lamp_ip, hue, saturation, brightness)
  os.system(command)
  time.sleep(4)