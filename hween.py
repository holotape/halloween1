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
   print("░░░░░░░░░░   0%")
   time.sleep(1)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("▓░░░░░░░░░  10%")
   time.sleep(1)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("▓▓░░░░░░░░  20%")
   time.sleep(1)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("▓▓▓░░░░░░░  30%")
   time.sleep(1)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("▓▓▓▓░░░░░░  40%")
   time.sleep(1)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("▓▓▓▓▓░░░░░  50%")
   time.sleep(1)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("▓▓▓▓▓▓░░░░  60%")
   time.sleep(1)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("▓▓▓▓▓▓▓░░░  70%")
   time.sleep(1)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("▓▓▓▓▓▓▓▓░░  80%")
   time.sleep(1)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("▓▓▓▓▓▓▓▓▓░  90%")
   time.sleep(1)
   
   sys.stderr.write("\x1b[2J\x1b[H")
   print("▓▓▓▓▓▓▓▓▓▓ 100%")
   
experiment_xxx()
print "[UNSUCCESSFUL]"
time.sleep(2)
print "RECALCULATING"
time.sleep(2)
while line:
    print line
    line = file_object.readline()
    time.sleep(0.09)
file_object.close()