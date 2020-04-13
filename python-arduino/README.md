# Arduino on WSL1 - checklist
There are many userguides in the web explaining how to run your first Arduino program  on native Windows. 
the purpose of this checklist is to demonstrate the same on WSL1.  

## Installation 
* Install Arduino IDE from [Arduino site](https://www.arduino.cc/en/Main/Software)

* Install Arduino Drivers as explained in [here](https://www.arduino.cc/en/Guide/DriverInstallation).  

* The demo application is based on python3 and [pyfirmata2](https://pypi.org/project/pyFirmata2/).   
python2 might work as well but was not tested .
```
sudo apt install python3-pip
sudo pip3 install pyfirmata2
```

## Find the serial port 
find Arduino serial port via device manager .  
<b> note </b> : COM3 anme in WSL is /dev/ttyS3  
see more information [here](https://icircuit.net/accessing-com-port-from-wsl/2704)

## Set the wires 
connect the wires as described in [this article](https://create.arduino.cc/projecthub/GodsVictor1/simple-blinking-led-bf4fc3) 

## Load fyfirmata sketch via Arduino IDE
fyfirmata2 must be loaded to Arduino board.  
See the section ["Uploading the Firmata Sketch"]( https://realpython.com/arduino-python/) 

## Test the board
Check the connection to the board using any one of the methods below :
* Turn on one light using [firmata test](https://github.com/firmata/firmata_test) 
* Run test from Arduino IDE using ide-test.py 
* If code is not working from WSL1 , try native windows ( using COM2) . see [this](https://github.com/berndporr/pyFirmata2/blob/master/examples/blink.py) code

## Run the blink.py in WSL1
```
sudo python3 ./blink.py
```

## Debug the Arduino board from WSL1 
Debug Arduino  connection using the command below
```
cu -l /dev/ttyS3 --debug all
```

## Future - WSL2  
* WSL2 is not yet supporting USB :-(
  
