# Demo project for python Arduino using WSL1

## Arduino IDE
* Install Arduio driver and IDE from  from hourly build https://www.arduino.cc/en/Main/Software
 ( Installataion can also be done from store )
* Update the Drivers as explained in https://www.arduino.cc/en/Guide/DriverInstallation
(drivers location is arduino-nightly-windows\arduino-nightly\drivers)


## Find the correct COM
find Arduino serial port via device manager .
<b> note </b> : /dev/ttyS3 is the WSL name for COM3

https://icircuit.net/accessing-com-port-from-wsl/2704

## Install the python pyfirmata2 package
The demo application is based on python3 and pyfirmata2 . 
python2 might work as well but was not tested .
```
sudo apt install python3-pip
sudo pip install pyfirmata2
```

## Setup the wires in Arduino
https://create.arduino.cc/projecthub/GodsVictor1/simple-blinking-led-bf4fc3

## Test the board 


## Load fyfirmata sketch via Arduino IDE
fyfirmata must be loaded to Arduino board
See the section "Uploading the Firmata Sketch" in https://realpython.com/arduino-python/

## Run the blink.py
```
sudo python3 ./blink.py
```

to see example of blink.py for native windows see
https://github.com/berndporr/pyFirmata2/blob/master/examples/blink.py

## Future 
* WSL2 is not yet supporting USB 
