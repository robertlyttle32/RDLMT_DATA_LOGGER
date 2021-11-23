#!/bin/bash
import serial
import io
import time
import os
import logging
from pathlib import Path
from datetime import datetime
from ublox_gps import UbloxGps
import make_csv_file as form_gps
from datetime import datetime
from pa1010d import PA1010D
import schedule
import argparse
#import DISPLAY_TEXT as TEXT
import sys
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import ST7789
import RPi.GPIO as GPIO


latitude = 0
longitude = 0
altitude = 0
num_sats = 0
gps_qual = 0
speed_over_ground = 0
pdop = 0
vdop = 0
hdop = 0
timestamp = 0
#FUNCTION = 'GPS_log'
LATITUDE = 0
LONGITUDE = 0
NAME = 0
ALTITUDE = 0
SPEED = 0
DATE = 0
TIME = 0
count = 0
RESET = False
RESET_BUTTON = False
STOP = False
#port = serial.Serial('/dev/serial0', baudrate=38400, timeout=1)
#gps = UbloxGps(port)
gps = PA1010D()
display_type = "dhmini"
LINE_NUM = 0
MESSAGE = ''
x = 0
y = 0


BUTTON_X_GPIO = 16
BUTTON_Y_GPIO = 24
BUTTON_A_GPIO = 5
BUTTON_B_GPIO = 6


GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_X_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_Y_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_A_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_B_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)


if display_type == "dhmini":
    disp = ST7789.ST7789(
        height=240,
        width=320,
        rotation=180,
        port=0,
        cs=1,
        dc=9,
        backlight=13,
        spi_speed_hz=60 * 1000 * 1000,
        offset_left=0,
        offset_top=0
   )

else:
    print ("Invalid display type!")


disp.begin()
def get_display(x, y, MESSAGE):
    # Initialize display.
    #disp.begin()
    WIDTH = disp.width
    HEIGHT = disp.height
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    t_start = time.time()
    #draw.rectangle((0, 0, disp.width, disp.height), (0, 0, 0))
    draw.text((x, y), MESSAGE, font=font, fill=(255, 255, 255))
    draw.text((0, 20), '--START', font=font, fill=(255, 255, 255))
    draw.text((0, 200), '--RESET', font=font, fill=(255, 255, 255))
    draw.text((240, 20), 'STOP--', font=font, fill=(255, 255, 255))
    draw.text((240, 200), 'OFF--', font=font, fill=(255, 255, 255))
    disp.display(img)


def daily_folder():
    get_image_time = datetime.now()
    camera_sub_dir = get_image_time.strftime("%Y_%m_%d")
    return camera_sub_dir


def make_new_dir():
    FUNCTION = 'GPS'
    HOME = Path.home()
    STORAGE_DIRECTORY = f'{HOME}/{FUNCTION}_{daily_folder()}'

    if os.path.exists(STORAGE_DIRECTORY):
        pass
    else:
        os.mkdir(STORAGE_DIRECTORY)
        #time.sleep(.5)
        #CSV_FILE = f'{STORAGE_DIRECTORY}/GPS_1.csv'
        #count = 0
        #form_gps.format_gps(CSV_FILE,count,LATITUDE,LONGITUDE,NAME,ALTITUDE,SPEED,DATE,TIME)
    #print (path)
    return STORAGE_DIRECTORY


def get_csv_num():
    try:
        count = 0
        STORAGE_DIRECTORY = make_new_dir()
        CSV_FILE = f'{STORAGE_DIRECTORY}/GPS_1.csv'
        if os.path.exists(CSV_FILE):
            print('CSV file: ',CSV_FILE)
            with open(CSV_FILE,'r') as read_file:
                line_count = len(read_file.readlines())
                print(line_count)
                count = line_count
        else:
            count = 0
            make_new_dir()

        return count

    except Exception as e:
        print('something went wrong try again ....', e)

    finally:
        pass

#Define the remote path file path
#remoteFilePath = '/tmp/home/data/'
#Define the localFilePath path file path
#localFilePath = make_new_dir(STORAGE_DIRECTORY) # '/home/rdl-nano2/rdl_mobile_tech/'

