# halloween1

This is a little program made for a halloween event.  I was asked to make something for "the lab of a mad scientist who is researching super powers". It is designed to run on Linux on a lightweight computer (I used a Raspberry Pi) attached to an old, low resolution CRT monitor.  It will not display properly on a Windows-based machine because it uses some characters that display differently on Linux.
This program will loop infinitely, so press Ctrl-C to exit.
You will need Python 2.7.whatever installed, so: *sudo apt-get update && sudo apt-get install python*

To keep the screen on in the terminal (not x): 
*sudo nano /etc/kbd/config*

Find the line for BLANK_TIME and POWERDOWN_TIME and set them to 0.

BLANK_TIME=0
POWERDOWN_TIME=0

Then reboot or restart the service.

To start the program at boot:

*sudo nano /etc/rc.local*

Add this line near the bottom:

*python /home/pi/hween.py*
(assuming this is the location of the file)

This should work as long as you're booting to terminal and not X.  If you're booting to X, git gud nub <3
