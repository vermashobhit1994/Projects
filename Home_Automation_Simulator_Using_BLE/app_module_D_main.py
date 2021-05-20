#program to understand client
#!/usr/bin/env python3

import socket
import threading
import json
import logging
import sys
import logging
from logging.handlers import RotatingFileHandler
import datetime as dt

#import matplotlib
#matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import re
import numpy as np
import os


#PORT = 1234
PORT = 3459
HOST = 'localhost'
global s

fig = plt.figure("Temperature_Live_Plottig")
fig_hum = plt.figure("Humidty_Live_Plotting")
ax = fig.add_subplot(1, 1, 1)
ax_hum = fig_hum.add_subplot(1,1,1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)
#s.connect((HOST,PORT))


def plot_hum_data(ys_hum):
    plt.pause(0.001)
    ax_hum.plot(ys_hum)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    #plt.title('Humidity over Time')
    #plt.ylabel('Humdity(in %)')
    #plt.xlabel('DataSets')
    
    


def animate():
    xs = []
    ys = []
    xs_hum = []
    ys_hum = []
    
    
    logger=logging.getLogger() 
    logger.setLevel(logging.INFO) 
    handler = RotatingFileHandler("log_data.txt", maxBytes=2000000, backupCount=2)
    logger.addHandler(handler)
    c, addr = s.accept()
    while True:
        
        print("Connected:", addr)
        c.send(b'Thank you for connecting')
        
        data_receive = c.recv(1024)   
        #res_bytes = json.dumps(data_receive).encode('utf-8') 
        #res = json.loads(res_bytes) 
        data_string = data_receive.decode('utf-8')
        data_list = data_string.split(',')
        #data_list = list(res.values())
        #print('data_list',data_list)

        temp_list = re.findall(r'\d+', data_list[4])
        temp_list = list(map(int, temp_list))

        hum_list = re.findall(r'\d+', data_list[5])
        hum_list = list(map(int, hum_list))


        slave_list = re.findall(r'\d+', data_list[3])
        slave_list = list(map(int, slave_list))
                     
        temp = int(temp_list[0])
       
        
        slave_id = int(slave_list[0])
        logger.info('slave_id: '+str(slave_id)+' temp : '+str(temp))
        print('temp is',temp)

        xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        ys.append(temp)
        
        
        plt.pause(0.001)
        ax.plot(ys)
        
        
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        #plt.title('Temperature over Time')
        #plt.ylabel('Temperature (deg C)')
        #plt.xlabel('DataSets')


        hum = int(hum_list[0])
        
        slave_id = int(slave_list[0])
        logger.info('slave_id: '+str(slave_id)+' hum : '+str(hum))
        print('hum is',hum)

        xs_hum.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        ys_hum.append(hum)

        plot_hum_data(ys_hum)
        

        

  
if __name__ == "__main__":
    ani = animation.FuncAnimation(fig,fig_hum,animate,interval=1000)
    plt.show()


        
        

    
    

		
		
			

		
		