def get_logger(object, STORAGE_DIRECTORY):
    #logger
    LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
    logging.basicConfig(filename ='/'+STORAGE_DIRECTORY+'/gps.log',level=logging.DEBUG,format=LOG_FORMAT) #Append mode
    #logging.basicConfig(filename ='/XAVIER_RELEASE/test.log',level=logging.DEBUG,format=LOG_FORMAT,filemode='w') #Overwrite mode
    logger = logging.getLogger()
    log_info = logger.info(object)
    #logger.debug('test debug log')
    #logger.warning('test warning log')
    #logger.error('test error log')
    #logger.critical('test critical log')
    return log_info

#port = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
#gps = UbloxGps(port)


#!/usr/bin/env python3
#import time
#from pa1010d import PA1010D
#gps = PA1010D()

#count = get_csv_num()
def run(count):
    count = int(count)
    HOME = Path.home()
    FUNCTION = 'GPS'
    STORAGE_DIRECTORY = f'{HOME}/{FUNCTION}_{daily_folder()}'
    CSV_FILE = f'{STORAGE_DIRECTORY}/GPS_1.csv'
    try:
        #STORAGE_DIRECTORY = make_new_dir()
        result = gps.update()
        if result:
            TIMESTAMP = gps.timestamp
            LATITUDE = gps.latitude
            LONGITUDE = gps.longitude
            ALTITUDE = gps.altitude
            NUM_SATS = gps.num_sats
            GPS_QUAL = gps.gps_qual
            SPEED = gps.speed_over_ground
            FIX_TYPE = gps.mode_fix_type
            PDOP = gps.pdop
            VDOP = gps.vdop
            HDOP = gps.hdop

            coordinates = f'lat_{latitude}, lon_{longitude}, speed_{speed_over_ground}'
            get_logger(coordinates, STORAGE_DIRECTORY)
            #NO,LATITUDE,LONGITUDE,NAME,ALTITUDE,SPEED,DATE,TIME
            #NAME = count.zfill(3)
            NAME = count
            NAME = f'TP{NAME}'
            DATE = datetime.now().strftime('%Y/%m/%d')
            TIME = datetime.now().strftime('%H:%M:%S')
            form_gps.format_gps(CSV_FILE,count,LATITUDE,LONGITUDE,NAME,ALTITUDE,SPEED,DATE,TIME)
            #if count != None:
            #count = count + 1
            print('Longitude: ', LONGITUDE)
            print('Latitude: ', LATITUDE)
            global MESSAGE1
            MESSAGE1 = f'GPS LOGGING: {count}\nSAT: {NUM_SATS}' # print multiple lines on Pimoroni dhmini Display

    except (ValueError, IOError) as err:
        print(err)
    finally:
        pass

if __name__ == '__main__':
    RESET_BUTTON = False
    RESET = False
    count = get_csv_num()
    def cycle_logger(): # run schedule to cycle files at midnight
        time.sleep(1)
        os.system(f'rm -r {make_new_dir()}')
        time.sleep(2)
        make_new_dir()
        count = 0
        run(count)

    def reset_logger(): # run to reset log files to zero
        time.sleep(1)
        os.system(f'rm -r {make_new_dir()}')
        time.sleep(2)
        make_new_dir()
        count = 0
        run(count)

def midnight_schedule():
    global RESET
    RESET = True

#target=get_presence,args=[entries])
schedule.every().day.at('00:00').do(midnight_schedule)
#schedule.every().day.at('00:00').do(do_something)
while True:
    #RESET = True
    schedule.run_pending()

    START = False
    if START == True:
        run(count)

    #Reset logger with push button
    #RESET_BUTTON add push butto
    elif not GPIO.input(BUTTON_B_GPIO): # reset logger
        reset_logger()
        count = 0

    elif RESET == True:
        cycle_logger()
        count = 0
        RESET = False

    elif not GPIO.input(BUTTON_Y_GPIO): # stop logger
        pass

    elif not GPIO.input(BUTTON_X_GPIO): # stop logger
        break

    else:
        run(count)
    get_display(50, 110,MESSAGE1)  # get_display(x, y, message) x is vertical position and y is horizontal
    time.sleep(1)
    count = count + 1

