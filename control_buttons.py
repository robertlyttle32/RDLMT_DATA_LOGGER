#!/bin/bash
import time
import RPi.GPIO as GPIO
import os
import DISPLAY_TEXT as display

BUTTON_X_GPIO = 16
BUTTON_Y_GPIO = 24
BUTTON_A_GPIO = 5
BUTTON_B_GPIO = 6
if __name__ == '__main__':

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_X_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_Y_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_A_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_B_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    pressed = False
    while True:
    # button is pressed when pin is LOW
        #if not GPIO.input(BUTTON_X_GPIO):
        if  not GPIO.input(BUTTON_A_GPIO):
            #if not pressed:
            print("START")
            pressed = True
            os.system('python3 /home/pi/release/DATA_LOGGER_MAIN.py')
            time.sleep(.25)

            #os.system('./scrolling-text.py dhmini')
                # button not pressed (or released)

        if  not GPIO.input(BUTTON_Y_GPIO):
            time.sleep(5)
            #if not pressed
            GPIO.cleanup()
            os.system('sudo poweroff')
        display.get_display(70, 110, 'Press START')

