import socket,time,threading
from queue import Queue 
from random import randint as rand
import sys
sys.path.append('/home/sobhit/Desktop/ankit_python/home_automation')
from  configuration  import configure as config

start =  config.database['start']
stop =  config.database['stop']
count = 0
packet_type_1 =  config.database['packet_type_1']
slave_id = config.database['slave_id']
frequency_of_data_generation = config.database['frequency_of_data_generation']
data_format_of_packet1  = {}
temperature = 0
humidity = 0
sock_queue = Queue()


def packet_init():
        
    data_format_of_packet1['start_bit'] = start 
    data_format_of_packet1['packet_type ']= packet_type_1  
    data_format_of_packet1['payload_len']=2
    data_format_of_packet1['slave_id']=slave_id
    data_format_of_packet1['temperature']= 0  
    data_format_of_packet1['humidity']= 0
    data_format_of_packet1['stop_bit']=stop 
    data_format_of_packet1['checksum']= checksum_size_claculation()
    

def checksum_size_claculation():
    return 1+len(packet_type_1)+len(slave_id)+1+1+1

def packet_type_1_data_update(temperature,humidity):
    data_format_of_packet1['temperature'] = temperature
    data_format_of_packet1['humidity'] = humidity
    return data_format_of_packet1

def call_from_thread():
    sock_queue.put(call_for_update_payload())
    
def send_packet_1():
    global temperature,humidity
   
    while True:   
     
        time_object = threading.Timer(frequency_of_data_generation,call_from_thread,args=None, kwargs=None) 
        time_object.start()
        time_object.join()
        temperature = rand(10,30)
        humidity = rand(35,60)
        dict_received_periodically= sock_queue.get() 
        print(f'getting from thread {dict_received_periodically}')
        return dict_received_periodically
        
def call_for_update_payload():
    update_dict_receive = packet_type_1_data_update(temperature,humidity)
    return update_dict_receive
