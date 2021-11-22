#!/usr/bin/env python3
import csv
import os
from pathlib import Path



def format_gps(FILENAME,NO,LATITUDE,LONGITUDE,NAME,ALTITUDE,SPEED,DATE,TIME): # requires 9 objects
#def format_gps():
    #FILENAME = 'TEST.csv'
    if os.path.exists(FILENAME):
        with open(FILENAME, 'a', newline='') as csvfile:
            fieldnames = ['No', 'Latitude','Longitude','Name','Altitude','Speed','Date','Time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'No':NO,'Latitude':LATITUDE,'Longitude':LONGITUDE,'Name':NAME,'Altitude':ALTITUDE,'Speed':SPEED,'Date':DATE,'Time':TIME})
    else:
        with open(FILENAME, 'a', newline='') as csvfile:
            fieldnames = ['No', 'Latitude','Longitude','Name','Altitude','Speed','Date','Time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'No':NO,'Latitude':LATITUDE,'Longitude':LONGITUDE,'Name':NAME,'Altitude':ALTITUDE,'Speed':SPEED,'Date':DATE,'Time':TIME})

