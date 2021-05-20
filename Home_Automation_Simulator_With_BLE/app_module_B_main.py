
import socket
import json
import sys
sys.path.append('/home/sobhit/Desktop/ankit_python/home_automation')
from  configuration  import configure as config

TCP_IP = config.database['host']
TCP_PORT1 = config.database['TCP_PORT_1']
TCP_PORT2 = config.database['TCP_PORT_2']
BUFFER_SIZE = config.database['BUFFER_SIZE']

final_list_of_values = []
final_list_of_keys = []



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

    def connect_to_socket(self,host,port):
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
        data_string =b_string.decode("utf-8")      
        return data_string
    elif attibute == 'd':
        data_string =b_string.decode("utf-8")       
        dict_rec_from_socket = json.loads(data_string)      
        return dict_rec_from_socket
    else:
        data_string =b_string.decode("utf-8")       
        dict_rec_from_socket = json.loads(data_string)                    
        final_list_of_values = list(dict_rec_from_socket.values())  
        final_list_of_keys   = list(dict_rec_from_socket.keys())
        return final_list_of_values

'''Below convert_into_bytes function  use to convert dictionary into bytes string'''
def convert_into_bytes(final_list_of_keys,final_list_of_values):
    updated_dict = {final_list_of_keys[i]: final_list_of_values[i] for i in range(0, len(lst))}   
    transfer_bytes_string = json.dumps(updated_dict).encode('utf-8')          
    return transfer_bytes_string       

def check_checksum_of_rec_data(check_sum.final_result[7]):
    if check_sum == final_result[7]:
        return True
    else:
        return False


'''socket programing start from here'''
'''socket acception part'''
socket_object_s1= My_Socket()
socket_object_s1.bind_to_socket(TCP_IP, TCP_PORT1)
socket_object_s1.listen_from_socket(1)
connection_id, address_of_socket = socket_object_s1.accept_from_socket()
print(f'Connection address:{address_of_socket}')


'''socket connection part'''
socket_object_c2 = My_Socket()
socket_object_c2.connect_to_socket(TCP_IP,TCP_PORT2)

'''Data communication start from here'''

while True:
    
    rec_byte_string = socket_object_s1.receive_from_socket(connection_id)
    final_result = convert_from_bytes_string(rec_byte_string ,'l')
    if final_result[3] == '0x12345678':
        if final_result[0] == 0xAA:
            payload_len = final_result[2]
            if final_result[payload_len+4] == 0xBB:
                check_sum = 1+len(config.database['packet_type_1'])+payload_len+len(config.database['slave_id'])+1+1
                ret = check_checksum_of_rec_data(check_sum,final_result[7])
                if ret:
                    if final_result[1] == '0xA1':
                        transfer_bytes_string = convert_into_bytes(final_list_of_keys,final_list_of_values) 
                        socket_object_c2.send_to_socket(transfer_bytes_string)

                    elif final_result[1] =='0xA2':
                        config.database['frequency_of_data_generation '] = final_result[4]

                    elif final_result[1] =='0xA4':
                        config.database['frequency_of_data_generation '] = final_result[4]
                        transfer_bytes_string = convert_into_bytes(final_list_of_keys,final_list_of_values) 
                        socket_object_c2.send_to_socket(transfer_bytes_string)

    else:
        break
    connection_id.close()
    socket_object_c2.close()
    socket_object_s1.close()



