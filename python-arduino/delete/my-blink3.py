#!/usr/bin/python3

import pyfirmata2


PIN = 13  # Pin 13 is used
DELAY = 1  # 1 second delay

# Adjust that the port match your system, see samples below:
# On Linux: /dev/tty.usbserial-A6008rIF, /dev/ttyACM0,
# On Windows: \\.\COM1, \\.\COM2
#PORT =  pyfirmata2.Arduino.AUTODETECT
PORT = '\\.\COM3'
PORT = '/dev/ttyS3'

# Creates a new board
board = pyfirmata2.Arduino(PORT)

# Loop for blinking the led
while True:
    board.digital[PIN].write(1)  # Set the LED pin to 1 (HIGH)
    board.pass_time(DELAY)
    board.digital[PIN].write(0)  # Set the LED pin to 0 (LOW)
    board.pass_time(DELAY)
