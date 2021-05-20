import random,threading,json
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time,socket,pdb
import logging,logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
Rotating_handler = logging.handlers.RotatingFileHandler(filename = 'data.csv',mode = 'a+',maxBytes = 1024,backupCount = 5)
logger.addHandler(Rotating_handler)
logger.debug('logger created')

PORT_C_D = 3547
HOST = 'localhost'
temp_list = []
humid_list = []
time_list = []

time_value = 0
plt.style.use('fivethirtyeight')

c = None
def write_data(temp_value,humid_value,slave_id):
	logger.debug( str(slave_id) +'\t'+ str(temp_value)+ '\t'+str(humid_value) +'\n')


def animate(i):
	
	data_receive = s.recv(1024)
		
	data_string = data_receive.decode('utf-8')
	data_dict = json.loads(data_string)
	       
                            
        final_list_of_values = list(data_dict.values())	
	
	temp_value = None
	humid_value = None
	slave_id = None
	temp_value = int(final_list_of_values[4])
	humid_value = int(final_list_of_values[5])
	slave_id = (final_list_of_values[3])

	global temp_list,humid_list
	temp_list.append(temp_value)
	humid_list.append(humid_value)
	 
	global time_value
	time_value += 1

	global time_list
	time_list.append(time_value)
	plt.cla()

	
	plt.plot(time_list,temp_list, label='Temperature_data')
	plt.plot(time_list,humid_list , label='Humidity_data')
	plt.legend(loc='upper left')
	
	print(temp_value,humid_value,slave_id)
	t1 = threading.Thread(target = write_data,args = [temp_value,humid_value,slave_id])
	t1.start()
	t1.join()

	
def plot_graph():
	print('before animate')	
	ani = FuncAnimation(plt.gcf(), animate,interval = 1000)
	print('after animate')
	plt.show()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT_C_D))
s.listen(5)

c,addr = s.accept()
time_value = 0


print('connected by address',addr)
plot_graph()
flag = 0
#s.close()
