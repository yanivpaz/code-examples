#
#!/usr/bin/python
 
# Import required libraries
from pyfirmata import Arduino, util
from time import sleep
 
# Define custom function to perform Blink action
def blinkLED(pin, message):
    print ( message )
    board.digital[pin].write(1)
    sleep(1)
    board.digital[pin].write(0)
    sleep(1)
 
# Associate port and board with pyFirmata
#port = '/dev/ttyACM0'
port = 'COM2'
board = Arduino(port)
# Use iterator thread to avoid buffer overflow
it = util.Iterator(board)
it.start()
 
# Define pins
redPin = 13
while True:
 blinkLED(redPin, "message to the world")
