#!/bin/bash
sudo apt update
sudo apt install python3-pip
pip3 install schedule
pip3 install pysftp

#Install driver for Pimoroni Display HAT Mini
echo 'Install driver for Pimoroni Display HAT Mini'
sudo apt install python-rpi.gpio python-spidev python-pip python-pil python-numpy
sudo pip3 install st7789
git clone https://github.com/pimoroni/st7789-python

#Install driver for Pimoroni PA1010D GPS Breakout
echo 'Install driver for Pimoroni PA1010D GPS Breakout'
sudo raspi-config nonint do_i2c 0 #Enable I2C
git clone https://github.com/pimoroni/pa1010d-python
cd pa1010d-python
sudo ./install.sh

#Install drivers Zero2Go Omini Rev2 Raspberry Pi HAT: https://www.uugear.com/doc/Zero2Go_Omini_Rev2_UserManual.pdf
echo 'Install drivers Zero2Go Omini Rev2 Raspberry Pi HAT: https://www.uugear.com/doc/Zero2Go_Omini_Rev2_UserManual.pdf'
#Zero2Go Omini Rev2 raspberry pi HAT:
cd ~/
wget http://www.uugear.com/repo/Zero2GoOmini/installZero2Go.sh
sudo sh installZero2Go.sh

#CONFLICTION WITH 1-WIRE INTERFACE
#If you have 1-Wire interface enabled and didn’t specify the GPIO pin for 1-Wire, 
#it will use GPIO-4 and that conflict with Zero2Go Omini. Zero2Go Omini uses GPIO-4 to receive shutdown command, 
#if GPIO-4 is also assigned to 1-Wire, Zero2Go’s software will receive shutdown command unexpectedly. 
#If your Raspberry Pi always automatically shutdown itself after installing Zero2Go’s software, 
#that most probably due to the confliction with 1-Wire interface.

#When this happens, you most probably can not login your Raspberry Pi because it always shuts itself down before you get the chance to login. 
#To solve this problem, you will need to take out the micro-SD card on your Raspberry Pi, and access its file system via a card reader. 
#You need to edit the config.txt file in the “boot” volume to change the GPIO pin used by 1-Wire interface, 
#or you can disable 1-Wire interface if you don’t need it for now. You need to find something like “dtoverlay=w1-gpio” in the file.

#If you want 1-Wire to use GPIO-18, just change “dtoverlay=w1-gpio” to:

#dtoverlay=w1-gpio,gpiopin=18

#If you want to disable 1-Wire interface, just comment it out:

#dtoverlay=w1-gpio

#Save the file and eject your micro SD card, and put it back to your Raspberry Pi. Now your Raspberry Pi should be able to boot normally.

