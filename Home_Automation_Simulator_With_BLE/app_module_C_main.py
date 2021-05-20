import pdb
import socket
import json
import sys
sys.path.append('/home/sobhit/Desktop/ankit_python/home_automation')
from  configuration  import configure as config
#Declaration start from here

TCP_IP = config.database['host']
TCP_PORT2 = config.database['TCP_PORT_2']
TCP_PORT3 = config.database['TCP_PORT_3']
BUFFER_SIZE = config.database['BUFFER_SIZE']
res_dict = {}
final_list_of_values = []
final_list_of_keys = []
r_rec_byte_string_dict = {}
count = 0
count_again = 0




#Definations strat from here

class My_Socket:
    
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
    def bind_to_socket(self,host,port):
        self.sock.bind((host,port))

    def accept_from_socket(self):
        connection_id, address_of_socket = self.sock.accept()
        return connection_id,address_of_socket

    def connect_to_socket(self, host,port):
        self.sock.connect((host,port))

    def listen_from_socket(self,number_of_module):
        self.sock.listen(number_of_module)

    def send_to_socket(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg)
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + len(msg)

    def receive_from_socket(self,connection_id):
        self.connection_id = connection_id
        bytes_string_rec_from_socket = self.connection_id.recv(BUFFER_SIZE)
        return bytes_string_rec_from_socket
'''My_socket class end here'''
'''different functionality start from here'''




'''Below convert_from_bytes_string function use for convert the bytes string into list,string or dictionary'''
def convert_from_bytes_string(b_string,attibute):
    if attibute == 's':
        rec_byte_string_string =b_string.decode("utf-8")      
        return rec_byte_string_string
    elif attibute == 'd':
        rec_byte_string_string =b_string.decode("utf-8")       
        dict_rec_from_socket = json.loads(rec_byte_string_string)      
        return dict_rec_from_socket
    else:
        rec_byte_string_string =b_string.decode("utf-8")       
        dict_rec_from_socket = json.loads(rec_byte_string_string)                    
        final_list_of_values = list(dict_rec_from_socket.values())  
        final_list_of_keys   = list(dict_rec_from_socket.keys())
        return final_list_of_values

'''Below convert_into_bytes function  use to convert dictionary into bytes string'''
def convert_into_bytes(final_list_of_keys,final_list_of_values):
    updated_dict = {final_list_of_keys[i]: final_list_of_values[i] for i in range(0, len(lst))}   
    transfer_bytes_string = json.dumps(updated_dict).encode('utf-8')          
    return transfer_bytes_string       


'''socket programing start from here'''
'''socket acception part'''



#function is use to make the packet 2 
def send_packet_4_to_reset(receive_list):
    receive_list[1] = config.database['packet_type_4']
    receive_list[4] = 5
    receive_list[5] = 0
    
    transfer_bytes_string = convert_into_bytes(final_list_of_keys,receive_list)
    return transfer_bytes_string

#function is use to make packet to reset the slave
def send_packet_2(receive_list):
    receive_list[1] = config.database['packet_type_2']
    receive_list[4] = 2
    receive_list[5] = 0
    
    transfer_bytes_string = convert_into_bytes(final_list_of_keys,receive_list)
    return transfer_bytes_string



# To check_abnormality the abnormality rec_byte_string of temprature
def check_abnormality(final_list):    
    if final_list[4] < 30: # 
        count = 0
        
    else:
        count += 1
        if count == 5:
            transfer_bytes_string = send_packet_2(final_list_of_values)
            socket_object_c3.send_to_socket(transfer_bytes_string)
            while True:
                rec_byte_string= socket_object_s2.receive_from_socket(conn)    #Bytes string recieved in rec_byte_string
                final_list = convert_from_bytes_string(rec_byte_string,'l')
                if final_list[4] >= 30:
                    count_again += 1
                    if count_again == 10:
                        transfer_bytes_string = send_packet_4_to_reset(final_list)
                        socket_object_c3.send_to_socket(transfer_bytes_string)
                        break
                else:
                    count_again = 0
                    break            
        else:
            count = 0


#socket programing start from here
#Socket accept part
socket_object_s2= My_Socket()
socket_object_s2.bind_to_socket(TCP_IP,TCP_PORT2)
socket_object_s2.listen_from_socket(1)
connection_id, address_of_socket = socket_object_s2.accept_from_socket()
print(f'Connection address:{address_of_socket}')

#socket connect part
pdb.set_trace()
socket_object_c3 = My_Socket()
socket_object_c3.connect_to_socket(TCP_IP,TCP_PORT3)

#data communication start from here
while True:     #infinite loop
    rec_byte_string= socket_object_s2.receive_from_socket(connection_id)                #Bytes string recieved in rec_byte_string
    final_list = convert_from_bytes_string(rec_byte_string,'l')
    check_abnormality(final_list)                     #check_abnormalitying for abnormality in rec_byte_string

    print(f'packet type:{final_list[1]} and slave id : {final_list[3]}and pyload temp : {final_list[4]} and humidity{final_list[5]}')
    transfer_bytes_string = convert_into_bytes(final_list_of_keys,final_list_of_values)
    print(transfer_bytes_string)
    socket_object_c3.send_to_socket(transfer_bytes_string)
    connection_id.close()
    socket_object_c2.close()
    socket_object_s1.close()
connection_id.close()
