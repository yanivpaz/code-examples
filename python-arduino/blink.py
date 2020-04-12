# Import required libraries
from pyfirmata2 import Arduino, util
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
port = '/dev/ttyS3'
#board = Arduino(Arduino.AUTODETECT)
board = Arduino(port)
# Use iterator thread to avoid buffer overflow
it = util.Iterator(board)
it.start()
 
# Define pins
redPin = 13
while True:
 board.digital[13].write(1)
 blinkLED(redPin, "message to the world")
 board.digital[13].write(0)
