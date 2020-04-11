# Demo project for python Arduino

## Arduino IDE
Install Arduio driver and IDE from  from hourly build https://www.arduino.cc/en/Main/Software
update the Drivers as explained in https://www.arduino.cc/en/Guide/DriverInstallation
(drivers location is arduino-nightly-windows\arduino-nightly\drivers)

installataion can also be done from store 

## Find the correct COM


https://blogs.msdn.microsoft.com/wsl/2017/04/14/serial-support-on-the-windows-subsystem-for-linux/
https://icircuit.net/accessing-com-port-from-wsl/2704

```
sudo apt install cu
cu -l /dev/ttyS3 -s 9600
```


## Install the python packages 
```
sudo apt-get install python-setuptools
sudo easy_install pip
sudo pip install pyserial
sudo pip install pyfirmata
```

## setup the wires 

https://create.arduino.cc/projecthub/GodsVictor1/simple-blinking-led-bf4fc3


## Check from WSL 
```
 python wsl-test.py
```

## More info
*  https://github.com/microsoft/WSL/issues/1929 


```
cu -l /dev/ttyS3 --debug all -s 1200
```
