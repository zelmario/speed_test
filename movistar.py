# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:16:50 2021

@author: zelmario
"""

import speedtest #if not installed, install with: pip3 install speedtest-cli
import datetime
import time as t

servers = [1546] #URUGUAY server of speedtest
threads = None
s = speedtest.Speedtest()
s.get_servers(servers)

#bucle *will run every 5 mins)
while True:
    if datetime.datetime.now().strftime('%T')[4:] == '0:00' or datetime.datetime.now().strftime('%T')[4:] == '5:00':
        time = datetime.datetime.now().strftime('%T')
        s.download(threads=threads)
        s.upload(threads=threads)
        results_dict = s.results.dict()
        #extract download and upload speed and converto to MB/s
        download = round(results_dict.get('download') / 1e+6,2)
        upload = round(results_dict.get('upload') / 1e+6,2)
        
        #create csv line to write into the file
        csv = str(time) + ',' + str(download) + ',' + str(upload)
        print(csv)
        file_object = open('/home/pi/movistar.csv', 'a', encoding="utf-8") 
        file_object.write(csv + '\n')
        file_object.close()



