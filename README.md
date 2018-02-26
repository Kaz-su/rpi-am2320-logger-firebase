# rpi-am2320-logger-firebase
Temperature and humidity Logger on Raspberry Pi.  
Store temp/hum to Firebase Realtime Database 10 minutes each (You can change this).

## What is AM2320?
Temperature and Humidity Sensor.  
https://akizukidenshi.com/download/ds/aosong/AM2320.pdf

## Requirement
You need `Raspberry Pi`, `AM2320`, and Internet, some wires(connect Pi -> AM2320).  
Logged in Pi, you need `pytz` and `python-firebase`.
```
$ sudo pip install pytz
$ sudo pip install python-firebase
```

## Install
```
$ cd path/to/youwant
$ git clone git@github.com:Kaz-su/rpi-am2320-logger-firebase.git
```

## Usage
First, connect pi to AM2320.
![connection](https://github.com/Kaz-su/rpi-am2320-logger-firebase/blob/master/pi3_am2320.jpg)

Run script.
```
nohup python logger.py &
```

Datas will store like below
![sample](https://github.com/Kaz-su/rpi-am2320-logger-firebase/blob/master/example.png)
