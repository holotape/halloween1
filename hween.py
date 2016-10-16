import sys, time, colorama, random

from colorama import init
init()

from random import randint

file_object = open("kernel.txt", "r")
line = file_object.readline()

print ("\033[1;32;40m INITIALISING  \n")
time.sleep(2)
sys.stderr.write("\x1b[2J\x1b[H")

def experiment_xxx():
   print "RUNNING TEST ON SUBJECT", random.randint(522,9067)
   time.sleep(10)

   sys.stderr.write("\x1b[2J\x1b[H")
   print("INJECTING X-SERUM")
   print("░░░░░░░░░░   0%")
   time.sleep(2)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("INJECTING X-SERUM")
   print("▓░░░░░░░░░  10%")
   time.sleep(2)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("MEASURING VITALS")
   print("▓▓░░░░░░░░  20%")
   time.sleep(2)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("MEASURING VITALS")
   print("▓▓▓░░░░░░░  30%")
   time.sleep(2)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("SUBJECT NON-RESPONSIVE")
   print("▓▓▓▓░░░░░░  40%")
   time.sleep(6)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("INCREASING VOLTAGE +10,000v")
   print("▓▓▓▓▓░░░░░  50%")
   time.sleep(3)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("SUBJECT NON-RESPONSIVE")
   print("▓▓▓▓▓▓░░░░  60%")
   time.sleep(4)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("INCREASING VOLTAGE +20,000v")
   print("▓▓▓▓▓▓▓░░░  70%")
   time.sleep(3)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("WARNING: VOLTAGE TOLERANCE LIMIT REACHED")
   print("▓▓▓▓▓▓▓▓░░  80%")
   time.sleep(4)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("WARNING: SUBJECT VITALS CRITICAL")
   print("▓▓▓▓▓▓▓▓▓░  90%")
   time.sleep(3)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("WARNING: TERMINATE PROGRAM")
   print("▓▓▓▓▓▓▓▓▓▓ 100%")
   time.sleep(3)

experiment_xxx()
print "[UNSUCCESSFUL: SUBJECT LOST]"
time.sleep(2)
print "[RECALCULATING]"
time.sleep(2)
while line:
    print line
    line = file_object.readline()
    time.sleep(0.09)
file_object.close()