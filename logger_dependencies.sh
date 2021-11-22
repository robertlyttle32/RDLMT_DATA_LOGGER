#!/bin/bash
sudo apt update
sudo apt install python3-pip
pip3 install schedule
sudo apt install python-rpi.gpio python-spidev python-pip python-pil python-numpy
sudo pip3 install st7789
git clone https://github.com/pimoroni/st7789-python
