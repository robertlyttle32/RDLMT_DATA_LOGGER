#!/bin/bash
import os
import time


while True:
    os.system('python3 get_remote_data_logger_files.py')
    print('running script: get_remote_data_logger_files.py')
    time.sleep(60)
    os.system('python3 get_remote_data_logger_files.py')
    print('running script: get_remote_data_logger_files.py')
    time.sleep(60)
