import csv
import random,socket
import time
import sys
sys.path.append('/home/sobhit/Desktop/ankit_python/home_automation')
from  configuration  import configure as config

BUFFER_SIZE = config.database['BUFFER_SIZE']
time_as_x_value = 0
temperature_as_y_value = 1000
humidity_as_y_value = 1000
PORT = config.database['TCP_PORT_3']
HOST = config.database['host']
fieldnames = ["time_as_x_value", "temperature_as_y_value", "humidity_as_y_value"]

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

    def connect_to_socket(self, host, port):
        self.sock.connect((host, port))

    def listen_from_socket(self,number_of_module):
        self.sock.listen(number_of_module)

    def send_to_socket(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send_to_socket(msg)
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + len(msg)

    def receive_from_socket(self,connection_id):
        self.connection_id = connection_id
        bytes_string_rec_from_socket = self.connection_id.recv(BUFFER_SIZE)
        return bytes_string_rec_from_socket


'''Below convert_from_bytes_string function use for convert the bytes string into list,string or dictionary'''
def convert_from_bytes_string(b_string,attribute):
    if attribute == 's':
        rec_byte_string_string =b_string.decode("utf-8")      
        return rec_byte_string_string
    elif attribute == 'd':
        rec_byte_string_string =b_string.decode("utf-8")       
        dict_rec_from_socket = json.loads(rec_byte_string_string)      
        return dict_rec_from_socket
    else:
        rec_byte_string_string =b_string.decode("utf-8")       
        dict_rec_from_socket = json.loads(rec_byte_string_string)                    
        final_list_of_values = list(dict_rec_from_socket.values())  
        final_list_of_keys   = list(dict_rec_from_socket.keys())
        return final_list_of_values



'''My_socket class end here'''
socket_object_s3 = My_Socket()
socket_object_s3.bind_to_socket(HOST, PORT)
socket_object_s3.listen_from_socket(1)
connection_id, address_of_socket = socket_object_s3.accept_from_socket()

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

     
    print("Connected:", address_of_socket)
    connection_id.send(b'Thank you for connecting')
        
    bytes_string_rec = socket_object_s3.receive_from_socket(connection_id)   
    final_list = convert_from_bytes_string(bytes_string_rec,'l')

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "time_as_x_value": time_as_x_value,
            "temperature_as_y_value": final_list[4],
            "humidity_as_y_value": final_list[5]
        }

        csv_writer.writerow(info)
        print(time_as_x_value, temperature_as_y_value, humidity_as_y_value)

        time_as_x_value += 2
        

    time.sleep(1)
