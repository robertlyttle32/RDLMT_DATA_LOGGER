#Author: Robert Lyttle
#Date: 10/22/21
#Description: download files matching file name or extension
#Remove each dowloaded file from remote server


import pysftp
import os
import time
import ftplib
import gzip
import shutil
#import pathlib
import glob
import fnmatch
import re
import logging
from pathlib import Path
from datetime import datetime


myHostname = 'hostname/IP'
myUsername = 'Username'
myPassword = 'Password'


cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

#myHostname = input('Enter IP address for avc: ')
#print('Enter file name or file extension you would like to download.')
#print('If file extion is used all file matching will be downloaded.')
FILE_NAME = '*.csv' #input('Enter file name or file extension: ')
#print('Enter name for directory you want to create. files will be downloaded this directory')
#tollPointDrectory = 'images' #input('Enter name: ')



def daily_folder():
    get_image_time = datetime.now()
    camera_sub_dir = get_image_time.strftime("%Y_%m_%d")
    return camera_sub_dir

tollPointDirectory = f'DATA_LOGS_{daily_folder()}'

HOME = Path.home()
#MODEL = 'vehicleModel'
#path = f'{HOME}/{tollPointDrectory}_{toll_point_folder()}'
#path = '/home/rld-toughdev/Desktop/DATA_LOGGER_DEV/'
####path = '/home/rld-toughdev/Desktop/DATA_LOGGER_DEV/DATA_LOGGER_RELEASE/'
path = '/home/rld-toughdev/Downloads/DATA_LOGGER_FILES/'+tollPointDirectory
STORAGE_DIRECTORY = path # Storage for database, images
if os.path.exists(STORAGE_DIRECTORY):
    pass
else:
    os.mkdir(STORAGE_DIRECTORY)


####remoteFilePath = '/home/pi/release'
#remoteFilePath = '/home/pi/DATA_LOGGER_DEV_2021'
remoteFilePath = '/home/pi/'+'GPS_'+daily_folder()+'/'
#remoteFilePath = '/home/rdl-garage/Desktop/REMOTE_DATA_LOGGER' #+toll_point_folder()
#Define the remote path file path
#remoteFilePath = '/tmp/home/data/'
#Define the localFilePath path file path
localFilePath = STORAGE_DIRECTORY # '/home/rdl-nano2/rdl_mobile_tech/'


#logger
LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename =localFilePath+'/file_download.log',level=logging.DEBUG,format=LOG_FORMAT) #Append mode
#logging.basicConfig(filename ='/XAVIER_RELEASE/test.log',level=logging.DEBUG,format=LOG_FORMAT,filemode='w') #Overwrite mode
logger = logging.getLogger()
#logger.info('This is a test log')
#logger.debug('test debug log')
#logger.warning('test warning log')
#logger.error('test error log')
#logger.critical('test critical log')


try:
    with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, cnopts=cnopts) as sftp:
        print("Connection succesfully established ... ")
        print('Downloading.....')
        for filename in sftp.listdir(remoteFilePath):
            if fnmatch.fnmatch(filename, FILE_NAME):
                print(filename)
                saved = filename.rstrip()
                saved = saved.split('-')
                #print(saved[3])
                #if count > final_count:
                sftp.get(remoteFilePath + "/" + filename, localFilePath + "/" + filename)
                logger.info(f'{localFilePath}/{filename} stored on local server')
                #sftp.remove(remoteFilePath+'/'+filename)
                logger.info(f'{remoteFilePath}/{filename} removed from remote sever')


        print()
        print('Process summary.....')
        print(datetime.now())
        print(f'Files from: {myHostname} directory {remoteFilePath}')
        logger.info(f'Files from: {myHostname} directory {remoteFilePath}')
        print(f'Files stored: {localFilePath}')
        logger.info(f'Files stored: {localFilePath}')
        size_info = sftp.stat(remoteFilePath)
        print(size_info.st_size)

        print('Done.....')

except Exception as e:
    print('connection lose ...', e)
