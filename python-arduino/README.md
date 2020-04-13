# Arduino on WSL1 - checklist

## Install Arduino IDE
Install Arduino IDE from https://www.arduino.cc/en/Main/Software
( Installation can also be done from microsoft store )

## Install Arduino drivers
  Install Arduino Drivers as explained in https://www.arduino.cc/en/Guide/DriverInstallation
(if  nightly builds are used , drivers location is arduino-nightly-windows\arduino-nightly\drivers)

## Install python3 pyfirmata2 package in WSL
The demo application is based on python3 and pyfirmata2.   
python2 might work as well but was not tested .
```
sudo apt install python3-pip
sudo pip3 install pyfirmata2
```

## Find the serial port 
find Arduino serial port via device manager .

<b> note </b> : COM3 anme in WSL is /dev/ttyS3  
see more explnation [here](https://icircuit.net/accessing-com-port-from-wsl/2704)

## Set the wires 
connect the wires as described in [this article](https://create.arduino.cc/projecthub/GodsVictor1/simple-blinking-led-bf4fc3) 


## Load fyfirmata sketch via Arduino IDE
fyfirmata2 must be loaded to Arduino board.  
See the section ["Uploading the Firmata Sketch"]( https://realpython.com/arduino-python/) 

## Run the blink.py
```
sudo python3 ./blink.py
```

## Test the board
* Turn on one light using [firmata test](https://github.com/firmata/firmata_test) 
* Run test from Arduino IDE using ide-test.py 
* If code is not working from WSL , try native windows ( using COM2) . see [this](https://github.com/berndporr/pyFirmata2/blob/master/examples/blink.py) code


## Debugging the board from command line 
Debug Arduino  connection using the command below
```
cu -l /dev/ttyS3 --debug all
```

## Future - WSL2  
* WSL2 is not yet supporting USB :-(
  
